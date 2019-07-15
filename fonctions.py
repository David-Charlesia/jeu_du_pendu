# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:58:03 2019

@author: tidad
"""

import donnees
from random import randint

mot=""
m_j=""
joueur=""
compteur=0

def nouveau():
    global mot
    global joueur
    global m_j
    
    i=randint(0,len(donnees.mots)-1)
    mot=donnees.mots[i]
    
    joueur=input("Entre votre pseudo : ")
    donnees.nouveau_joueur(joueur)
    m="*"*len(mot)
    print("Mot : "+m)
    m_j="*"*len(mot)
    
def aff_mot(i):
    global m_j
    m=""
    if i!=-1:
        for j in range(0,i):
            m+=m_j[j]
            
        m+=mot[i]
        
        for k in range(i+1,len(mot)):
            m+=m_j[k]
            
        m_j=m        
        print("Mot : "+m)
    else:
        print("Mot : "+m_j)
    
def jouer():
    global compteur
    
    lettre=input("Entrez une lettre : ")
    
    c=compteur
    
    for i in range(len(mot)):
        if mot[i]==lettre:
            donnees.gagne(joueur)
            print("bravo !")
            aff_mot(i)
            compteur+=1
    
    if c==compteur:
        donnees.perdu(joueur)
        print("dommage !")
        aff_mot(-1)
    
    #donnees.charger()
    
def fin():
    if mot==m_j:
        return True
    else:
        return False