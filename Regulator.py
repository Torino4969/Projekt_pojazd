import math


              
class Regulator:
    def __init__(self,pozRx,pozRy,pozX,pozY,orient):
        self.pozRx = pozRx
        self.pozRy = pozRy
        self.pozX = pozX
        self.pozY = pozY
        self.orient = orient
        self.zlokalizowano = False

    def regulacjaKonta(self):

        alfa = math.atan2(self.pozY - self.pozRy , self.pozX - self.pozRx)
        ekont = -self.orient + alfa * 180 / math.pi
        if ekont >180:
            ekont = ekont - 360
        if ekont < -180:
            ekont = ekont + 360
        
        sygnalK = abs(ekont)
        if  sygnalK > 120:
            sygnalK = 80
        elif  sygnalK <= 120 and sygnalK > 60 :
            sygnalK = 70
        elif  sygnalK <=60:
            sygnalK = 60

        return ekont,sygnalK

    def regulacjaPolzenia(self):

        dx = self.pozX - self.pozRx
        dy = self.pozY - self.pozRy
        sygnalD = math.sqrt(dx*dx + dy*dy)
        #if sygnalD > self.gGorny:
        #    sygnalD = self.gGorny
        #if sygnalD < self.gDolny:
        #    sygnalD = self.gDolny
        if  sygnalD > 300:
            sygnalD = 80
        elif  sygnalD <= 300 and sygnalD > 100 :
            sygnalD = 70
        elif  sygnalD <=100:
            sygnalD = 60

        return math.sqrt(dx*dx + dy*dy), sygnalD

    def aktualizacjaLokalizacji(self, pozRx, pozRy, orient):

        self.pozRx = pozRx
        self.pozRy = pozRy
        self.orient = orient

    def ustawieniePunktuDocelowego(self, pozX,pozY):

        self.pozX = pozX
        self.pozY = pozY
        self.zlokalizowano = False

    def ustalonoPozycje(self):

        self.zlokalizowano = True



