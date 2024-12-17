import cv2
import mediapipe
from cvzone.HandTrackingModule import HandDetector

camera = cv2.VideoCapture(0)  # video için yazılan kod

mpHands = mediapipe.solutions.hands  # burda eli tanımlıyoruz

hands = mpHands.Hands()  # elin şekil ve biçimini tanımlıyoruz

mpDraw = mediapipe.solutions.drawing_utils  # el de gözüken noktalar için yazılan kod

detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:

    success, img = camera.read()  # kameradan gelen görüntüyü okuma

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # kameradan gelen BGR görüntüsünü RGB ye çeviriyoruz

    hlms = hands.process(imgRGB)  # elden gelen görüntünün konum yerini

    height, width, channel = img.shape  # konumun bölgesini belirliyor

    mands, img = detector.findHands(img)

    if mands:
        mand1 = mands[0]
        lmList1 = mand1["lmList"]

    if hlms.multi_hand_landmarks:  # eğer bir konum varsa diye soruyoruz
        for handlandmarks in hlms.multi_hand_landmarks:  # eldeki tüm noktaları geziyoruz

            for fingerNum, landmark in enumerate(handlandmarks.landmark):  # el numarası ve konumu geziyoruz
                positionX, positionY = int(landmark.x * width), int(
                    landmark.y * height)  # konumun sayılarını belirliyoruz

                if fingerNum == 4 and landmark.y < handlandmarks.landmark[6].y and (
                        handlandmarks.landmark[12].y > handlandmarks.landmark[10].y) and (
                        handlandmarks.landmark[8].y > handlandmarks.landmark[3].y) and (
                        handlandmarks.landmark[4].y < handlandmarks.landmark[20].y):
                    print("A")

                if fingerNum == 4 and landmark.x > handlandmarks.landmark[13].x and (
                        handlandmarks.landmark[12].y < handlandmarks.landmark[8].y):
                    print("B")
                    # if fingerNum == 12 and (landmark.x > handlandmarks.landmark[5].x) and (handlandmarks.landmark[4].x > handlandmarks.landmark[8].x):
                # print("C")
                if fingerNum == 8 and (landmark.y < handlandmarks.landmark[12].y) and (
                        landmark.y < handlandmarks.landmark[4].y) and (landmark.x > handlandmarks.landmark[20].x):
                    print("D")

                    # if fingerNum == 4 and (landmark.x > handlandmarks.landmark[20].x)and (handlandmarks.landmark[8].x > handlandmarks.landmark[16].x) and (handlandmarks.landmark[8].y < handlandmarks.landmark[12].y):
                    # print("G")

                # if fingerNum == 8 and (landmark.y > handlandmarks.landmark[10].y) and (handlandmarks.landmark[4].y < handlandmarks.landmark[5].y):
                # print("F")

                # if fingerNum == 4 and (landmark.x > handlandmarks.landmark[16].x) and (handlandmarks.landmark[12].x > handlandmarks.landmark[16].x) and (landmark.y < handlandmarks.landmark[20].y):
                # print("H")

                if fingerNum == 20 and landmark.y < handlandmarks.landmark[16].y and (
                        handlandmarks.landmark[4].x > handlandmarks.landmark[6].x):
                    print("I")

                if fingerNum == 4 and (landmark.x > handlandmarks.landmark[8].x) and (
                        landmark.x < handlandmarks.landmark[12].x) and (landmark.y < handlandmarks.landmark[16].y):
                    print("K")

            mpDraw.draw_landmarks(img, handlandmarks, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Camera", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
