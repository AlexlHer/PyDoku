# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 16:56:38 2016

@author: rdossantos
"""

def disponibilite_sur_case(l:list, coord:tuple):
    """
    Cette fonction vérifie les différentes possibilités d'une case
    """
    res = []
    ligne = disponibilite_sur_ligne(coord, l)
    colonne = disponibilite_sur_colonne(coord,l)
    bloc = disponibilite_sur_bloc(coord, l)

    for i in range(1,10):
        if i in ligne and i in colonne and i in bloc:
            res.append(i)
    return res
