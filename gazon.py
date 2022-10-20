#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 19:09:21 2022

@author: markomilovic
"""

import numpy as np
from MEC1315_STL import *
from Fonctions import *

gazon1 = LireSTL('icosahedron.stl')
gazon1 = Affinite (gazon1,20,0,30)
gazon1 = Rotation_x_y_z(gazon1, "x", 45)
gazon1 = Repetition_Rectangulaire(gazon1, 15, [500,0,0])
gazon1 = Repetition_Rectangulaire(gazon1, 100, [0,2990,0])
gazon1 = Translation(gazon1,0,10,0)

gazon2 = LireSTL('icosahedron.stl')
gazon2 = Affinite (gazon2,20,0,30)
gazon2 = Rotation_x_y_z(gazon2, "x", -45)
gazon2 = Repetition_Rectangulaire(gazon2, 15, [500,0,0])
gazon2 = Repetition_Rectangulaire(gazon2, 100, [0,2990,0])
gazon2 = Translation(gazon2,500,-10,0)

gazon3 = Fusion(gazon1,gazon2)
gazon3 = Repetition_Rectangulaire(gazon3, 2, [2000,0,0])

gazon = Fusion(gazon1,gazon2,gazon3)
gazon = Translation(gazon,-1500,-1500,20)

f,v,n = gazon[0], gazon[1], gazon[2]
nom_fichier = 'gazon.stl'
EcrireSTLASCII(nom_fichier, f, v, n)