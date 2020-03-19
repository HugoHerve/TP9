class Sapin():
    def __init__(self, masseMax=0, massetotal=0, deco=[]):
        self.__masseMax = masseMax
        self.__massetotaldeco = massetotal
        self.__decoration = deco


    def addDeco (self, element):
        self.__decoration.append(element)
        self.__massetotaldeco += element.getMasse()
    def supprDeco (self, element):
        self.__decoration.remove(element)
        self.__massetotaldeco -= element.getMasse()
    def afficheSapin(self):
        print("Le sapin de Noël peut supporter", self.__masseMax,"g de décoration.")
        if len(self.__decoration) == 0:
            print("Il ne contient actuellement aucune décoration")
            print("----------")
        else:
            print("Il contient actuellement",len(self.__decoration),"décoration(s), la masse totale de déco est de",self.__massetotaldeco,'g')
            if self.__massetotaldeco > self.__masseMax :
                print("Le sapin est trop chargé !!!!!!!")
            for i in self.__decoration:
                  i.affiche()
            print("----------")


