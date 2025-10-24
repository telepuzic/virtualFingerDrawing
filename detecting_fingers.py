import math


def second_finger_up(results): # распознование разогнутого указательного пальца
    a5x = results.multi_hand_landmarks[0].landmark[5].x
    a5y = results.multi_hand_landmarks[0].landmark[5].y
    a6x = results.multi_hand_landmarks[0].landmark[6].x
    a6y = results.multi_hand_landmarks[0].landmark[6].y
    a7x = results.multi_hand_landmarks[0].landmark[7].x
    a7y = results.multi_hand_landmarks[0].landmark[7].y
    a8x = results.multi_hand_landmarks[0].landmark[8].x
    a8y = results.multi_hand_landmarks[0].landmark[8].y
    a0x = results.multi_hand_landmarks[0].landmark[0].x
    a0y = results.multi_hand_landmarks[0].landmark[0].y
    if math.hypot(a5x-a0x, a5y-a0y) < math.hypot(a6x-a0x, a6y-a0y) < math.hypot(a7x-a0x, a7y-a0y) < math.hypot(a8x-a0x, a8y-a0y):
        return True


def second_finger_down(results): # распознование согнутого указательного пальца
    a8x = results.multi_hand_landmarks[0].landmark[16].x
    a8y = results.multi_hand_landmarks[0].landmark[16].y
    a7x = results.multi_hand_landmarks[0].landmark[15].x
    a7y = results.multi_hand_landmarks[0].landmark[15].y
    a5x = results.multi_hand_landmarks[0].landmark[13].x
    a5y = results.multi_hand_landmarks[0].landmark[13].y
    a0x = results.multi_hand_landmarks[0].landmark[0].x
    a0y = results.multi_hand_landmarks[0].landmark[0].y
    n7 = math.hypot(a7x - a0x, a7y - a0y)
    n8 = math.hypot(a8x - a0x, a8y - a0y)
    n5 = math.hypot(a5x - a0x, a5y - a0y)
    if n5 / 3 * 2 > n8 or n5 / 3 * 2 > n7:
        return True


def third_finger(results): # распознование согнутого среднего пальца
    a12x = results.multi_hand_landmarks[0].landmark[12].x
    a12y = results.multi_hand_landmarks[0].landmark[12].y
    a11x = results.multi_hand_landmarks[0].landmark[11].x
    a11y = results.multi_hand_landmarks[0].landmark[11].y
    a9x = results.multi_hand_landmarks[0].landmark[9].x
    a9y = results.multi_hand_landmarks[0].landmark[9].y
    a0x = results.multi_hand_landmarks[0].landmark[0].x
    a0y = results.multi_hand_landmarks[0].landmark[0].y
    n11 = math.hypot(a11x-a0x, a11y-a0y)
    n12 = math.hypot(a12x-a0x, a12y-a0y)
    n9 = math.hypot(a9x-a0x, a9y-a0y)
    if n9 / 3 * 2 > n12 or n9 / 3 * 2 > n11:
        return True


def forth_finger(results): # распознование согнутого безымянного пальца
    a16x = results.multi_hand_landmarks[0].landmark[16].x
    a16y = results.multi_hand_landmarks[0].landmark[16].y
    a15x = results.multi_hand_landmarks[0].landmark[15].x
    a15y = results.multi_hand_landmarks[0].landmark[15].y
    a13x = results.multi_hand_landmarks[0].landmark[13].x
    a13y = results.multi_hand_landmarks[0].landmark[13].y
    a0x = results.multi_hand_landmarks[0].landmark[0].x
    a0y = results.multi_hand_landmarks[0].landmark[0].y
    n15 = math.hypot(a15x - a0x, a15y - a0y)
    n16 = math.hypot(a16x - a0x, a16y - a0y)
    n13 = math.hypot(a13x - a0x, a13y - a0y)
    if n13 / 3 * 2 > n16 or n13 / 3 * 2 > n15:
        return True


def fifth_finger_down(results): # распознование согнутого мизинца
    a20x = results.multi_hand_landmarks[0].landmark[20].x
    a20y = results.multi_hand_landmarks[0].landmark[20].y
    a19x = results.multi_hand_landmarks[0].landmark[19].x
    a19y = results.multi_hand_landmarks[0].landmark[19].y
    a17x = results.multi_hand_landmarks[0].landmark[17].x
    a17y = results.multi_hand_landmarks[0].landmark[17].y
    a0x = results.multi_hand_landmarks[0].landmark[0].x
    a0y = results.multi_hand_landmarks[0].landmark[0].y
    n19 = math.hypot(a19x - a0x, a19y - a0y)
    n20 = math.hypot(a20x - a0x, a20y - a0y)
    n17 = math.hypot(a17x - a0x, a17y - a0y)
    if n17 / 3 * 2 > n20 or n17 / 3 * 2 > n19:
        return True


def fifth_finger_up(results): # распознование разогнутого мизинца
    a20x = results.multi_hand_landmarks[0].landmark[20].x
    a20y = results.multi_hand_landmarks[0].landmark[20].y
    a19x = results.multi_hand_landmarks[0].landmark[19].x
    a19y = results.multi_hand_landmarks[0].landmark[19].y
    a18x = results.multi_hand_landmarks[0].landmark[18].x
    a18y = results.multi_hand_landmarks[0].landmark[18].y
    a17x = results.multi_hand_landmarks[0].landmark[17].x
    a17y = results.multi_hand_landmarks[0].landmark[17].y
    a0x = results.multi_hand_landmarks[0].landmark[0].x
    a0y = results.multi_hand_landmarks[0].landmark[0].y
    if math.hypot(a17x-a0x, a17y-a0y) < math.hypot(a18x-a0x, a18y-a0y) < math.hypot(a19x-a0x, a19y-a0y) < math.hypot(a20x-a0x, a20y-a0y):
        return True