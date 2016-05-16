# -*- coding: utf-8 -*-
#--------------------------------------
# Auteur : Alexandre
# Projet Sudoku : Module error
#--------------------------------------

def doublon(l:list):
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
		resinter = 0
		for i in range (1,10):
			if l[x].count(i) > 1:
				resinter += 1
		resligne.append(resinter)
	for y in range(9):
		listinter = []
		resinter = 0
		for x in range(9):
			listinter.append(l[x][y])
		for i in range(1,10):
			if listinter.count(i) > 1:
				resinter += 1
		rescolonne.append(resinter)
	return (resligne,rescolonne)


def doub_bloc(l:list):
	repet = doublon(l)
	blocs = [0]*9
	for i in range (3):
		blocs[0] += repet[0][i] + repet[1][i]
		blocs[1] += repet[0][i]
		blocs[2] += repet[0][i]
		blocs[3] += repet[1][i]
		blocs[6] += repet[1][i]
	for i in range(3,6):
		blocs[1] += repet[1][i]
		blocs[3] += repet[0][i]
		blocs[4] += repet[0][i] + repet[1][i]
		blocs[5] += repet[0][i]
		blocs[7] += repet[1][i]
	for i in range(6,9):
		blocs[2] += repet[1][i]
		blocs[5] += repet[1][i]
		blocs[6] += repet[0][i]
		blocs[7] += repet[0][i]
		blocs[8] += repet[0][i] + repet[1][i]

	inter = 0
	for j in range(1,8):
		if blocs[j]>blocs[inter]:
			inter = j
			
	return inter


