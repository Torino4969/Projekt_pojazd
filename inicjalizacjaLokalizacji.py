import pojazd
import mapa
import znacznik as zn
import cv2.aruco as aruco
import cv2
import numpy as np
import regulator as reg
import math
import threading
from silnik1 import Silnik
from krawedz import granicaLewa,granicaPrawo,granicaSrodek

czcionka = cv2.FONT_HERSHEY_SIMPLEX


#inicjalizacja pojazdu
pojazdRobot = pojazd.Pojazd(150,260)


#deklaracja znaczników:
#znacznik71 = zn.ArucoZ(71,[0,0,0],[0,0,0],30)
#znacznik72 = zn.ArucoZ(72,[0, 200, 0],[0,0,0],30)
#znacznik73 = zn.ArucoZ(73,[390, 200, 0],[0,0,0],30)
#znacznik74 = zn.ArucoZ(74,[390, 0, 0],[0,0,0],30)

#deklaracja znaczników2:

znacznik71 = zn.ArucoZ(71,[150,150,0],[0,0,0],100)
znacznik72 = zn.ArucoZ(72,[1050, 150, 0],[0,0,0],100)
znacznik73 = zn.ArucoZ(73,[1050, 850, 0],[0,0,0],100)
znacznik74 = zn.ArucoZ(74,[150, 850, 0],[0,0,0],100)
znacznik75 = zn.ArucoZ(75,[600, 500, 0],[0,0,0],100)
znacznik81 = zn.ArucoZ(81,[540, 1000, 50],[0,0,90],100)




znaczniki = [znacznik71,znacznik72,znacznik73,znacznik74,znacznik75,znacznik81 ]

#kamera:
kamera = zn.Kamera(np.float32([[998.7279, 0.0, 658.5191], [0.0, 998.7279, 347.5342], [0.0, 0.0, 1.0]]) , np.float32([0, 0, 0, 0]))

#aruco:
marker_size = 100.0
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_ARUCO_ORIGINAL)
parameters = aruco.DetectorParameters_create()

#obraz z kamery:
#cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
#font = cv2.FONT_HERSHEY_PLAIN
#ret, frame = cap.read()

class StreamKamery(threading.Thread):
    def __init__(self, threadId, kamera):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.kamera = kamera
        self.cap = cv2.VideoCapture(kamera)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.ret, self.frame = self.cap.read()
        self.daemon =True

    def run(self):
        while True:
            self.ret, self.frame = self.cap.read()

    def obraz(self):
        return self.frame

kamerka = StreamKamery(1,0)
kamerka.start()

#strzalki wspolrzednych znacznikow:
strzalki3d_2 = np.float32([[0, 0, 0], [40, 0, 0], [0, 40, 0], [0, 0, 40]])
strzalki2d_2 = np.float32([[0, 0], [0, 0], [0, 0], [0, 0]])

# macierz przeksztalcenia obrotu o 180 wokol osi X:
R_flip  = np.zeros((3,3), dtype=np.float32)
R_flip[0,0] = 1.0
R_flip[1,1] =-1.0
R_flip[2,2] =-1.0

# deklaracja mapy

mapaa = mapa.Mapa(1000,1000,1200,1000,0.7,30)
mapaa.defrysujZnaczniki(znaczniki)
mapaa.wyczysc()

#deklaracja regulatora


regulaorr = reg.Regulator(0,0,500,750,0)

#deklaracja silnika:

silnik11 = Silnik(2, 3, 4, 17, 22, 27)


def estymacjaPolozenia(corners, ids):
    if ids is not None:
        n = 0
        for id_roz in ids:

            for znacznik in znaczniki:
                if id_roz == znacznik.id:

                    ret = aruco.estimatePoseSingleMarkers(corners[n], marker_size, kamera.macierz,
                                                          kamera.dist)
                    rvec, tvec = ret[0][0, 0, :], ret[1][0, 0, :]
                    R_ct = np.matrix(cv2.Rodrigues(rvec)[0])
                    R_tc = R_ct.T
                    pos_camera = -R_tc * np.matrix(tvec).T
                    znacznik.rozpoznanie(id_roz)
                    znacznik.obliczanieWspol(pos_camera)
                    znacznik.obliczanieOrien(R_tc*R_flip)
            n+=1

    pojazdRobot.aktualizacjaPolozenia(znaczniki)
    #pojazdRobot.informacje()




