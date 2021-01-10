import numpy as np
import cv2

def nothing(x):
    pass


def granicaLewa(frame):

    frame1 = frame[600:720, 0:426]
    hsv1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    l_b = np.array([0, 100, 100])
    u_b = np.array([5, 255, 255])
    FGmask1 = cv2.inRange(hsv1, l_b, u_b)
    count1 = cv2.countNonZero(FGmask1)
    print("liczba pikseli dla lewej: " )
    print(count1)
    #cv2.imshow('final1', FGmask1)
    if count1>5000:
        return True
    else:
        return False

def granicaSrodek(frame):

    frame2 = frame[600:720, 427:852]
    hsv2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
    l_b = np.array([0, 100, 100])
    u_b = np.array([5, 255, 255])
    FGmask2 = cv2.inRange(hsv2, l_b, u_b)
    count2 = cv2.countNonZero(FGmask2)
    print("liczba pikseli dla srodkowej :")
    print(count2)
    #cv2.imshow('final2', FGmask2)
    if count2>3000:
        return True
    else:
        return False

def granicaPrawo(frame):

    frame3 = frame[600:720, 852:1280]
    hsv3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2HSV)
    l_b = np.array([0, 100, 100])
    u_b = np.array([5, 255, 255])
    FGmask3 = cv2.inRange(hsv3, l_b, u_b)
    count3 = cv2.countNonZero(FGmask3)
    print("liczba pikseli dla prawej: " )
    print(count3)
    #cv2.imshow('final3', FGmask3)
    if count3>5000:
        return True
    else:
        return False




