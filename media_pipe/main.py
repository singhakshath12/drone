import cv2
from hand_tracking import get_frame_and_landmarks
from gestures import finger_states, detect_direction, calculate_speed

while True:
    frame, left_lm, right_lm = get_frame_and_landmarks()
    if frame is None:
        continue

    display_text = "nothing"
    speed_text = "0.0"

    # RIGHT HAND - SPEED
    if right_lm:
        speed = calculate_speed(right_lm)
        speed_text = str(speed)

    # LEFT HAND - HESTURE
    if left_lm:
        direction = detect_direction(left_lm)
        if direction:
            display_text = direction
        else:
            fingers = finger_states(left_lm)

            # FIST
            if fingers == [0, 0, 0, 0, 0]:
                display_text = "fist"

            # OPEN PALM
            elif fingers == [1, 1, 1, 1, 1]:
                display_text = "palm open"

            else:
                display_text = "nothing"

    cv2.putText(
        frame,
        display_text,
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0, 0, 0),
        3
    )

    cv2.putText(
        frame,
        speed_text,
        (20, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0, 0, 0),
        3
    )

    cv2.imshow("MEDIAPIPE", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
