import cv2
from media.hand_tracking import get_frame_and_landmarks
from media.gestures import finger_states, detect_direction, custom_gesture

while True:
    frame, lm = get_frame_and_landmarks()

    if frame is None:
        continue

    gesture_text = "nothing"

    if lm:
        fingers = finger_states(lm)
        custom = custom_gesture(fingers, lm)

        if custom:
            gesture_text = custom

        else:
            direction = detect_direction(lm)

            if direction in ["UP", "DOWN", "LEFT", "RIGHT"]:
                 gesture_text = direction
            else:
                gesture_text = "nothing"


    cv2.putText(
        frame,
        gesture_text,
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0, 0, 0),
        3
    )

    cv2.imshow("Hand Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()