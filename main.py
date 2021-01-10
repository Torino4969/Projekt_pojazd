from inicjalizacjaLokalizacji import *
import cv2
filepath = "punktyReg.txt"
f = open(filepath, "r")
sterowanieM = False


def zmianaPunktu():
    f = open(filepath, "r")
    pozX =int(f.readline())
    pozY = int(f.readline())
    regulaorr.ustawieniePunktuDocelowego(pozX,pozY)
    f.close()

def lokalizacjaM():   
    frame = kamerka.obraz()    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, rejected = aruco.detectMarkers(image=gray, dictionary=aruco_dict, parameters=parameters,
                                                 cameraMatrix=kamera.macierz, distCoeff=kamera.dist)
    aruco.drawDetectedMarkers(frame, corners)
    cv2.imshow('frame', frame)
    estymacjaPolozenia(corners, ids)
    mapaa.wyczysc()
    mapaa.rysujPojazd(pojazdRobot)
    cv2.imshow('Mapa', mapaa.mapaUpr)
    if pojazdRobot.zlokalizowano == True and regulaorr.zlokalizowano == False:

        regulaorr.aktualizacjaLokalizacji(pojazdRobot.polozenie[0], pojazdRobot.polozenie[1], pojazdRobot.orientacja[2])
        ekont,sterowaniekont = regulaorr.regulacjaKonta()
        edroga, sterowaniedroga = regulaorr.regulacjaPolzenia()
        print("------------")
        #print(ekont)
        #print(edroga)
        print("------------")
        if math.fabs(edroga) < 50:
           regulaorr.ustalonoPozycje()
        elif math.fabs(ekont) >  10  and pojazdRobot.zlokalizowano == True:
           print("roznica konta: ")
           print(ekont)
           print("sterowanie: ")
           print(sterowaniekont)
           if ekont<0:
                silnik11.wprawo(abs(sterowaniekont),0.05)
                silnik11.stop(0.2)
           else:
                
                silnik11.wlewo(abs(sterowaniekont),0.05)
                silnik11.stop(0.2)
                
        elif pojazdRobot.zlokalizowano == True:
                print("roznica polozenia: ")
                print(edroga)
                print("sterowanie polozenia: ")
                print(sterowaniedroga)
                silnik11.doprzodu(sterowaniedroga,0.1)
                silnik11.stop(0.2)
    elif regulaorr.zlokalizowano == True:
        print("utrzymaj pozycje...")
        silnik11.stop(0.2)
    if pojazdRobot.zlokalizowano == False and regulaorr.zlokalizowano == False:
        if granicaSrodek(frame) == True:
            print("zawroc")
            #silnik11.wlewo(40,1.5)
            silnik11.doprzodu(40,0.1)
            silnik11.stop(0.1)
        elif granicaLewa(frame) == True:
            #print("skrec w prawo")
            #silnik11.wprawo(40,0.5)
            silnik11.doprzodu(40,0.1)
            silnik11.stop(0.1)
        elif granicaPrawo(frame) == True:
            #print("skrec w lewo")
            #silnik11.wlewo(40,0.5)
            silnik11.doprzodu(40,0.1)
            silnik11.stop(0.1)
        else:
            print("jedz na przod")
            silnik11.doprzodu(40,0.1)
            silnik11.stop(0.1)
    #pojazdRobot.informacje()

    for znacznik in znaczniki:
        znacznik.zerowanie()

def lokalizacjaM():
    frame = kamerka.frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, rejected = aruco.detectMarkers(image=gray, dictionary=aruco_dict, parameters=parameters,
                                                 cameraMatrix=kamera.macierz, distCoeff=kamera.dist)
    aruco.drawDetectedMarkers(frame, corners)
    cv2.imshow('frame', frame)
    estymacjaPolozenia(corners, ids)
    mapaa.wyczysc()
    mapaa.rysujPojazd(pojazdRobot)
    cv2.imshow('Mapa', mapaa.mapaUpr)
    for znacznik in znaczniki:
        znacznik.zerowanie()



if __name__ == '__main__':

       while True:
        if sterowanieM == False:
            lokalizacjaA()
        else:
            lokalizacjaM()
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            kamerka.cap.release()
            cv2.destroyAllWindows()
            f.close()
            break
        if key == ord('z'):
            zmianaPunktu()
        if key == ord('m'):
            sterowanieM = True
        if key == ord('n'):
            sterowanieM = False
        if key == ord('w') and sterowanieM == True:
            print("jedz do przodu")
            silnik11.doprzodu(70,0.1)
        if key == ord('s')and sterowanieM == True:
            print("stop")
            silnik11.stop(0.2)
        if key == ord('d')and sterowanieM == True:
            print("jedz w prawo")
            silnik11.wprawo(70,0.1)
        if key == ord('a')and sterowanieM == True:
            print("jedz w lewo")
            silnik11.wlewo(70,0.1)



