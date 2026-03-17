import cv2
import os
from deepface import DeepFace
from deepface.modules import verification
import os
import urllib.request

model_path = os.path.expanduser("~/.deepface/weights/arcface_weights.h5")

if not os.path.exists(model_path):
    print("Downloading ArcFace model...")
    os.makedirs(os.path.dirname(model_path), exist_ok=True)

    url = "https://github.com/serengil/deepface_models/releases/download/v1.0/arcface_weights.h5"
    urllib.request.urlretrieve(url, model_path)

    print("Download complete!")
    
# Folder containing known faces
db_path = "faces"

known_embeddings = []
known_names = []

print("Loading known faces...")

for file in os.listdir(db_path):

    if file.endswith(".jpg") or file.endswith(".png"):

        path = os.path.join(db_path, file)

        rep = DeepFace.represent(
            img_path=path,
            model_name="ArcFace",
            enforce_detection=False
        )

        embedding = rep[0]["embedding"]

        known_embeddings.append(embedding)

        name = os.path.splitext(file)[0]
        known_names.append(name)

print("Loaded:", known_names)

# Webcam
cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

while True:

    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        face = frame[y:y+h, x:x+w]

        try:
            rep = DeepFace.represent(
                img_path=face,
                model_name="ArcFace",
                enforce_detection=False
            )

            emb = rep[0]["embedding"]

            name = "Unknown"
            best_distance = 999

            for i, known_emb in enumerate(known_embeddings):

                dist = verification.find_cosine_distance(known_emb, emb)

                if dist < best_distance:
                    best_distance = dist
                    name = known_names[i]

            if best_distance > 0.68:
                name = "Unknown"
                color = (0,0,255)
            else:
                color = (0,255,0)

        except:
            name = "Error"
            color = (255,255,0)

        cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)
        cv2.putText(frame,name,(x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,color,2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
