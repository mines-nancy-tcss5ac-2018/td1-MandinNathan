# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 14:38:55 2018

@author: mandin4u
"""

def solve(n):
#Initialisation de la somme a 0
    S=0 
    A=2**n 
#Convertion de l'entier en chaine de caractere (permet l'acces aux chiffres un par un)
    L=str(A)

    for i in range(len(L)):
        S=S+int(L[i]) 
    return S

assert solve(15)==26

n=1000

print(solve(n))
