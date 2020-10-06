# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:15:55 2020

@author: natha


from matplotlib.pyplot import *   
from numpy import *
import pickle


def pearson(x,y):
     n=len(x)
     vals=range(n)

     sumx=sum([float(x[i]) for i in vals])
     sumy=sum([float(y[i]) for i in vals])

     sumxSq=sum([x[i]**2.0 for i in vals])
     sumySq=sum([y[i]**2.0 for i in vals])

     pSum=sum([x[i]*y[i] for i in vals])
     # Calculating Pearson correlation
     num=pSum-(sumx*sumy/n)
     den=((sumxSq-pow(sumx,2)/n)*(sumySq-pow(sumy,2)/n))**.5
     if den==0: return 0
     r=num/den
     return 
 """
 
    
from matplotlib.pyplot import *   
from numpy import *
import pandas as pd
df = pd.read_csv('toy_complet.csv',header=None, delimiter=' ')
    
print(df)
#somme carrer de la ligne 
print('somme carrer  T  ')
T= ((df.loc[0] ** 2).sum())

print(T)
print ("")
print ("")
print ("")
print ("")
print("----------- Similarité Pearson ----------------")
for i in [0, 1, 2, 3,4,5,6,7,8,9,10,11]:
    max = 0
    
    S1=df.loc[0].sum()
    S2=df.loc[i].sum()
    
    Li= ((df.loc[i] ** 2).sum())

    print("somme des carrés de la ligne  ", i, " : ", Li)


    #produire scalaire 
   
    TLi=(df.loc[0]*df.loc[i]).sum()
    print('Ptot LigneO et Ligne', i," : ",TLi)

    #similarité du cosinus de T et U
    sci = ((TLi - (S1 * S2) / 1000)) / sqrt((T - ((S1**2) / 1000)) * (Li - ((S2**2) / 1000)))
    sci = round(sci,3)
    print('similarité Pearson LigneO et Ligne', i," : ",sci)
    print("----------------------------")
    print("                            ")
    print("                            ")
   
    
    
print("fin ")