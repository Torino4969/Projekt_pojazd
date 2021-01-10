import cv2
import numpy as np
import math

czcionka = cv2.FONT_HERSHEY_SIMPLEX

class Mapa:
    def __init__(self,wysokosc, szerokosc, xWymiar, yWymiar,skala ,margines):
        self.wysokosc = wysokosc
        self.szerokosc = szerokosc
        self.xWymiar = xWymiar
        self.yWymiar = yWymiar
        self.margines = margines
        self.skala = skala
        self.mapaUpr = np.zeros((self.wysokosc,self.szerokosc,3), np.uint8 )
        self.mapaUpr = cv2.rectangle(self.mapaUpr, (self.margines , self.margines) , ( int(self.xWymiar * self.skala+self.margines)  , int(self.yWymiar * self.skala + self.margines)  ), (255,255,255), 1 )
        self.wyczyszcony = np.zeros((self.wysokosc,self.szerokosc,3), np.uint8 )
        self.wyczyszcony = cv2.rectangle(self.mapaUpr, (self.margines, self.margines), (
        int(self.xWymiar * self.skala + self.margines), int(self.yWymiar * self.skala + self.margines)),
                                     (255, 255, 255), 1)



    def defrysujZnaczniki(self,znaczniki):
        for znacznik in znaczniki:
            poczatekX = int( self.margines - (znacznik.rozmiar/2)*self.skala + float(znacznik.translacja[0])*self.skala)
            poczatekY = int(self.yWymiar*self.skala - (znacznik.rozmiar/2)*self.skala - float(znacznik.translacja[1])*self.skala + self.margines)
            koniecX = int(self.margines+(znacznik.rozmiar / 2 )* self.skala + float(znacznik.translacja[0]) * self.skala  )
            koniecY = int(self.yWymiar*self.skala - znacznik.rozmiar / 2 * self.skala - float(znacznik.translacja[1]) * self.skala+ znacznik.rozmiar * self.skala + self.margines)

            self.wyczyszcony=cv2.rectangle(self.wyczyszcony, ( poczatekX ,poczatekY), ( koniecX, koniecY), (255,255,255),1 )
            self.wyczyszcony=cv2.putText(self.wyczyszcony, str(znacznik.id),(poczatekX, koniecY - 2),czcionka,0.6 * self.skala ,(255,255,255),1 )
            cv2.imwrite("wyczysc.jpg",self.wyczyszcony)


    def wyczysc(self):

        self.mapaUpr = cv2.imread("wyczysc.jpg")


    def rysujPojazd(self,pojazd):

        punkt2_X = int(self.margines  -  self.skala * math.sin((pojazd.orientacja[2]*math.pi)/180) * (pojazd.wymiarX/2) + self.skala * pojazd.polozenie[0])
        punkt2_Y = int(self.yWymiar*self.skala  -  self.skala * math.cos((pojazd.orientacja[2]*math.pi)/180) * (pojazd.wymiarX/2)- self.skala * pojazd.polozenie[1] + self.margines)
        punkt1_X =int(self.margines  +   self.skala * math.sin((pojazd.orientacja[2]*math.pi)/180) * (pojazd.wymiarX/2) + self.skala * pojazd.polozenie[0])
        punkt1_Y = int(self.yWymiar*self.skala   +  self.skala * math.cos((pojazd.orientacja[2]*math.pi)/180) * (pojazd.wymiarX/2)- self.skala * pojazd.polozenie[1] + self.margines)

        punkt3_X = int(punkt2_X - self.skala * math.cos((pojazd.orientacja[2]*math.pi)/180) * pojazd.wymiarY)
        punkt3_Y = int(punkt2_Y + self.skala * math.sin((pojazd.orientacja[2]*math.pi)/180) * pojazd.wymiarY)
        punkt4_X = int(punkt1_X - self.skala * math.cos((pojazd.orientacja[2] * math.pi) / 180) * pojazd.wymiarY)
        punkt4_Y = int(punkt1_Y + self.skala * math.sin((pojazd.orientacja[2] * math.pi) / 180) * pojazd.wymiarY)

        if pojazd.zlokalizowano == True:
            kolor = (0,255,0)
        else:
            kolor = (0,0,255)



        self.mapaUpr = cv2.line(self.mapaUpr, ( punkt1_X ,punkt1_Y), ( punkt2_X, punkt2_Y), kolor,1 )
        self.mapaUpr = cv2.line(self.mapaUpr, (punkt2_X, punkt2_Y), (punkt3_X, punkt3_Y), (255, 255, 255), 1)
        self.mapaUpr = cv2.line(self.mapaUpr, (punkt1_X, punkt1_Y), (punkt4_X, punkt4_Y), (255, 255, 255), 1)
        self.mapaUpr = cv2.line(self.mapaUpr, (punkt3_X, punkt3_Y), (punkt4_X, punkt4_Y), (255, 255, 255), 1)





