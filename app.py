import cv2
import mediapipe as mp
import pyautogui
import math

pyautogui.FAILSAFE = False

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

def finger_up(hand_landmarks, idx):
    return hand_landmarks.landmark[idx].y < hand_landmarks.landmark[idx - 2].y

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                index_finger = hand_landmarks.landmark[8]
                x = int(index_finger.x * screen_w)
                y = int(index_finger.y * screen_h)

                pyautogui.moveTo(x, y)  # cursor movement

                # Fist gesture → left click
                fist = all(
                    hand_landmarks.landmark[i].y > hand_landmarks.landmark[0].y
                    for i in [8, 12, 16, 20]
                )
                if fist:
                    pyautogui.click()

                # Thumbs up → scroll up
                thumb_tip = hand_landmarks.landmark[4]
                thumb_ip = hand_landmarks.landmark[3]
                if thumb_tip.y < thumb_ip.y:
                    pyautogui.scroll(20)

                # Two fingers up → scroll down
                if finger_up(hand_landmarks, 8) and finger_up(hand_landmarks, 12):
                    pyautogui.scroll(-20)

        cv2.imshow("Gesture Mouse", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
