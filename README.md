# 🎯 DeepFace CCTV - Real-Time Face Recognition System

A simple yet powerful **real-time face recognition system** built using:

- DeepFace (ArcFace model)
- OpenCV
- Python
## Required
python 3.12

## Features
- Multi-face detection
- Multi-person recognition
- Automatic model download
- One-command installation
- Webcam-based real-time recognition

## Installation

### Windows
git clone https://github.com/Soutak1984/deepface-app.git

cd deepface-app
python -m venv venv
venv\Scripts\activate
or  python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt
install.bat

### Linux / Raspberry Pi
git clone https://github.com/Soutak1984/deepface-app.git

cd deepface-app

chmod +x install.sh

./install.sh

## Run
python app.py

## Notes
- ArcFace model (~130MB) downloads automatically on first run
- Press Q to exit

## Author
Soutak Biswas
