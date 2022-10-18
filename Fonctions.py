import numpy as np
from MEC1315_STL import *


def Translation(objet,x,y,z):
    f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
    v=v+np.array([x,y,z])
    return f,v,n

def Homotetie(objet,facteur):
    f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
    v=v*facteur
    return f,v,n

def Rotation_x_y_z(objet,axe,angle):
    f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
    rad=np.radians(angle)
    if axe =='x':
        v=np.dot(v,Rx(rad))
        n=np.dot(n,Rx(rad))

    elif axe =='y':
        v=np.dot(v, Ry(rad))
        n=np.dot(n, Ry(rad))
        
    elif axe =='z':
        v=np.dot(v, Rz(rad))
        n=np.dot(n, Rz(rad))

    return f,v,n
    
def Affinite (objet,facteur_x,facteur_y,facteur_z):
    f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
    v[:,0]=v[:,0]*facteur_x
    v[:,1]=v[:,1]*facteur_y
    v[:,2]=v[:,2]*facteur_z
    n=CalculNormal(f,v)
    return f,v,n    
    
def Centre_Sur_Axe(objet,axe): 
    f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
    if axe =='x':
        x_min=min(v[:,0])
        v=v-np.array([x_min,0,0])
        return f,n,v
    
    elif axe == 'y':
        y_min=min(v[:,1])
        v=v-np.array([0,y_min,0])
        return f,n,v
    
    elif axe =='z':
        z_min=min(v[:,2])
        v=v-np.array([0,0,z_min])
        return f,n,v

def Centre_000(objet):
    f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
    x_centre= (max(v[:,0])-min(v[:,0]))/2
    y_centre= (max(v[:,1])-min(v[:,1]))/2
    z_centre= (max(v[:,2])-min(v[:,2]))/2
    v=v - np.array([x_centre,y_centre,z_centre])
    return f,v,n
    
    
def Fusion(*args): 
    F,V,N = [],[],[]
    nv = 0
    for i in range(len(args)):
        F.append(args[i][0] + nv)
        V.append(args[i][1])
        N.append(args[i][2])
        nv= nv+ len(V[i])
        f = np.vstack(F)
        v = np.vstack(V)
        n = np.vstack(N)
    return f,v,n


def Repetition_Circulaire(objet,nb_repetition,axe_rotation,rayon,angle_total):
    objet = Translation(objet, rayon[0], rayon[1], rayon[2])
    liste_objets = []
    angle= angle_total/nb_repetition
    for i in range (nb_repetition): 
        objet = Rotation_x_y_z(objet, axe_rotation, angle)
        liste_objets.append(objet)
    return Fusion(*liste_objets)
        
def Repetition_Rectangulaire(objet, nb_repetition, distance):
    offset_x, offset_y, offset_z = 0,0,0
    liste_objets = []
    for i in range (nb_repetition+1):
        objet = Translation(objet, offset_x, offset_y, offset_z)
        offset_x, offset_y, offset_z = distance[0]/nb_repetition, distance[1]/nb_repetition, distance[2]/nb_repetition
        liste_objets.append(objet)
    return Fusion(*liste_objets)
        
        
