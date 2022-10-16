# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:57:47 2022

@author: joela
"""

import numpy as np
from MEC1315_STL import *
from Fonctions import *
import random 




#====================Terrain de soccer=========================
cube=LireSTL('Cube.stl')

terrain = cube
terrain = Affinite(terrain, 3000, 3000, 20)
terrain = Centre_000(terrain)
terrain = Translation(terrain, 0, 0, 10)
#=======================Drapeaux de coin=========================
triangle =LireSTL('Triangle.stl')
cylindre =LireSTL('Cylindre.stl')

tige=cylindre
tige=Affinite(tige, 30, 30, 300)
tige=Translation(tige, -1230, -1230, 0)
tige=Repetition_Rectangulaire(tige, 2, 'y', 4900)

drapeau=triangle
drapeau=Affinite(drapeau, 50, 50, 30)
drapeau=Rotation_x_y_z(drapeau, 'y', 90)
drapeau=Rotation_x_y_z(drapeau, 'z', -90)
drapeau=Translation(drapeau, -1215, -1215, 300)
drapeau=Repetition_Rectangulaire(drapeau, 2, 'y', 4900)

#=======================TEEMO=========================#
perso=LireSTL('Teemo_nobase.stl')
teemo=perso
teemo=Homotetie(teemo, 22)
teemo=Translation(teemo, 0, 200, 20)
teemo=Rotation_x_y_z(teemo, 'z', 290)

#=======================Ballon=========================#
ico=LireSTL('icosahedron.stl')
ballon=ico
ballon=Homotetie(ballon, 100)
ballon=Translation(ballon, -1000, 0, 0)
ballon=Repetition_Circulaire(ballon, random.randint(4, 9), 'y', 250, 0, 100, 0.5)

#=======================Lumieres=========================
panneau1 = LireSTL('Cylindre.stl')
panneau1 = Affinite(panneau1, 100, 100, 1500)
panneau1 = Translation(panneau1, -1400, -1400, 0)
panneau2 = LireSTL('Cube.stl')
panneau2 = Affinite(panneau2, 100, 600, 400)
panneau2 = Centre_000(panneau2)
panneau2 = Translation(panneau2, -1400, -1400, 1500)
lumieres = LireSTL('icosahedron.stl')
lumieres = Affinite(lumieres, 100, 100, 100)
lumieres = Repetition_Rectangulaire(lumieres, 3, 'y', 600)
lumieres = Repetition_Rectangulaire(lumieres, 2, 'z', 400)
lumieres = Centre_000(lumieres)
lumieres = Translation(lumieres, -1250, -1350, 1500)
panneau = Fusion(panneau1, panneau2, lumieres)
panneau = Repetition_Rectangulaire(panneau, 2, 'y', 5600)

#===========================Estrades============================
estradeTriangle= LireSTL('Triangle.stl')
estradeTriangle = Rotation_x_y_z(estradeTriangle, 'y', -90)
estradeTriangle = Rotation_x_y_z(estradeTriangle, 'z', 180)
estradeTriangle = Affinite(estradeTriangle, 3000, 1000, 1000)
estradeTriangle = Translation(estradeTriangle, -1500, 2500, 0)
estradeBanc1= LireSTL('Triangle.stl')
estradeBanc1 = Rotation_x_y_z(estradeBanc1, 'y', 90)
estradeBanc1= Affinite(estradeBanc1, 3000, 333, 333)
estradeBanc1 = Translation(estradeBanc1, -1500, 1500, 333)
estradeBanc2= LireSTL('Triangle.stl')
estradeBanc2 = Rotation_x_y_z(estradeBanc2, 'y', 90)
estradeBanc2= Affinite(estradeBanc2, 3000, 333, 333)
estradeBanc2= Translation(estradeBanc2, -1500, 1833, 666)
estradeBanc3= LireSTL('Triangle.stl')
estradeBanc3 = Rotation_x_y_z(estradeBanc3, 'y', 90)
estradeBanc3= Affinite(estradeBanc3, 3000, 333, 333)
estradeBanc3 = Translation(estradeBanc3, -1500, 2166, 999)
estrade = Fusion(estradeTriangle,estradeBanc1,estradeBanc2,estradeBanc3)



#================Fusion+export======================#

terrain_f=Fusion(terrain,tige,drapeau,teemo,ballon,panneau,estrade)




nom_fichier='Scene_69.stl'


fj=terrain_f[0]
vj=terrain_f[1]
nj=terrain_f[2]

EcrireSTLASCII(nom_fichier,fj,vj,nj)
