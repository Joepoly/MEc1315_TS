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
tige = Affinite(tige, 30, 30, 600)
tige = Translation(tige, -800, -1230, 0)
tige = Repetition_Rectangulaire(tige, 1, [0,2450,0])

drapeau = LireSTL('Triangle.stl')
drapeau = Affinite(drapeau, 100, 100, 60)
drapeau = Rotation_x_y_z(drapeau, 'y', 90)
drapeau = Rotation_x_y_z(drapeau, 'z', -90)
drapeau = Translation(drapeau, -785, -1215, 600)
drapeau = Repetition_Rectangulaire(drapeau, 1, [0,2450,0])


#=======================Random=========================
z_ballon = np.random.randint(-350,0)
nbr_ballon = 0
angle_ballon = 0
y_teemo, z_teemo = 0,0
a_marque = True

if z_ballon <= -200 :
    nbr_ballon = 5
    angle_ballon = -47.5
    z_teemo = -50
    y_teemo = 700
    a_marque = False
    
else:
    nbr_ballon = 10
    angle_ballon = -100
    z_teemo = 100
    y_teemo = 750

#=========================Teemo==========================
teemo = LireSTL('Teemo_nobase.stl')
teemo = Homotetie(teemo, 22)
teemo = Translation(teemo, 0, y_teemo, z_teemo)
teemo = Rotation_x_y_z(teemo, 'z', -90)
teemo = Rotation_x_y_z(teemo, 'y', -20)

#=======================Ballon=========================

ballon = LireSTL('icosahedron.stl')
ballon = Homotetie(ballon, 100)
ballon = Translation(ballon, 200, 0, 900)
ballon = Repetition_Circulaire(ballon, nbr_ballon, 'y', [200,0,0], angle_ballon)
ballon = Translation(ballon, 0, 0, z_ballon)

#=======================Lumieres=========================
panneau1 = LireSTL('Cylindre.stl')
panneau1 = Affinite(panneau1, 100, 100, 1500)
panneau1 = Translation(panneau1, -1400, -1400, 0)
panneau2 = LireSTL('Cube.stl')
panneau2 = Affinite(panneau2, 100, 600, 400)
panneau2 = Centre_000(panneau2)
panneau2 = Translation(panneau2, -1400, -1400, 1500)
lumieres = LireSTL('icosahedron.stl')
lumieres = Homotetie(lumieres, 100)
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
estradeBanc= Affinite(estradeBanc, 3000, 1000/6, 1000/6)
estradeBanc = Translation(estradeBanc, -1500, 1500, 1000/6)
estradeBanc = Repetition_Rectangulaire(estradeBanc, 5, [0,1000-(1000/6),1000-(1000/6)])


barriereV= LireSTL('Cylindre.stl')
barriereV=Affinite(barriereV,30,30,(1000/6)-15)
barriereH=Rotation_x_y_z(barriereV,'x',-90)
barriereH=Translation(barriereH,0,-15,(1000/6)-30)
barriere=Fusion(barriereH,barriereV)
barriere=Translation(barriere,-1470,1530,1000/6)
barriere=Repetition_Rectangulaire(barriere, 4, [0,1000-(2000/6),1000-(2000/6)] )

barriere=Repetition_Rectangulaire(barriere, 1, [2900,0,0] )


estrade = Fusion(estradeTriangle,estradeBanc,barriere)

#========================Spectateurs==============================
corps = LireSTL('Cylindre.stl')
corps = Affinite(corps, 0.75, 0.75, 1)

tete = LireSTL('icosahedron.stl')
tete = Translation(tete, 0, 0, 1)

chaise1 = LireSTL('Cube.stl')
chaise1 = Affinite(chaise1, 1.5, 1.5, 0.1)
chaise1 = Centre_000(chaise1)
chaise2 = Rotation_x_y_z(chaise1, 'y', -90)
chaise2 = Translation(chaise2, 0.75, 0, 0.75)
chaise = Fusion(chaise1,chaise2)

bras = LireSTL('Cylindre.stl')
bras = Rotation_x_y_z(bras, 'x', 90)
bras = Affinite(bras, 0.25, 1, 0.25)
bras = Translation(bras, 0, 0, 0.5)
bras = Repetition_Rectangulaire(bras, 1, [0,1,0])

jambes = LireSTL('Cylindre.stl')
jambes = Rotation_x_y_z(jambes, 'y', 90)
jambes = Affinite(jambes, 1, 0.25, 0.25)
jambes = Translation(jambes, -1, 0.25, 0.1)
jambes = Repetition_Rectangulaire(jambes, 1, [0,-0.5,0])

bonhomme = Fusion(corps,tete,chaise,bras,jambes)
bonhomme = Homotetie(bonhomme, 100)

bonhomme=Rotation_x_y_z(bonhomme, 'z', 90)
bonhomme=Translation(bonhomme,-1350,1580,(1000/6)+10)
bonhomme=Repetition_Rectangulaire(bonhomme,  4, [0,1000-(2000/6),1000-(2000/6)])
bonhomme=Repetition_Rectangulaire(bonhomme, 9,[2650,0,0] )



