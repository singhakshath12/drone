import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("gesture_cnn.keras")

labels = ["DOWN", "LEFT", "RIGHT", "UP"]

CONF_THRESHOLD = 0.6 # confidence threshold

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        continue    

    h, w, _ = frame.shape
    crop = frame[h//4:3*h//4, w//4:3*w//4]  # center crop
    img = cv2.resize(crop, (64,64))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img, verbose=0)
    confidence = np.max(pred)
    class_id = np.argmax(pred)

    if confidence > CONF_THRESHOLD:
        gesture = labels[class_id]
    else:
        gesture = "NOTHING"

    # display result
    cv2.putText(frame, gesture,
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.4,
        (0, 0, 0),
        3)

    cv2.imshow("cnn gesture control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
