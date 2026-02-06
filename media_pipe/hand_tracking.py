import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

video = cv2.VideoCapture(0)

def get_frame_and_landmarks():
    ret, frame = video.read()
    if not ret:
        print ("no camera")

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    landmarks = None
    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        landmarks = hand.landmark
        mp.solutions.drawing_utils.draw_landmarks(
            frame, hand, mp_hands.HAND_CONNECTIONS
        )

    return frame, landmarks
