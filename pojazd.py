class Pojazd:
    def __init__(self,wymiarX,wymiarY):
        self.wymiarX = wymiarX
        self.wymiarY = wymiarY
        self.zlokalizowano = False
        self.polozenie = [0,0,0]
        self.orientacja = [0,0,0]

    def lokalizacja(self, zloka):
        if (zloka == True):
            self.zlokalizowano =True
        else:
            self.zlokalizowano = False
    def aktualizacjaPolozenia(self,znaczniki):

        liczbaRozp = 0
        starePolozenie = self.polozenie
        staraOrientacja = self.orientacja
        self.polozenie = [0,0,0]
        self.orientacja = [0,0,0]

        for znacznik in znaczniki:
            if znacznik.rozpoznano == True:
                liczbaRozp += 1
                self.polozenie[0] += znacznik.polozenieRobota[0]
                self.polozenie[1] += znacznik.polozenieRobota[1]
                self.polozenie[2] += znacznik.polozenieRobota[2]

                self.orientacja[0] += znacznik.orientacjaRobota[0]
                self.orientacja[1] += znacznik.orientacjaRobota[1]
                self.orientacja[2] += znacznik.orientacjaRobota[2]

        if(liczbaRozp>=1):
            print(liczbaRozp)
            self.polozenie[0] = self.polozenie[0] / liczbaRozp
            self.polozenie[1] = self.polozenie[1] / liczbaRozp
            self.polozenie[2] = self.polozenie[2] / liczbaRozp
            self.orientacja[0] = self.orientacja[0] / liczbaRozp
            self.orientacja[1] = self.orientacja[1] / liczbaRozp
            self.orientacja[2] = self.orientacja[2] / liczbaRozp
            self.zlokalizowano = True
        else:
            self.polozenie = starePolozenie
            self.orientacja = staraOrientacja
            self.zlokalizowano = False

    def informacje(self):
        if (self.zlokalizowano == True):
            print("Polozenie pojazdu (aktualne): ")
        else:
            print("Polozenie pojazdu (nie aktualne): ")
        print(self.polozenie[0])
        print(self.polozenie[1])
        print(self.polozenie[2])
        if (self.zlokalizowano == True):
            print("Orientacja pojazdu (aktualna): ")
        else:
            print("Orientacja pojazdu (nie aktualna): ")

        print(self.orientacja[0])
        print(self.orientacja[1])
        print(self.orientacja[2])
        print("---------------------------------------------")

