@echo off

echo Installing dependencies...
pip install -r requirements.txt

echo Creating DeepFace folder...
mkdir %USERPROFILE%\.deepface\weights

echo Downloading ArcFace model...

IF NOT EXIST "%USERPROFILE%\.deepface\weights\arcface_weights.h5" (
    powershell -Command "Invoke-WebRequest -Uri https://github.com/serengil/deepface_models/releases/download/v1.0/arcface_weights.h5 -OutFile %USERPROFILE%\.deepface\weights\arcface_weights.h5"
) ELSE (
    echo Model already exists, skipping download.
)

echo Setup complete!
pause