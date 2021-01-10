import math
import numpy as np


class Kamera():
    def __init__(self, macierz, dist ):
        self.macierz = macierz
        self.dist = dist

class ArucoZ():
    def __init__(self, id, translacja, rotacja,rozmiar ):
        self.id = id
        self.translacja = translacja
        self.rotacja = rotacja
        self.rozmiar = rozmiar
        self.alfa = rotacja[0] * (math.pi / 180)
        self.beta = rotacja[1] * (math.pi / 180)
        self.gamma = rotacja[2] * (math.pi / 180)
        self.macierzRPY = np.float32([[math.cos(self.alfa) * math.cos(self.beta),
                                  math.cos(self.alfa) * math.sin(self.beta) * math.sin(self.gamma) - math.sin(self.alfa) * math.cos(self.gamma),
                                  math.cos(self.alfa) * math.sin(self.beta) * math.cos(self.gamma) + math.sin(self.alfa) * math.sin(self.gamma)],
                                 [math.sin(self.alfa) * math.cos(self.beta),
                                  math.sin(self.alfa) * math.sin(self.beta) * math.sin(self.gamma) + math.cos(self.alfa) * math.cos(self.gamma),
                                  math.sin(self.alfa) * math.sin(self.beta) * math.cos(self.gamma) - math.cos(self.alfa) * math.sin(self.gamma)],
                                 [-math.sin(self.beta), math.cos(self.beta) * math.sin(self.gamma), math.cos(self.beta) * math.cos(self.gamma)]])

        self.rozpoznano = False
        self.polozenieRobota = [0, 0, 0]
        self.orientacjaRobota = [0, 0, 0]

    def obliczanieWspol(self,pos_camera):

        self.polozenieRobota[0] = (self.macierzRPY * pos_camera)[0] + self.translacja[0]
        self.polozenieRobota[1] = (self.macierzRPY * pos_camera)[1] + self.translacja[1]
        self.polozenieRobota[2] = (self.macierzRPY * pos_camera)[2] + self.translacja[2]


    def rozpoznanie(self, id):
        if (self.id == id):
            self.rozpoznano = True


    def informacje(self):

        if (self.rozpoznano == True):
            print(self.id)
            print(self.polozenieRobota[0])
            print(self.polozenieRobota[1])
            print(self.polozenieRobota[2])
            print("Orientacja: ")
            print(self.orientacjaRobota[0])
            print(self.orientacjaRobota[1])
            print(self.orientacjaRobota[2])
            print("---------------------------------------------")

    def zerowanie(self):
        self.rozpoznano = False

    def obliczanieOrien(self, rvec):
        
        rvecc =   self.macierzRPY * rvec

        sy = math.sqrt(rvecc[0, 0] * rvecc[0, 0] + rvecc[1, 0] * rvecc[1, 0])

        degeneracja = sy < 1e-6

        if not degeneracja:
            
            y = math.atan2(-rvecc[2, 0], sy)
            ycos= math.cos(y)
            
            x = math.atan2(rvecc[2, 1]/ycos, rvecc[2, 2]/ycos)
            z = math.atan2(rvecc[1, 0]/ycos, rvecc[0, 0]/ycos)


        else:
            x = math.atan2(-rvecc[1, 2], rvecc[1, 1])
            y = math.atan2(-rvecc[2, 0], sy)
            z = 0

        self.orientacjaRobota[0] = x * (180/math.pi)
        self.orientacjaRobota[1] = y * (180/math.pi)
        self.orientacjaRobota[2] = z * (180/math.pi)





