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
#=======================Drapeaux de coin======================
triangle =LireSTL('Triangle.stl')
cylindre =LireSTL('Cylindre.stl')

tige=cylindre
tige=Affinite(tige, 30, 30, 300)
tige=Translation(tige, -800, -1230, 0)
tige=Repetition_Rectangulaire(tige, 2, 'y', 4900)

drapeau=triangle
drapeau=Affinite(drapeau, 50, 50, 30)
drapeau=Rotation_x_y_z(drapeau, 'y', 90)
drapeau=Rotation_x_y_z(drapeau, 'z', -90)
drapeau=Translation(drapeau, -785, -1215, 300)
drapeau=Repetition_Rectangulaire(drapeau, 2, 'y', 4900)

#=======================TEEMO=========================
perso=LireSTL('Teemo_nobase.stl')
teemo=perso
teemo=Homotetie(teemo, 22)
teemo=Translation(teemo, 0, 200, 20)
teemo=Rotation_x_y_z(teemo, 'z', 290)

#=======================Ballon=========================
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

#====================Spectateurs=========================
perso1=LireSTL('Camille.stl')
perso2=LireSTL('Fiora.stl')
camille=perso1
fiora=perso2

camille=Homotetie(camille, 18)
camille=Rotation_x_y_z(camille, 'z', -30)
camille=Translation(camille, 1400, 1950,650)
camille=Repetition_Rectangulaire(camille, 5, 'x', -3000)



fiora=Homotetie(fiora, 4)
fiora=Rotation_x_y_z(fiora, 'z', -30)
fiora=Translation(fiora, -550, 900, 350)
fiora=Repetition_Rectangulaire(fiora,4 , 'x', 2500)


#====================But==========================

but1 = LireSTL('Cylindre.stl')
but1 = Affinite(but1, 1, 1, 15)
but1 = Repetition_Rectangulaire(but1, 2, 'x', 40)
but1 = Repetition_Rectangulaire(but1, 2, 'y', 20)


but2 = LireSTL('Cylindre.stl')
but2 = Affinite(but2, 1, 1, 21)
but2 = Rotation_x_y_z(but2,"y",90)
but2 = Translation(but2,-0.5,0,0)
but3 = Repetition_Rectangulaire(but2, 2, 'z', 29)
but2 = Repetition_Rectangulaire(but2, 2, 'y', 20)


but4 = LireSTL('Cylindre.stl')
but4 = Affinite(but4, 1, 1, 10)
but4 = Rotation_x_y_z(but4,"y",90)
but4 = Rotation_x_y_z(but4,"z",90)
but4 = Repetition_Rectangulaire(but4, 2, 'z', 29)
but4 = Repetition_Rectangulaire(but4, 2, 'x', 40)


but5 = LireSTL('Cylindre.stl')
but5 = Affinite(but5, 0.01, 0.01, 15)
but5 = Repetition_Rectangulaire(but5, 50, 'x', 20)


but6 = LireSTL('Cylindre.stl')
but6 = Affinite(but6, 0.01, 0.01, 20)
but6 = Rotation_x_y_z(but6,"y",90)
but6 = Repetition_Rectangulaire(but6, 35, 'z', 15)


but7 = LireSTL('Cylindre.stl')
but7 = Affinite(but7, 0.01, 0.01, 15)
but7 = Repetition_Rectangulaire(but7, 25, 'y', 10)


but8 = LireSTL('Cylindre.stl')
but8 = Affinite(but8, 0.01, 0.01, 10)
but8 = Rotation_x_y_z(but8,"x",-90)
but8 = Repetition_Rectangulaire(but8, 35, 'z', 15)


but9 = Fusion(but7,but8)
but9 = Translation(but9,20,0,0)


but10 = LireSTL('Cylindre.stl')
but10 = Affinite(but10, 0.01, 0.01, 10)
but10 = Repetition_Rectangulaire(but10, 50, 'x', 20)
but10 = Rotation_x_y_z(but10,"x",-90)


but11 = LireSTL('Cylindre.stl')
but11 = Affinite(but11, 0.01, 0.01, 20)
but11 = Rotation_x_y_z(but11,"y",90)
but11 = Repetition_Rectangulaire(but11, 25, 'z', 10)
but11 = Rotation_x_y_z(but11,"x",-90)


but = Fusion(but1,but2,but3,but4,but5,but6,but7,but8,but9,but10,but11)

but= Homotetie(but, 50)
but=Rotation_x_y_z(but, 'x', 180)
but=Rotation_x_y_z(but, 'z', 90)
but=Translation(but, -1300, -500, 800)




#================Fusion+export======================#

terrain_f=Fusion(terrain,tige,drapeau,teemo,ballon,panneau,estrade,fiora,camille,but)




nom_fichier='Scene_69.stl'


fj=terrain_f[0]
vj=terrain_f[1]
nj=terrain_f[2]

EcrireSTLASCII(nom_fichier,fj,vj,nj)
