import numpy as np
from MEC1315_STL import *


def translation(objet,x,y,z):
    f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
    v=v+np.array([x,y,z])
    return f,v,n

def homotetie(objet,facteur):
    f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
    v=v*facteur
    return f,v,n

def rotation_x_y_z(objet,axe,angle):
    if axe =='x':
        f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
        rad=np.radians(degre)
        v=np.dot(v,Rx(rad))
        n=np.dot(n,Rx(rad))
        return f,v,n
    
    elif axe =='y':
        f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
        rad=np.radians(degre)
        v=np.dot(v, Ry(rad))
        n=np.dot(n, Ry(rad))
        return f,v,n
    
    elif axe =='z':
        f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
        rad=np.radians(degre)
        v=np.dot(v, Rz(rad))
        n=np.dot(n, Rz(rad))
        return f,v,n
    
def affinite (objet,facteur_x,facteur_y,facteur_z):
    f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
    v[:,0]=v[:,0]*facteur_x
    v[:,1]=v[:,1]*facteur_y
    v[:,2]=v[:,2]*facteur_z
    n=CalculNormal(f,v)
    return f,v,n    
    
def centre_sur_axe(objet,axe): 
    if axe =='x':
        f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
        x_min=min(v[:,0])
        v=v-np.array([x_min,0,0])
        return f,n,v
    
    if axe == 'y':
        f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
        y_min=min(v[:,1])
        v=v-np.array([0,y_min,0])
        return f,n,v
    
    if axe =='z':
        f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
        z_min=min(v[:,2])
        v=v-np.array([0,0,z_min])
        return f,n,v

def centre_000(objet):
    f,v,n=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
    x_centre= (max(v[:,0])-min(v[:,0]))/2
    y_centre= (max(v[:,1])-min(v[:,1]))/2
    z_centre= (max(v[:,2])-min(v[:,2]))/2
    v=v - np.array([x_centre,y_centre,z_centre])
    return f,v,n
    
        
    
def fusion(*args):
    F,V,N=[],[],[]
    nv=0
    
    for i in range(len(args)):
        F.append(args[i][0] + nv)
        V.append(args[i][1])
        N.append(args[i][2])

        nv= nv+len(V[i])
        
        f=np.vstack(F)
        v=np.vstack(V)
        n=np.vstack(N)
        
    return f,v,n


def repetition_circulaire(objet,nb_repetition,axe_rotation,offset):
    f1,v1,n1=np.array(objet[0]),np.array(objet[1]),np.array(objet[2])
    nv=len(v1)
    angle= 2*np.pi/nb_repetition
    
 
    
    if axe_rotation=='x':
        v1[:,0]=v1[:,0]+offset
        v1[:,1]=v1[:,1]+offset
       
        
        f,v,n = np.empty([0,3]), np.empty([0,3]), np.empty([0,3])
        
        for i in range (nb_repetition):
            stack = nv*i
            f=np.vstack((f,f1+stack))
            v=np.vstack((v,np.dot(v1,Rx(i*angle))))
            n=np.vstack((n,np.dot(n1,Rx(i*angle))))
        return f,v,n
        
    elif axe_rotation=='y':
        v1[:,0]=v1[:,0]+offset
        v1[:,1]=v1[:,1]+offset
        
        f,v,n = np.empty([0,3]), np.empty([0,3]), np.empty([0,3])
        
        for i in range (nb_repetition):
            stack = nv*i
            f=np.vstack((f,f1+stack))
            v=np.vstack((v,np.dot(v1,Ry(i*angle))))
            n=np.vstack((n,np.dot(n1,Ry(i*angle))))
        return f,v,n
        
    elif axe_rotation=='z':
        v1[:,0]=v1[:,0]+offset
        v1[:,1]=v1[:,1]+offset
        
        f,v,n = np.empty([0,3]), np.empty([0,3]), np.empty([0,3])
        
        for i in range (nb_repetition):
            stack = nv*i
            f=np.vstack((f,f1+stack))
            v=np.vstack((v,np.dot(v1,Rz(i*angle))))
            n=np.vstack((n,np.dot(n1,Rz(i*angle))))
        return f,v,n
        
