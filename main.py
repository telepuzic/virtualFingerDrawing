import cv2
import mediapipe as mp
import numpy as np
import detecting_fingers
import math


#создаем детектор
handsDetector = mp.solutions.hands.Hands()
cap = cv2.VideoCapture(0)
a = []
colors = [(82, 5, 123), (154, 240, 100), (20, 213, 193), (220, 20, 60)] # создание массива  с цветами и их изначальное определение
current_color = (82, 5, 123) # начальный цвет
while(cap.isOpened()):
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q') or not ret:
        break
    flipped = np.fliplr(frame)
    # переводим его в формат RGB для распознавания
    flippedRGB = cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB)
    # Распознаем
    results = handsDetector.process(flippedRGB) # распознаем руку
    if results.multi_hand_landmarks is not None:
        mp.solutions.drawing_utils.draw_landmarks(flippedRGB,
                                                  results.multi_hand_landmarks[0], mp.solutions.hands.HAND_CONNECTIONS)
        if detecting_fingers.second_finger_up(results) and detecting_fingers.third_finger(results) and detecting_fingers.forth_finger(results) and detecting_fingers.fifth_finger_down(results) and math.hypot(int(results.multi_hand_landmarks[0].landmark[8].x *
                             flippedRGB.shape[1]) - 250, int(results.multi_hand_landmarks[0].landmark[8].y *
                    flippedRGB.shape[0]) - 50) <= 50: # распознаем положение разогнутого указательного пальца и согнутых остальных чтобы изменить цвет на фиолетовый
            current_color = (82, 5, 123)
        elif detecting_fingers.second_finger_up(results) and detecting_fingers.third_finger(results) and detecting_fingers.forth_finger(results) and detecting_fingers.fifth_finger_down(results) and math.hypot(int(results.multi_hand_landmarks[0].landmark[8].x *
                             flippedRGB.shape[1]) - 350, int(results.multi_hand_landmarks[0].landmark[8].y *
                    flippedRGB.shape[0]) - 50) <= 50: # распознаем положение разогнутого указательного пальца и согнутых остальных чтобы изменить цвет на зеленый
            current_color = (154, 240, 100)
        elif detecting_fingers.second_finger_up(results) and detecting_fingers.third_finger(results) and detecting_fingers.forth_finger(results) and detecting_fingers.fifth_finger_down(results) and math.hypot(int(results.multi_hand_landmarks[0].landmark[8].x *
                             flippedRGB.shape[1]) - 450, int(results.multi_hand_landmarks[0].landmark[8].y *
                    flippedRGB.shape[0]) - 50) <= 50: # распознаем положение разогнутого указательного пальца и согнутых остальных чтобы изменить цвет на бирюзовый
            current_color = (20, 213, 193)
        elif detecting_fingers.second_finger_up(results) and detecting_fingers.third_finger(results) and detecting_fingers.forth_finger(results) and detecting_fingers.fifth_finger_down(results) and math.hypot(int(results.multi_hand_landmarks[0].landmark[8].x *
                             flippedRGB.shape[1]) - 550, int(results.multi_hand_landmarks[0].landmark[8].y *
                    flippedRGB.shape[0]) - 50) <= 50: # распознаем положение разогнутого указательного пальца и согнутых остальных чтобы изменить цвет на красный
            current_color = (220, 20, 60)
        elif detecting_fingers.second_finger_up(results) and detecting_fingers.third_finger(results) and detecting_fingers.forth_finger(results) and detecting_fingers.fifth_finger_down(results): # распознаем положение разогнутого указательного пальца и согнутых остальных чтобы рисовать на экране
            x_tip = int(results.multi_hand_landmarks[0].landmark[8].x *
                    flippedRGB.shape[1]) # координата x подушечки указательного пальца
            y_tip = int(results.multi_hand_landmarks[0].landmark[8].y *
                    flippedRGB.shape[0]) # координата y подушечки указательного пальца
            a += [[current_color, x_tip, y_tip]] # сохранение координат подушечки указательного пальца и цвета которым должно быть нарислвано
        elif detecting_fingers.second_finger_down(results) and detecting_fingers.third_finger(results) and detecting_fingers.forth_finger(results) and detecting_fingers.fifth_finger_down(results): # распознавание кулака для отчистки экрана
            a=[] # очищение массива, то есть стирание с экрана (будет так же в поседующих строчках кода
        elif detecting_fingers.second_finger_down(results) and detecting_fingers.third_finger(results) and detecting_fingers.forth_finger(results) and detecting_fingers.fifth_finger_up(results): # распознавание мизинца для изменения цвета
            m = colors.index(current_color) # нахождение индекса цвета, которым сейчас рисуем
            if m < len(colors) - 1:
                current_color = colors[m+1]
            else:
                current_color = colors[0]
    for i in range(len(a)):
        cv2.circle(flippedRGB, (a[i][1], a[i][2]), 10, a[i][0], -1) # непосредственно рисование
    cv2.circle(flippedRGB, (50, 50), 50, current_color, -1) # кружок, который показывает каким цветом сейчас рисуете
    cv2.circle(flippedRGB, (250, 50), 50, (82, 5, 123), -1) # кружок, показав на который рисуете фиолетовым
    cv2.circle(flippedRGB, (350, 50), 50, (154, 240, 100), -1) # кружок, показав на который рисуете зеленым
    cv2.circle(flippedRGB, (450, 50), 50, (20, 213, 193), -1) # кружок, показав на который рисуете бирюзовым
    cv2.circle(flippedRGB, (550, 50), 50, (220, 20, 60), -1) # кружок, показав на который рисуете красным
    res_image = cv2.cvtColor(flippedRGB, cv2.COLOR_RGB2BGR)
    cv2.imshow("Hands", res_image)

# освобождаем ресурсы
handsDetector.close()