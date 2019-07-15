# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:34:09 2019

@author: tidad
"""

import pickle

donnees=dict()
mots=["gang","avion","debut","basket","carte","micro","batterie","carnet","eau","feu","album"]


def nouveau_joueur(nom):
    donnees[nom]=0

def gagne(nom):
    donnees[nom]+=1

def perdu(nom):
    donnees[nom]-=1
    
def sauvegarder():
    with open('scores','wb') as fichier:
        pick=pickle.Pickler(fichier)
        pick.dump(donnees)

def charger():
    global donnees
    with open('scores','rb') as fichier:
        pick=pickle.Unpickler(fichier)
        donnees=pick.load()