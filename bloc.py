# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
def encadrement(nbre:int)->tuple:
    if nbre in range (0,3):
        tup = (0,3)
    elif nbre in range (3,6):
        tup = (3,6)
    else:
        tup = (6,9)
    return tup
    
def disponibilité_sur_bloc(coord:tuple, l:list)->list:
    x = coord[0]
    y = coord[1]
    temp = []
    res = []
    blocx = encadrement(x)
    blocy = encadrement(y)
    for i in range (blocy[0], blocy[1]):
        for j in range (blocx[0], blocx[1]):
            print(i,j)
            temp.append(l[i][j])
    for i in range (1,10):
        print(i)
        if i not in temp:
            res.append(i)
    return res
            
    
    