# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 14:55:56 2018

@author: mandin4u
"""

def solve(f):
#Creation de listes vide pour lister les noms et les resultats
    L_nom=[]
    score_f=0
    for ligne in f:
        L_nom=L_nom+ligne.split(',')
    L_nom=sorted(L_nom)
    for i in range(len(L_nom)):
#       Initialisation du score a 0
        S=0
        for j in range(1,len(L_nom[i])-1):
            S=S+(alphabet.index(L_nom[i][j])+1)
        score_f=score_f+(i+1)*S
        
    return score_f

f=open('p022_names.txt','r')
f_test=open('p022_test.txt','r') #fichier txt contenant "COLIN"

alphabet=['A','B','C','D','E','F','G','H','I','J','K','L',\
'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

assert solve(f_test)==53

print(solve(f))

    
