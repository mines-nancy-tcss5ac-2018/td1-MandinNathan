# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:44:56 2018

@author: mandin4u
"""

def reverse(nb):
    nb=str(nb)
    nb_reverse=str()
    for i in range(1,len(nb)+1):
        nb_reverse=nb_reverse+nb[-i]
    return int(nb_reverse)

def test(n):
    nb=n
    for i in range(50):
        nb=nb+reverse(nb)
        if nb==reverse(nb):
            return None
    return n

def solve(n):
    L_Lychrel=[]
    for i in range(1,n+1):
        L_Lychrel.append(test(i))
    L_Lychrel=[i for i in L_Lychrel if i!=None]
    return len(L_Lychrel),L_Lychrel

n=10000

assert 196 in solve(196)[1]

print(solve(n)[0])
            