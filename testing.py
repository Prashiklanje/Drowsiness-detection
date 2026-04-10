import cv2
import numpy as np
from tensorflow import keras

# Load model
model = keras.models.load_model(
    r'C:\Users\ujjwa\Desktop\Drowsiness ML\Drowsiness_model.h5'
)

# Load Haar cascades
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)

cap = cv2.VideoCapture(0)

counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Default values (IMPORTANT)
    status = "No Face"
    color = (255, 255, 0)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            eye = roi_color[ey:ey+eh, ex:ex+ew]

            eye = cv2.resize(eye, (128, 128))
            eye = eye / 255.0
            eye = eye.reshape(1, 128, 128, 3)

            pred = model.predict(eye)

            if pred[0][0] > 0.5:
                status = "Open Eyes"
                color = (0, 255, 0)
                counter = 0
            else:
                status = "Closed Eyes"
                color = (0, 0, 255)
                counter += 1

            break
        break

    #  Drowsiness Alert
    if counter > 5:
        cv2.putText(frame, " DROWSY!", (100, 200),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)

    #  Display
    cv2.putText(frame, status, (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow("Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()