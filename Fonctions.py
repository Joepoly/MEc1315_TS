import numpy as np
from MEC1315_STL import *


def Translation(objet,x,y,z):
    #Initialisation de f,v,n pour l'objet
    f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
    
    #Translation de l'objet
    v=v+np.array([x,y,z])
    
    #Retourne le nouvel objet
    return f,v,n

def Homotetie(objet,facteur):
    #Initialisation de f,v,n pour l'objet
    f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
    
    #Homotétie de l'objet
    v=v*facteur
    
    #Retourne le nouvel objet
    return f,v,n

def Rotation_x_y_z(objet,axe,angle):
    #Initialisation de f,v,n pour l'objet
    f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
    
    #Transformation de l'angle en radians
    rad=np.radians(angle)
    
    #Rotation de l'objet par rapport à l'axe X
    if axe =='x':
        v=np.dot(v,Rx(rad))
        n=np.dot(n,Rx(rad))

    #Rotation de l'objet par rapport à l'axe Y
    elif axe =='y':
        v=np.dot(v, Ry(rad))
        n=np.dot(n, Ry(rad))
        
    #Rotation de l'objet par rapport à l'axe Z
    elif axe =='z':
        v=np.dot(v, Rz(rad))
        n=np.dot(n, Rz(rad))

    #Retourne le nouvel objet
    return f,v,n
    
def Affinite (objet,facteur_x,facteur_y,facteur_z):
    #Initialisation de f,v,n pour l'objet
    f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
    
    #Affinité de l'objet selon l'axe des X
    v[:,0]=v[:,0]*facteur_x
    #Affinité de l'objet selon l'axe des Y
    v[:,1]=v[:,1]*facteur_y
    #Affinité de l'objet selon l'axe des Z
    v[:,2]=v[:,2]*facteur_z
    
    #Calcul de la nouvelle normale de l'objet
    n=CalculNormal(f,v)
    
    #Retourne le nouvel objet
    return f,v,n    
    
def Centre_Sur_Axe(objet,axe): 
    #Initialisation de f,v,n pour l'objet
    f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
    
    #Centrer sur l'axe des X
    if axe =='x':
        x_min=min(v[:,0])
        v=v-np.array([x_min,0,0])
    
    #Centrer sur l'axe des Y
    elif axe == 'y':
        y_min=min(v[:,1])
        v=v-np.array([0,y_min,0])

    #Centrer sur l'axe des Z
    elif axe =='z':
        z_min=min(v[:,2])
        v=v-np.array([0,0,z_min])
    
    #Retourne le nouvel objet
    return f,n,v

def Centre_000(objet):
    #Initialisation de f,v,n pour l'objet
    f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
    
    #Centrer sur X = 0
    x_centre= (max(v[:,0])-min(v[:,0]))/2
    #Centrer sur Y = 0
    y_centre= (max(v[:,1])-min(v[:,1]))/2
    #Centrer sur Z = 0
    z_centre= (max(v[:,2])-min(v[:,2]))/2
    
    #Translation de l'objet jusqu'au point 0,0,0
    objet = Translation(objet, -x_centre, -y_centre, -z_centre)
    
    #Retourne le nouvel objet
    return objet
    
    
def Fusion(*args): 
    #Création de trois listes vides pour stocker f,v,n des objets à fusionner
    F,V,N = [],[],[]
    
    #Décalage pour les faces
    nv = 0
    
    #Ajout des objets à fusionner dans F,V,N
    for i in range(len(args)):
        F.append(args[i][0] + nv) #Ajout du décalage pour les faces
        V.append(args[i][1])
        N.append(args[i][2])
        #Décalage du nombre de faces de l'objet précédent
        nv= nv+ len(V[i])
        
        #Création du nouvel objet avec la fusion
        f = np.vstack(F)
        v = np.vstack(V)
        n = np.vstack(N)
        
    ##Retourne le nouvel objet fusionné
    return f,v,n


def Repetition_Circulaire(objet,nb_repetition,axe_rotation,rayon,angle_total):
    #Translation de l'objet du rayon en x,y,z souhaité
    objet = Translation(objet, rayon[0], rayon[1], rayon[2])
    #Création d'une liste vide pour stocker les objets
    liste_objets = []
    #Angle pour chaque répétition -> angle_total : Angle sur lequel la rotation sera faite
    angle= angle_total/nb_repetition
    
    for i in range (nb_repetition):
        #Rotation de l'objet selon l'axe demandé
        objet = Rotation_x_y_z(objet, axe_rotation, angle)
        #Ajout de l'objet dans la liste
        liste_objets.append(objet)
    #Retour de la Fusion de tous les éléments de la liste d'objets
    return Fusion(*liste_objets)
        
def Repetition_Rectangulaire(objet, nb_repetition, distance):
    #Initialisation des offsets en X Y Z
    offset_x, offset_y, offset_z = distance[0]/nb_repetition, distance[1]/nb_repetition, distance[2]/nb_repetition
    #Création d'une liste d'objets vides contenant l'objet de base
    liste_objets = [objet]
    
    for i in range (nb_repetition):
        #Translation de l'objet de X Y Z par les offsets
        objet = Translation(objet, offset_x, offset_y, offset_z)
        #Ajout de l'objet dans la liste d'objets
        liste_objets.append(objet)
    #Retour de la Fusion de tous les éléments de la liste d'objets
    return Fusion(*liste_objets)
        
        
