import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

video = cv2.VideoCapture(0)

def get_frame_and_landmarks():
    ret, frame = video.read()
    if not ret:
        return None, None, None

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    left_hand = None
    right_hand = None

    if result.multi_hand_landmarks and result.multi_handedness:
        for hand_lm, handedness in zip(
            result.multi_hand_landmarks,
            result.multi_handedness
        ):
            label = handedness.classification[0].label  # 'Left' or 'Right'

            mp.solutions.drawing_utils.draw_landmarks(
                frame, hand_lm, mp_hands.HAND_CONNECTIONS
            )

            if label == "Left":
                left_hand = hand_lm.landmark
            else:
                right_hand = hand_lm.landmark

    return frame, left_hand, right_hand


