# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 15:55:59 2016

@author: rdossantos
"""

def disponibilite_sur_ligne(coord:tuple, l:list)->list:
"""
Cette fonction vérifie les chiffres qui ne sont pas dans la ligne pour
une coordonnee y constante puis si elle n'est pas sur dans la ligne
le chiffre qui varie de 1 à 10 sera rajouté à une liste l de la disponibilité
"""
    y = coord[0]
    res = []
    for i in range(1,10):
        if i not in l[y]: #si le chiffre i ne se trouve pas dans la ligne il sera rajouté à la liste l
            res.append(i)
    return res

