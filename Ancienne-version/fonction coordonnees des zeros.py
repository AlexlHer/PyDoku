# -*- coding: utf-8 -*-
"""
Created on Tue May  3 15:37:51 2016

@author: rdossantos
"""
"""
Cette fonction permet de garder en memoire les coordonnées des zeros.
"""
def CoordZero(l: list):
    res = []
    
    for x in range(9):
        for y in range(9):
            if l[x][y] == 0:
                res.append([x, y])
    return res
