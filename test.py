from Sapin import *
from Decoration import *
from Boule import *
from Guirlande import*
from GuirlandeLumineuse import *

sapin = Sapin(4000,0)
sapin.afficheSapin()
boule1 = Boule(2,"Rouge",200)
#boule1.afficheBoule()
sapin.addDeco(boule1)
sapin.afficheSapin()
guirlande1 = Guirlande(10,"Rouge",200)
sapin.addDeco(guirlande1)
sapin.afficheSapin()
sapin.supprDeco(boule1)
sapin.afficheSapin()
boule2 = Boule(4,"Rose",4000)
sapin.addDeco(boule2)
sapin.afficheSapin()
