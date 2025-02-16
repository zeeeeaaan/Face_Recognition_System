# Face_Recognition_System

📌 Project Overview

The Facial Recognition Attendance System is a Python-based application that automates the process of marking attendance using facial recognition technology. It captures faces, encodes them, and recognizes registered users to log attendance in a CSV file.

🛠️ Features

Stores and encodes multiple users' faces.

Real-time face detection and recognition.

Attendance logging in a CSV file.

Prevents duplicate entries for the same user on the same day.

Uses OpenCV and dlib for facial recognition.

📂 Project Structure
Facial_Recognition_Attendance/
│── dataset/                # Stores user face images
│── attendance.csv         # Stores attendance records
│── encode_faces.py        # Encodes face images and saves data
│── attendance_system.py   # Main script for recognition and attendance marking
│── requirements.txt       # Required Python packages

1️⃣ Install Required Libraries
pip install opencv-python numpy pandas face-recognition


📦 Dependencies

Ensure you have Python installed and then install the required libraries:
pip install -r requirements.txt

requirements.txt:
numpy
opencv-python
pandas
face-recognition
dlib
datetime


🚀 How to Run the Project

Capture & Encode Faces:

python encode_faces.py

This script will scan the dataset/ folder, encode faces, and store them.

Run the Attendance System:

python attendance_system.py

This will start real-time face recognition and mark attendance in attendance.csv.

🖼️ How It Works

Place user images inside the dataset/ folder with names as Username.jpg.

Run encode_faces.py to create face encodings.

Start attendance_system.py to recognize faces and log attendance.

