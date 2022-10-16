# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:57:47 2022

@author: joela
"""

import numpy as np
from MEC1315_STL import *
from Fonctions import *
import random 




#====================Terrain de soccer=========================#
cube=LireSTL('Cube.stl')

terrain = cube
terrain = Affinite(terrain, 2500, 2500, 20)
terrain = Centre_000(terrain)
terrain = Translation(terrain, 0, 0, 10)
#=======================Drapeaux de coin=========================#
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
teemo=Homotetie(teemo, 12)
teemo=Translation(teemo, 0, 200, 20)
teemo=Rotation_x_y_z(teemo, 'z', 290)

#=======================Ballon=========================#
ico=LireSTL('icosahedron.stl')
ballon=ico
ballon=Homotetie(ballon, 60)
ballon=Translation(ballon, -120, -300, 20)
ballon=Repetition_Circulaire(ballon,random.randint(1, 10) , 'z', -10, 20,0)




#================Fusion+export======================#

terrain_f=Fusion(terrain,tige,drapeau,teemo,ballon)




nom_fichier='terrain_joel.stl'


fj=terrain_f[0]
vj=terrain_f[1]
nj=terrain_f[2]

EcrireSTLASCII(nom_fichier,fj,vj,nj)
