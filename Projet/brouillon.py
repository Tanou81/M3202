# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import xlrd
from matplotlib.pyplot import *   
from numpy import *
import pickle
f=open('toy_complet.csv','rb')
contenu = f.read()
print (contenu)
with open('toy_complet.csv','rb')as fichier:
    mon_pickler = pickle.Pickler(fichier)
    #enregistrement
    







