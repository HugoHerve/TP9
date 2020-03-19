from Decoration import Decoration

class Boule(Decoration):
    def __init__(self, diametre, couleur="", masse=0):
        Decoration.__init__(self, couleur, masse)
        self.__diametre = diametre

    def getDiametre(self):
        return self.__diametre

    def affiche(self):
        print("Boule de couleur ",self._couleur,"de masse",self._masse,"g et de diamètre",self.__diametre,"cm")
