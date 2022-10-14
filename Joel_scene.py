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
terrain = affinite(terrain, 2500, 2500, 20)
terrain = centre_000(terrain)
terrain = translation(terrain, 0, 0, 10)
#=======================Drapeaux de coin=========================#
triangle =LireSTL('Triangle.stl')
cylindre =LireSTL('Cylindre.stl')

tige=cylindre
tige=affinite(tige, 30, 30, 300)
tige=translation(tige, -1230, -1230, 0)
tige=repetition_rectangulaire(tige, 1, 'y', 2450)

drapeau=triangle
drapeau=affinite(drapeau, 50, 50, 30)
drapeau=rotation_x_y_z(drapeau, 'y', 90)
drapeau=rotation_x_y_z(drapeau, 'z', -90)
drapeau=translation(drapeau, -1215, -1215, 300)
drapeau=repetition_rectangulaire(drapeau, 1, 'y', 2450)

#=======================TEEMO=========================#
perso=LireSTL('Teemo_nobase.stl')
teemo=perso
teemo=homotetie(teemo, 12)
teemo=translation(teemo, 0, 200, 20)
teemo=rotation_x_y_z(teemo, 'z', 290)

#=======================Ballon=========================#
ico=LireSTL('icosahedron.stl')
ballon=ico
ballon=homotetie(ballon, 60)
ballon=translation(ballon, -120, -300, 20)
ballon=repetition_circulaire(ballon,random.randint(1, 10) , 'z', -10, -1)




#================Fusion+export======================#

terrain_f=Fusion(terrain,tige,drapeau,teemo,ballon)




nom_fichier='terrain_joel.stl'


fj=terrain_f[0]
vj=terrain_f[1]
nj=terrain_f[2]

EcrireSTLASCII(nom_fichier,fj,vj,nj)
