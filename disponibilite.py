# -*- coding: utf-8 -*-
#--------------------------------------
# Auteurs : Ricardo Ramos, Rita Dos Santos, Alexandre l'Heritier
# PyDoku : Module disponibilite v1.0
#--------------------------------------

def disponibilite_sur_ligne(coord:tuple, l:list)->list:
	"""
	Fonction qui va chercher les disponibilités pour la ligne où se trouve
	la case, dont on donne les coordonnées sous forme de tuple dans 
	les arguments, dans la grille donnée sous forme de liste dans la grille.
	""" 
	y = coord[0]
	res = []
	for i in range(1,10):
		if i not in l[y]:
			res.append(i)
	return res

def disponibilite_sur_colonne(coord:tuple, liste:list)->list:
	"""
	Fonction qui cherche les chiffres qui ne sont pas dans la colonne
	voulu et renvoi ces chiffres.
	"""

	# Crée une liste avec neuf zero.
	temp = []

	# Boucle qui remplacent les zero par les chiffres de la colonne.
	for i in range(9):
		temp.append(liste[i][coord[1]])

	# Créer une liste dans fin.
	fin = []

	# Boucle qui prend les chiffres qui ne sont pas dans la liste temp.
	for i in range(1,10):
		if i not in temp:
			fin.append(i)

	# Retourne la liste fin.
	return fin

def ligne_vers_bloc(x, y, l:list)->list:
	if x == 1:
		x = 3
	if x == 2:
		x = 6
	if y == 1:
		y = 3
	if y == 2:
		y = 6
	ligne1 = l[x]
	ligne2 = l[x+1]
	ligne3 = l[x+2]
	liste = []
	for i in range(3):
		liste.append(ligne1[y+i])
	for i in range(3):
		liste.append(ligne2[y+i])
	for i in range(3):
		liste.append(ligne3[y+i])
	return liste

def total_ligne_vers_bloc(l:list)->list:
	fin = []
	for x in range(3):
		for y in range(3):
			a = ligne_vers_bloc(x, y, l)
			fin.append(a)
	return fin


def disponibilite_sur_bloc(coord:tuple, l:list)->list:
	liste = total_ligne_vers_bloc(l)
	x = coord[0]
	y = coord[1]
	if x in range(0,3):
		x = [1, 2, 3]
	elif x in range(3,6):
		x = [4, 5, 6]
	elif x in range(6,9):
		x = [7, 8, 9]

	if y in range(0,3):
		y = [1, 4, 7]
	elif y in range(3,6):
		y = [2, 5, 8]
	elif y in range(6,9):
		y = [3, 6, 9]
	for i in range(1,10):
		if i in x and i in y:
			liste_bloc = liste[i-1]
	# Créer une liste dans fin.
	fin = []

	# Boucle qui prend les chiffres qui ne sont pas dans la liste temp.
	for i in range(1,10):
		if i not in liste_bloc:
			fin.append(i)
	return fin

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
