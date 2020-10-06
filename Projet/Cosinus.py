# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:25:31 2020

@author: natha
"""

""" 1.3.1 Similarité du cosinus
Pour calculer la similarité du cosinus on doit calculer le produit scalaire des deux vecteurs et le diviser par le produit des normes des deux vecteurs.
Concrètement :

    norme d'un vecteur T de dimension n :

       |T| = sqrt(T1 * T1 + T2 * T2 + ... + Tn * Tn)

    produit scalaire de deux vecteurs T et U de dimension n :

        T . U = T1 * U1 + T2 * U2 + ... + Tn * Un

    similarité du cosinus de T et U

        simCos(T,U) = (T . U) / (|T| * |U|) 

"""
from matplotlib.pyplot import *   
from numpy import *
import pandas as pd
df = pd.read_csv('toy_complet.csv',header=None, delimiter=' ')
    
print(df)
print('   t   ')
print(df.loc[0])

print('somme de la ligne   ')
print(df.loc[0].sum())

#somme carrer de la ligne 
print('somme carrer norme T  ')
T= ((df.loc[0] ** 2).sum())
T= sqrt(T)
print(T)

print("----------------------------")
print("----------------------------")
print("----------------------------")
"""
#somme carrer de la ligne 
print('   somme carrer norme U  ')
U= ((df.loc[1] ** 2).sum())
U= sqrt(U)
print(U)



#produire scalaire 
print('  produit sclaire TU  ')
TU=(df.loc[0]*df.loc[1]).sum()
print (TU)


#similarité du cosinus de T et U
print('  similarité du cosinus de T et U')
sc3=TU/(T*U)
print(sc3)

print("----------------------------")


#similariter avec l2
#somme carrer de la ligne 
print('   somme carrer norme L2  ')
L2= ((df.loc[2] ** 2).sum())
L2= sqrt(L2)
print(L2)


#produire scalaire 
print('  produit sclaire TL2  ')
TL2=(df.loc[0]*df.loc[2]).sum()
print (TL2)

#similarité du cosinus de T et U
print('  similarité du cosinus de T et U')
sc4=TL2/(T*L2)
print(sc4)
"""

print("----------- Similarité Cosinus ----------------")
for i in [0, 1, 2, 3,4,5,6,7,8,9,10,11]:
    max = 0
    
    Li= ((df.loc[i] ** 2).sum())
    Li= sqrt(Li)
    print("norme de la ligne ", i, " : ", Li)


    #produire scalaire 
   
    TLi=(df.loc[0]*df.loc[i]).sum()
    print('produit sclaire LigneO et Ligne', i," : ",TLi)

    #similarité du cosinus de T et U
    sci = TLi/(T*Li)
    sci = round(sci,5)
    print('similarité cosinus LigneO et Ligne', i," : ",sci)
    print("----------------------------")
    print("                            ")
    print("                            ")
    
   
     

    
    
    
print("fin ")

print(max)









