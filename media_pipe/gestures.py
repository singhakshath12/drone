import math

def finger_states(lm):
    fingers = []

    # thumb (distance-based)
    thumb_tip = lm[4]
    thumb_mcp = lm[2]
    fingers.append(1 if abs(thumb_tip.x - thumb_mcp.x) > 0.04 else 0)

    # index, middle, ring, pinky
    tips = [8, 12, 16, 20]
    pips = [6, 10, 14, 18]

    for tip, pip in zip(tips, pips):
        fingers.append(1 if lm[tip].y < lm[pip].y else 0)

    return fingers  # [thumb, index, middle, ring, pinky]


def detect_direction(lm):
    if lm is None:
        return None

    # index finger MCP → TIP
    mcp = lm[5]
    tip = lm[8]

    dx = tip.x - mcp.x
    dy = tip.y - mcp.y  # y increases downward

    H_TH = 0.08
    V_TH = 0.08

    if abs(dx) > abs(dy):
        if dx > H_TH:
            return "left"
        elif dx < -H_TH:
            return "right"
    else:
        if dy > V_TH:
            return "down"
        elif dy < -V_TH:
            return "up"

    return None


def calculate_speed(lm):
    if lm is None:
        return 0.0

    thumb = lm[4]
    index = lm[8]

    dist = math.sqrt(
        (thumb.x - index.x) ** 2 +
        (thumb.y - index.y) ** 2
    )

    MIN_D = 0.04
    MAX_D = 0.25

    dist = max(min(dist, MAX_D), MIN_D)
    speed = (dist - MIN_D) / (MAX_D - MIN_D)

    return round(speed, 1)
