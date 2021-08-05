import cv2
import numpy as np
import imutils

def nothing(x):
    pass



cv2.namedWindow('track')

cv2.createTrackbar('lowh','track',22,180,nothing)
cv2.createTrackbar('lows','track',108,255,nothing)
cv2.createTrackbar('lowv','track',125,255,nothing)
cv2.createTrackbar('highh','track',31,180,nothing)
cv2.createTrackbar('highs','track',183,255,nothing)
cv2.createTrackbar('highv','track',186,255,nothing)

cap  = cv2.VideoCapture(1)
while(cap.isOpened()):
    ret,img = cap.read()
    lowh = cv2.getTrackbarPos('lowh','track')
    lows = cv2.getTrackbarPos('lows','track')
    lowv = cv2.getTrackbarPos('lowv','track')
    highh = cv2.getTrackbarPos('highh','track')
    highs = cv2.getTrackbarPos('highs','track')
    highv = cv2.getTrackbarPos('highv','track')
    low = (lowh, lows, lowv)
    high = (highh, highs, highv)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,low,high)
    filtered = cv2.GaussianBlur(mask,(5,5),5)
    cv2.imshow('img',img)
    cv2.imshow('q', mask)
    cv2.imshow('Filter',filtered)
    if cv2.waitKey(25) % 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
