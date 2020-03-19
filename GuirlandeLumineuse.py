from Guirlande import Guirlande

class GuirlandeLumineuse(Guirlande):
    def __init__(self, couleur = "", masse=0,longueur = 0, nblumieres=0):
        Guirlande.__init__(self,couleur,masse,longueur)
        self.__nblumires = nblumieres
    def getNblumires(self):
        return self.__nblumires
    def affiche(self):
        print("Guirlande lumineuse de couleur",self._couleur,"de masse",self._masse,"de longueur",self._longueur,"et comprenant",self.__nblumires)
