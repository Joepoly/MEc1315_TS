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





scene = Fusion(panneau)
f,v,n = scene[0], scene[1], scene[2]
nom_fichier = 'mena_issam.stl'
EcrireSTLASCII(nom_fichier, f, v, n)