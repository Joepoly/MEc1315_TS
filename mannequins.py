#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 13:45:09 2022

@author: markomilovic
"""

import numpy as np
from Fonctions import *
from MEC1315_STL import *




man1 = LireSTL('Cylindre.stl')
man1 = Affinite(man1, 1, 1, 10)
man1 = Repetition_Rectangulaire(man1, 3, 'x', 6)


man2 = LireSTL('Cube.stl')
man2 = Affinite(man2, 1, 1, 5)
man2 = Rotation_x_y_z(man2,"y",90)
man2 = Translation(man2,-0.5,-0.5,0)
man2 = Repetition_Rectangulaire(man2, 2, 'z', 20)

man3 = LireSTL('icosahedron.stl')
man3 = Rotation_x_y_z(man3,"z",45)
man3 = Affinite(man3, 4, 1, 4)
man3 = Translation(man3,2,0,-5)


man = Fusion(man1,man2,man3)
man = Repetition_Rectangulaire(man, 3, 'x', 20)



f,v,n = man[0], man[1], man[2]
nom_fichier = 'man.stl'
EcrireSTLASCII(nom_fichier, f, v, n)
