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
    if axe =='x':
        f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
        rad=np.radians(angle)
        v=np.dot(v,Rx(rad))
        n=np.dot(n,Rx(rad))
    
    elif axe =='y':
        f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
        rad=np.radians(angle)
        v=np.dot(v, Ry(rad))
        n=np.dot(n, Ry(rad))
        
    elif axe =='z':
        f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
        rad=np.radians(angle)
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
    if axe =='x':
        f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
        x_min=min(v[:,0])
        v=v-np.array([x_min,0,0])
        return f,n,v
    
    elif axe == 'y':
        f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
        y_min=min(v[:,1])
        v=v-np.array([0,y_min,0])
        return f,n,v
    
    elif axe =='z':
        f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
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


def Repetition_Circulaire(objet,nb_repetition,axe_rotation,offset_x,offset_y,offset_z,coefficient_pi):
    objet = Translation(objet, offset_x, offset_y, offset_z)
    f1,v1,n1=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
    liste_objets = []
    nv=len(v1)
    angle= coefficient_pi*np.pi/nb_repetition
    f,v,n = np.empty([0,3]), np.empty([0,3]), np.empty([0,3])
    for i in range (nb_repetition): 
        if axe_rotation=='x':
            stack = nv*i
            f=np.vstack((f,f1+stack))
            v=np.vstack((v,np.dot(v1,Rx(i*angle))))
            n=np.vstack((n,np.dot(n1,Rx(i*angle))))
        elif axe_rotation=='y':        
            stack = nv*i
            f=np.vstack((f,f1+stack))
            v=np.vstack((v,np.dot(v1,Ry(i*angle))))
            n=np.vstack((n,n1))
        elif axe_rotation=='z':
            stack = nv*i
            f=np.vstack((f,f1+stack))
            v=np.vstack((v,np.dot(v1,Rz(i*angle))))
            n=np.vstack((n,np.dot(n1,Rz(i*angle))))
    return f,v,n
        
def Repetition_Rectangulaire(objet,nb_repetition,axe_repetition,distance):
    offset = 0
    liste_objets = []
    for i in range (nb_repetition):
        if axe_repetition == 'x':
            objet = Translation(objet, offset, 0, 0)
            offset = distance/nb_repetition
            liste_objets.append(objet)   
        elif axe_repetition == 'y':
            objet = Translation(objet, 0, offset, 0)
            offset = distance/nb_repetition
            liste_objets.append(objet)
        elif axe_repetition == 'z':
            objet = Translation(objet, 0, 0, offset)
            offset = distance/nb_repetition
            liste_objets.append(objet)
    return Fusion(*liste_objets)
        
        
