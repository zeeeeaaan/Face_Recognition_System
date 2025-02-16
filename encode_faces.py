import os
import face_recognition
import pickle

# Define dataset path
DATASET_PATH = "dataset/"
ENCODINGS_FILE = "face_encodings.pkl"

# Create dataset folder if missing
if not os.path.exists(DATASET_PATH):
    os.makedirs(DATASET_PATH)
    print(f"⚠️ Created missing folder: {DATASET_PATH}")
    print("❌ No images found! Please add face images to 'dataset/' and rerun.")
    exit()

known_faces = []
known_names = []

# Process all images in the dataset folder
for filename in os.listdir(DATASET_PATH):
    if filename.endswith((".jpg", ".png", ".jpeg")):
        image_path = os.path.join(DATASET_PATH, filename)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if encodings:
            known_faces.append(encodings[0])
            known_names.append(os.path.splitext(filename)[0])  # Extract name from filename

# Save Encodings
with open(ENCODINGS_FILE, "wb") as f:
    pickle.dump({"encodings": known_faces, "names": known_names}, f)

print(f"✅ Encoded {len(known_faces)} faces and saved to {ENCODINGS_FILE}")
