def finger_states(lm):
    fingers = []

    # thumb (x-axis)
    fingers.append(1 if lm[4].x > lm[2].x else 0)

    # other fingers (y-axis)
    tips = [8, 12, 16, 20]
    pips = [6, 10, 14, 18]

    for tip, pip in zip(tips, pips):
        fingers.append(1 if lm[tip].y < lm[pip].y else 0)

    return fingers  # [thumb, index, middle, ring, pinky]

def detect_direction(lm):
    wrist = lm[0]
    index = lm[8]

    dx = index.x - wrist.x
    dy = index.y - wrist.y

    if abs(dx) > abs(dy):
        if dx > 0.15:
            return "right"
        elif dx < -0.15:
            return "left"
    else:
        if dy < -0.15:
            return "up"
        elif dy > 0.15:
            return "down"

    return "center"


def custom_gesture(fingers, lm):
    # fist
    if fingers == [0, 0, 0, 0, 0]:
        return "fist"

    # thumbs up
    if fingers == [1, 0, 0, 0, 0] and lm[4].y < lm[0].y:
        return "thumbs up"

    # thumbs down
    if fingers == [1, 0, 0, 0, 0] and lm[4].y > lm[0].y:
        return "thumbs down"

    # call
    if fingers == [1, 0, 0, 0, 1]:
        return "call"
    
    # null / idle gesture
    return "nothing"


