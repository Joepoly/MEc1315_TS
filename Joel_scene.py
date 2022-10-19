# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:57:47 2022

@author: joela
"""

import numpy as np
from MEC1315_STL import *
from Fonctions import *




#====================Terrain de soccer=========================
terrain = LireSTL('Cube.stl')
terrain = Affinite(terrain, 3000, 3000, 20)
terrain = Centre_000(terrain)
terrain = Translation(terrain, 0, 0, 10)

#=======================Drapeaux de coin======================
tige = LireSTL('Cylindre.stl')
tige = Affinite(tige, 30, 30, 300)
tige = Translation(tige, -800, -1230, 0)
tige = Repetition_Rectangulaire(tige, 1, [0,2450,0])

drapeau = LireSTL('Triangle.stl')
drapeau = Affinite(drapeau, 50, 50, 30)
drapeau = Rotation_x_y_z(drapeau, 'y', 90)
drapeau = Rotation_x_y_z(drapeau, 'z', -90)
drapeau = Translation(drapeau, -785, -1215, 300)
drapeau = Repetition_Rectangulaire(drapeau, 1, [0,2450,0])

#=======================TEEMO=========================
teemo = LireSTL('Teemo_nobase.stl')
teemo = Homotetie(teemo, 22)
teemo = Translation(teemo, 200, 700, 100)
teemo = Rotation_x_y_z(teemo, 'z', 290)
teemo = Rotation_x_y_z(teemo, 'y', -20)

#=======================Ballon=========================
ballon = LireSTL('icosahedron.stl')
ballon = Homotetie(ballon, 100)
ballon = Translation(ballon, -1000, 0, 0)
ballon = Repetition_Circulaire(ballon, 9, 'y', [20,0,100], 110)
ballon = Rotation_x_y_z(ballon, 'z', np.random.randint(-25,25))

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
lumieres = Repetition_Rectangulaire(lumieres, 2, [0,450,0])
lumieres = Repetition_Rectangulaire(lumieres, 1, [0,0,200])
lumieres = Centre_000(lumieres)
lumieres = Translation(lumieres, -1250, -1350, 1500)

panneau = Fusion(panneau1, panneau2, lumieres)
panneau = Repetition_Rectangulaire(panneau, 1, [0,2800,0])

#===========================Estrades============================
estradeTriangle= LireSTL('Triangle.stl')
estradeTriangle = Rotation_x_y_z(estradeTriangle, 'y', -90)
estradeTriangle = Rotation_x_y_z(estradeTriangle, 'z', 180)
estradeTriangle = Affinite(estradeTriangle, 3000, 1000, 1000)
estradeTriangle = Translation(estradeTriangle, -1500, 2500, 0)
estradeBanc= LireSTL('Triangle.stl')
estradeBanc = Rotation_x_y_z(estradeBanc, 'y', 90)
estradeBanc= Affinite(estradeBanc, 3000, 333, 333)
estradeBanc = Translation(estradeBanc, -1500, 1500, 333)
estradeBanc = Repetition_Rectangulaire(estradeBanc, 3, [0,666,666])

estrade = Fusion(estradeTriangle,estradeBanc)

#====================Joueurs=========================
camille=LireSTL('Camille.stl')

camille=Homotetie(camille, 22)
camille=Rotation_x_y_z(camille, 'z', -30)
camille=Translation(camille, 0, -1350,0)
camille=Translation(camille, np.random.randint(0,1200), np.random.randint(0,700), 0)

fiora=LireSTL('Fiora.stl')
fiora=Homotetie(fiora, 5)
fiora=Rotation_x_y_z(fiora, 'z', -30)
fiora=Translation(fiora, 400, 300, 50)
fiora=Translation(fiora, np.random.randint(0,1000), np.random.randint(-500,0), 0)

#====================But==========================

but1 = LireSTL('Cylindre.stl')
but1 = Affinite(but1, 1, 1, 15)
but1 = Repetition_Rectangulaire(but1, 1, [20,0,0])
but1 = Repetition_Rectangulaire(but1, 1, [0,10,0])


but2 = LireSTL('Cylindre.stl')
but2 = Affinite(but2, 1, 1, 21)
but2 = Rotation_x_y_z(but2,"y",90)
but2 = Translation(but2,-0.5,0,0)
but3 = Repetition_Rectangulaire(but2, 1, [0,0,14.5])
but2 = Repetition_Rectangulaire(but2, 1, [0,10,0])


but4 = LireSTL('Cylindre.stl')
but4 = Affinite(but4, 1, 1, 10)
but4 = Rotation_x_y_z(but4,"y",90)
but4 = Rotation_x_y_z(but4,"z",90)
but4 = Repetition_Rectangulaire(but4, 1, [0,0,14.5])
but4 = Repetition_Rectangulaire(but4, 1, [20,0,0])


but5 = LireSTL('Cylindre.stl')
but5 = Affinite(but5, 0.01, 0.01, 15)
but5 = Repetition_Rectangulaire(but5, 50, [20,0,0])


but6 = LireSTL('Cylindre.stl')
but6 = Affinite(but6, 0.01, 0.01, 20)
but6 = Rotation_x_y_z(but6,"y",90)
but6 = Repetition_Rectangulaire(but6, 35, [0,0,15])


but7 = LireSTL('Cylindre.stl')
but7 = Affinite(but7, 0.01, 0.01, 15)
but7 = Repetition_Rectangulaire(but7, 25, [0,10,0])


but8 = LireSTL('Cylindre.stl')
but8 = Affinite(but8, 0.01, 0.01, 10)
but8 = Rotation_x_y_z(but8,"x",-90)
but8 = Repetition_Rectangulaire(but8, 35, [0,0,15])


but9 = Fusion(but7,but8)
but9 = Translation(but9,20,0,0)


but10 = LireSTL('Cylindre.stl')
but10 = Affinite(but10, 0.01, 0.01, 10)
but10 = Repetition_Rectangulaire(but10, 50, [20,0,0])
but10 = Rotation_x_y_z(but10,"x",-90)


but11 = LireSTL('Cylindre.stl')
but11 = Affinite(but11, 0.01, 0.01, 20)
but11 = Rotation_x_y_z(but11,"y",90)
but11 = Repetition_Rectangulaire(but11, 25, [0,0,10])
but11 = Rotation_x_y_z(but11,"x",-90)


but = Fusion(but1,but2,but3,but4,but5,but6,but7,but8,but9,but10,but11)

but= Homotetie(but, 50)
but=Rotation_x_y_z(but, 'x', 180)
but=Rotation_x_y_z(but, 'z', 90)
but=Translation(but, -1300, -500, 800)

#====================Mannequins==========================
man1 = LireSTL('Cylindre.stl')
man1 = Affinite(man1, 1, 1, 10)
man1 = Repetition_Rectangulaire(man1, 2, [6,0,0])


man2 = LireSTL('Cube.stl')
man2 = Affinite(man2, 1, 1, 5)
man2 = Rotation_x_y_z(man2,"y",90)
man2 = Translation(man2,-0.5,-0.5,0)
man2 = Repetition_Rectangulaire(man2, 1, [0,0,10])

man3 = LireSTL('icosahedron.stl')
man3 = Rotation_x_y_z(man3,"z",45)
man3 = Affinite(man3, 4, 1, 4)
man3 = Translation(man3,2,0,-5)


man = Fusion(man1,man2,man3)
man = Repetition_Rectangulaire(man, 2, [20,0,0])
man = Affinite(man, 44, 44, 44)
man = Rotation_x_y_z(man,"x",180)
man = Rotation_x_y_z(man,"z",90)
man = Translation(man,-200,-350,450)


#================Fusion+export======================#
 
terrain_f=Fusion(terrain,tige,drapeau,teemo,ballon,panneau,estrade,but, camille, fiora, man)




nom_fichier='Scene_69.stl'


fj=terrain_f[0]
vj=terrain_f[1]
nj=terrain_f[2]

EcrireSTLASCII(nom_fichier,fj,vj,nj)