#=========================Joueurs==============================
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
but1 = Affinite(but1, 50, 50, 750)
but1 = Repetition_Rectangulaire(but1, 1, [1000,0,0])

but2 = LireSTL('Cylindre.stl')
but2 = Affinite(but2, 50, 50, 1000)
but2 = Rotation_x_y_z(but2, 'y', 90)
but2 = Translation(but2, 0, 0, 25)
but2 = Repetition_Rectangulaire(but2, 1, [0,0,700])

but3 = LireSTL('Cylindre.stl')
but3 = Affinite(but3, 0.5, 0.5, 750)
but3 = Repetition_Rectangulaire(but3, 50, [1000,0,0])

but4 = LireSTL('Cylindre.stl')
but4 = Affinite(but4, 0.5, 0.5, 1000)
but4 = Rotation_x_y_z(but4, 'y', 90)
but4 = Repetition_Rectangulaire(but4, 40, [0,0,750])

face_but1 = Fusion(but1,but2,but3,but4)
face_but1 = Rotation_x_y_z(face_but1, 'y', -90)

face_but2 = Rotation_x_y_z(face_but1, 'x', 90)
face_but2 = Translation(face_but2, 0, 1000, 1000)
face_but2 = Affinite(face_but2, 1, 1.5, 1)

face_but3 = Rotation_x_y_z(face_but2, 'y', 90)
face_but3 = Translation(face_but3, -1025, 0, 0)
face_but3 = Affinite(face_but3, 1, 1, 1000/750)

face_but1 = Repetition_Rectangulaire(face_but1, 1, [0,1500,0])


but = Fusion(face_but1,face_but2,face_but3)
but = Homotetie(but, 0.8)
but = Rotation_x_y_z(but, 'z', 180)
but = Translation(but, -1350, 650, 30)

#====================Mannequins==========================
man1 = LireSTL('Cylindre.stl')
man1 = Affinite(man1, 1, 1, 10)
man1 = Repetition_Rectangulaire(man1, 2, [4,0,0])

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
man = Translation(man,-500,-500,450)

#====================Gazon==========================

gazon1 = LireSTL('icosahedron.stl')
gazon1 = Affinite (gazon1,20,1,30)
gazon1 = Rotation_x_y_z(gazon1, "x", 45)
gazon1 = Repetition_Rectangulaire(gazon1, 15, [500,0,0])
gazon1 = Repetition_Rectangulaire(gazon1, 100, [0,2990,0])
gazon1 = Translation(gazon1,0,10,0)

gazon2 = LireSTL('icosahedron.stl')
gazon2 = Affinite (gazon2,20,1,30)
gazon2 = Rotation_x_y_z(gazon2, "x", -45)
gazon2 = Repetition_Rectangulaire(gazon2, 15, [500,0,0])
gazon2 = Repetition_Rectangulaire(gazon2, 100, [0,2990,0])
gazon2 = Translation(gazon2,500,-10,0)

gazon3 = Fusion(gazon1,gazon2)
gazon3 = Repetition_Rectangulaire(gazon3, 2, [2000,0,0])

gazon = Fusion(gazon1,gazon2,gazon3)
gazon = Translation(gazon,-1500,-1500,20)

#====================Cone==========================

cone1= LireSTL('Triangle.stl')
cone1 = Affinite(cone1,200,70,1)
cone1 = Rotation_x_y_z(cone1, "y", -90)
cone1 = Repetition_Circulaire(cone1, 360, "z", [0,0,0], 360)

cone2 = LireSTL('Cube.stl')
cone2 = Affinite(cone2,150,150,30)
cone2 = Centre_000(cone2)
cone2 = Translation(cone2, 0, 0, 15)

cone3 = Fusion(cone1,cone2)
cone4 = Repetition_Rectangulaire(cone3, 4, [-2000,0,0])
cone5 = Repetition_Rectangulaire(cone3, 4, [0,2500,0])

cone = Fusion (cone4,cone5)
cone = Translation(cone,1350,-1350,20)

#====================Feux d'artifice==========================

boite = LireSTL('Cube.stl')
boite = Affinite(boite, 100, 100, 300)
boite = Centre_000(boite)
boite = Translation(boite, 0,0,150)

    
if a_marque:
    feu = LireSTL('Cylindre.stl')
    feu = Affinite(feu, 10, 10, 800)
    feu = Rotation_x_y_z(feu, "x", 30)
    feu = Repetition_Circulaire(feu, 10, "z", [40,0,0], 360)
    feu = Translation(feu, 0,0,300)
    fire = Fusion(boite,feu)

else:
    fire = boite

fire = Translation(fire, -1400,-900,0)
fire = Repetition_Rectangulaire(fire, 1, [0,1900,0])
#================Fusion+export======================#
 
terrain_f=Fusion(terrain,tige,drapeau,teemo,ballon,panneau,estrade, bonhomme, but, camille, fiora, man, gazon, cone,fire)




nom_fichier='Scene_69.stl'


fj=terrain_f[0]
vj=terrain_f[1]
nj=terrain_f[2]

EcrireSTLASCII(nom_fichier,fj,vj,nj)
