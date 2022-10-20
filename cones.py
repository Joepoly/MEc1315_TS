#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 20:03:18 2022

@author: markomilovic
"""
import numpy as np
from MEC1315_STL import *
from Fonctions import *


cone1= LireSTL('Triangle.stl')
cone1 = Affinite(cone1,200,70,1)
cone1 = Rotation_x_y_z(cone1, "y", -90)
cone1 = Repetition_Circulaire(cone1, 360, "z", [0,0,0], 360)

cone2 = LireSTL('Cube.stl')
cone2 = Affinite(cone2,200,200,10)
cone2 = Centre_000(cone2)

cone3 = Fusion(cone1,cone2)
cone4 = Repetition_Rectangulaire(cone3, 4, [-2000,0,0])
cone5 = Repetition_Rectangulaire(cone3, 4, [0,2500,0])

cone = Fusion (cone3,cone4,cone5)
cone = Translation(cone,1350,-1350,20)

f,v,n = cone[0], cone[1], cone[2]
nom_fichier = 'cone.stl'
EcrireSTLASCII(nom_fichier, f, v, n)