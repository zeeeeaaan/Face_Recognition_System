import cv2
import face_recognition
import numpy as np
import pandas as pd
import pickle
import os
from datetime import datetime

# Load Face Encodings
encodings_file = "face_encodings.pkl"
if not os.path.exists(encodings_file):
    print("⚠️ Error: No encoded faces found! Run encode_faces.py first.")
    exit()

with open(encodings_file, "rb") as f:
    data = pickle.load(f)
known_faces = data["encodings"]
known_names = data["names"]

# Load or Create Attendance File
csv_filename = "attendance.csv"

# Check if the CSV file exists and is empty
def create_csv_if_empty():
    if not os.path.exists(csv_filename):
        df = pd.DataFrame(columns=["Name", "Time", "Status"])
        df.to_csv(csv_filename, index=False)
        print(f"⚠️ Created an empty {csv_filename} file.")
    else:
        # If the file is empty, add headers
        if os.path.getsize(csv_filename) == 0:
            df = pd.DataFrame(columns=["Name", "Time", "Status"])
            df.to_csv(csv_filename, index=False)
            print(f"⚠️ {csv_filename} was empty. Added headers.")

create_csv_if_empty()

# Initialize Webcam
cap = cv2.VideoCapture(0)

# Recognize Faces & Mark Attendance
def mark_attendance(name):
    df = pd.read_csv(csv_filename)

    # Prevent duplicate attendance entries
    if name not in df["Name"].values:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_entry = pd.DataFrame([{"Name": name, "Time": now, "Status": "Present"}])
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_csv(csv_filename, index=False)
        print(f"✅ Marked {name} present at {now}")


while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"

        if True in matches:
            match_index = np.argmax(matches)
            name = known_names[match_index]
            mark_attendance(name)

        # Draw Rectangle & Name
        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    # Display Webcam Feed
    cv2.imshow("Face Recognition Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
