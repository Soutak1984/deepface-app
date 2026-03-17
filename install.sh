#!/bin/bash

echo "Updating system..."
sudo apt update

echo "Installing Python & pip..."
sudo apt install -y python3 python3-pip wget

echo "Installing Python dependencies..."
pip3 install -r requirements.txt

echo "Creating DeepFace weights folder..."
mkdir -p ~/.deepface/weights

echo "Downloading ArcFace model (if not exists)..."

if [ ! -f ~/.deepface/weights/arcface_weights.h5 ]; then
    wget -O ~/.deepface/weights/arcface_weights.h5 \
    https://github.com/serengil/deepface_models/releases/download/v1.0/arcface_weights.h5
else
    echo "ArcFace model already exists, skipping download."
fi

echo "✅ Setup complete!"
echo "Run: python3 app.py"