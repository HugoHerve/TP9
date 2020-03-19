from abc import ABC, abstractmethod
class Decoration(ABC):                                             # Est une classe abstraite car contient une méthode abstraite
    def __init__(self, couleur="" , masse=0):
        self._couleur = couleur
        self._masse = masse

    def getCouleur(self):
        return self._couleur
    def getMasse(self):
        return self._masse

    @abstractmethod
    def affiche(self):                                   # Méthode abstraite
        pass
