import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm
import pyautogui
cap = cv2.VideoCapture(0)
pTime = 0
cTime = 0
detector = htm.handDetector(detectionCon=0.75)
tipIds =[4,8,12,16,20]
while True:
    success , img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPostiotin(img)
    if len(lmList) != 0 :
        fingers = []
        # Thump
        # if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
        #     fingers.append(1)
        # else:
        #     fingers.append(0)
        for id in range(1,5) :
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2] :
                fingers.append(1)
            else :
                fingers.append(0)

        totalFingers = fingers.count(1)
        if(totalFingers > 0 ) :
            pyautogui.press('space')
       # cv2.rectangle(img , (20 , 255) , (170,424) , (0,255,0) , cv2.FILLED)
       # cv2.putText(img , str(totalFingers) , (45 , 375) , cv2.FONT_HERSHEY_PLAIN , 10 , (255 , 0 ,0) , 25)
       #print(totalFingers)
    cTime = time.time()
    fps = 1 /(cTime - pTime)
    pTime = cTime
   # cv2.putText(img , str(int(fps)) , (10 , 70) , cv2.FONT_HERSHEY_PLAIN , 3 , (255,0,255) , 3 )
    cv2.imshow("Jumper" , img)
    cv2.waitKey(1)


















