#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:00:20 2022

@author: markomilovic
"""

import numpy as np
from Fonctions import *
from MEC1315_STL import *


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

but= Homotetie(but, 40)


f,v,n = but[0], but[1], but[2]
nom_fichier = 'but.stl'
EcrireSTLASCII(nom_fichier, f, v, n)