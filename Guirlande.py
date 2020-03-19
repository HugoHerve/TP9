from Decoration import Decoration

class Guirlande(Decoration):
    def __init__(self, longueur=0, couleur = "", masse=0 ):
        Decoration.__init__(self,couleur,masse)
        self._longueur = longueur

    def getLongueur(self):
        return self._longueurs

    def affiche(self):
        print("Guirlande de couleur",self._couleur,"de masse",self._masse,"g et de longueur", self._longueur,"cm")

