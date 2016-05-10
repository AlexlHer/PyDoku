# -*- coding: utf-8 -*-
#--------------------------------------
# Auteur : Alexandre
# Projet Sudoku : Module error
#--------------------------------------

def doublon(l):
    """
    Fonction qui va chercher les répétition dans une liste représentant une 
    grille de Sudoku.
    Argument:
    l : list
    retour:
    Tuple composé d'une liste qui donne les répétitions par ligne et une liste
    qui donne les répétitions par colonne. Ces deux listes sont elle-mêmes 
    composées de liste suivant ce format:
    [ligne ou colonne, coordonnée, nombre répété, nombre de fois répété]
    """
	resligne = []
	rescolonne = []
	for x in range(9):
		for i in range (1,10):
			if l[x].count(i) > 1:
				repetition = l[x].count(i)
				resinter = ['l',x,i,repetition]
				resligne.append(resinter)
	for y in range(9):
		listinter = []
		for x in range(9):
			listinter.append(l[x][y])
		for i in range(1,10):
			if listinter.count(i) > 1:
				repetition = listinter.count(i)
				resinter = ['c',y,i,repetition]
				rescolonne.append(resinter)
	return (resligne,rescolonne)
