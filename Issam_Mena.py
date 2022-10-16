import numpy as np
from Fonctions import *
from MEC1315_STL import *

panneau1 = LireSTL('Cylindre.stl')
panneau1 = Rotation_x_y_z(panneau1, 'x', -90)
panneau1 = Affinite(panneau1, 1, 10, 1)

panneau2 = LireSTL('Cube.stl')
panneau2 = Affinite(panneau2, 1, 4, 6)
panneau2 = Centre_000(panneau2)
panneau2 = Translation(panneau2, 0, 10, 0)

lumieres = LireSTL('icosahedron.stl')
lumieres = Repetition_Rectangulaire(lumieres, 3, 'z', 6)
lumieres = Repetition_Rectangulaire(lumieres, 2, 'y', 4)
lumieres = Centre_000(lumieres)
lumieres = Translation(lumieres, 0, 10.5, 0)

panneau = Fusion(panneau1, panneau2, lumieres)
panneau = Repetition_Rectangulaire(panneau, 2, 'z', 50)

estradeTriangle= LireSTL('Triangle.stl')
estradeTriangle = Rotation_x_y_z(estradeTriangle, 'y', 90)
estradeTriangle = Affinite(estradeTriangle, 50, 10, 10)
estradeTriangle = Translation(estradeTriangle, -50, 0, 50)

estradeBanc1= LireSTL('Triangle.stl')

estradeBanc1 = Rotation_x_y_z(estradeBanc1, 'y', 90)
estradeBanc1 = Rotation_x_y_z(estradeBanc1, 'x', 180)
estradeBanc1= Affinite(estradeBanc1, 50, 3, 3)
estradeBanc1 = Translation(estradeBanc1, -50, 3, 40)

estradeBanc2= LireSTL('Triangle.stl')

estradeBanc2 = Rotation_x_y_z(estradeBanc2, 'y', 90)
estradeBanc2= Rotation_x_y_z(estradeBanc2, 'x', 180)
estradeBanc2= Affinite(estradeBanc2, 50, 3, 3)
estradeBanc2= Translation(estradeBanc2, -50, 6, 43)

estradeBanc3= LireSTL('Triangle.stl')

estradeBanc3 = Rotation_x_y_z(estradeBanc3, 'y', 90)
estradeBanc3 = Rotation_x_y_z(estradeBanc3, 'x', 180)
estradeBanc3= Affinite(estradeBanc3, 50, 3, 3)
estradeBanc3 = Translation(estradeBanc3, -50, 9, 46)




#estradeBanc = Repetition_Rectangulaire(estradeBanc, 3, 'y', -10)
#estradeBanc = Repetition_Rectangulaire(estradeBanc, 3, 'z', -10)




scene = Fusion(panneau,estradeTriangle,estradeBanc1,estradeBanc2,estradeBanc3)
f,v,n = scene[0], scene[1], scene[2]
nom_fichier = 'mena_issam.stl'
EcrireSTLASCII(nom_fichier, f, v, n)