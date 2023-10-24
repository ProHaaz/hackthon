import serial.tools.list_ports
import pyautogui
import string
import cv2 as cv
import mediapipe as m
import time

def gestures():     # hand gestures
    t = 0
    print('starting....')
    mp = m.solutions.hands
    hands = mp.Hands(False, 1)
    draw = m.solutions.drawing_utils
    cap = cv.VideoCapture(0)
    cap.set(3, 1000)
    cap.set(4, 1000)
    x1 = x2 = 0
    to_check = [(8, 6), (12, 10), (16, 14), (20, 18)]
    while True:
        bol, img = cap.read()
        img = cv.flip(img, 3)
        # img = cv.flip(img, 1)
        img1 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        process = hands.process(img1)
        lm = process.multi_hand_landmarks
        h, w, d = img.shape

        if lm:
            shree = []
            Shree = []
            for hand in lm:
                draw.draw_landmarks(img, hand, mp.HAND_CONNECTIONS)
                for id, coord in enumerate(hand.landmark):
                    x = int(coord.x * w)
                    y = int(coord.y * h)
                    # print(id, x, y)
                    shree.append((x, y))

            num = 0
            for i in to_check:
                if shree[i[0]][1] > shree[i[1]][1]:
                    Shree.append(1)
                    num += 1
                else:
                    Shree.append(0)
            if shree[4][0] < shree[2][0]:
                num += 1
                Shree.append(1)
            else:
                Shree.append(0)

            nfv = 0
            for nf in range(0, 5):
                nfv = nfv + Shree[nf]
            print(nfv)

            if nfv == 0:
                time.sleep(0.2)
                t = t + 1
                if t == 10:
                    t =0
                    print('no fingers are closed')
                    with open('gst.txt', 'w') as fg0:
                        fg0.write('5')
                    # Send data to frontend that no five fingers are closed
            if nfv == 1:
                time.sleep(0.2)
                t = t + 1
                if t == 10:
                    t = 0
                    print('one finger is closed')
                    with open('gst.txt', 'w') as fg1:
                        fg1.write('4')
                    # Send data to frontend that one finger is closed
            if nfv == 2:
                time.sleep(0.2)
                t = t + 1
                if t == 10:
                    t = 0
                    print('two finger are closed')
                    with open('gst.txt', 'w') as fg2:
                        fg2.write('3')
                    # Send data to frontend that two finger are closed
            if nfv == 3:
                time.sleep(0.2)
                t = t + 1
                if t == 10:
                    t = 0
                    print('3 fingers are closed')
                    with open('gst.txt', 'w') as fg3:
                        fg3.write('2')
                    # Send data to frontend that 3 fingers are closed
            if nfv == 4:
                time.sleep(0.2)
                t = t + 1
                if t == 10:
                    t = 0
                    print('4 fingers are closed')
                    with open('gst.txt', 'w') as fg4:
                        fg4.write('1')
                    # Send data to frontend that 4 fingers are closed
            if nfv == 5:
                time.sleep(0.2)
                t = t + 1
                if t == 10:
                    t = 0
                    print('5 fingers are closed')
                    with open('gst.txt', 'w') as fg5:
                        fg5.write('0')
                    # Send data to frontend that 5 fingers are closed

            print(Shree)
            cv.putText(img, str(num), (150, 150), cv.FONT_HERSHEY_PLAIN, 12, (255, 0, 0), 12)
        cv.imshow('', img)
        if cv.waitKey(1) & 0xFF == ord('c'):
            break

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

serialInst.baudrate = 9600
serialInst.port = 'COM4'
serialInst.open()
usr = 0

with open('user.txt', 'w') as us:
    us.write('User 0')
with open('gst.txt', 'w') as gus:
    gus.write('-')


while True:
    if serialInst.in_waiting:
        pp = serialInst.readline()
        # print(pp.decode('utf'))
        x, y = pyautogui.position()

        a = pp.decode('utf')
        print(a)
        with open('The_data.txt', 'w') as fw:
            fw.write(str(a.translate({ord(c): None for c in string.whitespace})))
        with open('The_data.txt', 'r') as fr:
            uid = fr.readlines()
        if uid[0] == 'RFIDTagUID:33B10C17':
            usr = 1
            break
        elif uid[0] == 'RFIDTagUID:7A81CF5C':
            usr = 2
            break

if usr == 1:
    # Send data to frontend as user 1
    print('User 1')
    with open('user.txt', 'w') as fus:
        fus.write('User 1')
    gestures()
if usr == 2:
    # Send data to frontend as user 2
    print('User 2')
    gestures()