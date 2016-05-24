# -*- coding: utf-8 -*-
# Auteurs : Ricardo Ramos, Rita Dos Santos, Alexandre l'Heritier
print("----------------------------------------------------------------------")
print("PyDoku v2.0")
print("----------------------------------------------------------------------")

from interfaces import *
from disponibilite import *

def coordzero(liste: list):
	"""
	Fonction qui permet de garder en memoire les coordonnées des zeros.
	"""

	# Création d'une liste qui contiendra toutes les coordonnées
	res = []
    
	# On parcourt la grille à l'aide de deux boucles
	for x in range(9):
		for y in range(9):
			# On vérifie si la valeur dans la case est un zéro et si 
			# c'est le cas on garde les coordonnées sous forme de liste
			if liste[x][y] == 0:
				res.append([x, y])
	# On retourne la liste avec toutes les coordonnées
	return res


def ordre(sudoku:list, coordzero:list):

	# Création d'une liste qui va sauvegarder le résultat
	res = []
	# Parcourt de la grille
	for x in range(9):
		for y in range(9):
			# On vérifie si les coordonnées de la case sont dans 
			# les coordonnées correspondant aux zéros
			if [x, y] in coordzero:
				disp = disponibilite_sur_case(sudoku, (x,y))
				res_inter = [(x,y), disp]
				res.append(res_inter)
	final = []
	i = 1
	while i < 10:
		for x in range (len(res)):
			if len(res[x][1]) == i:
				final.append(res[x][0])
		i += 1
	return final




def remplissage(sudoku:list, coordzero):
	order = ordre(sudoku, coordzero)
	i = 0
	erreur = 0
	while i < len(order):
		erreur += 1
		#if erreur > 100000:
			#al_erreur_nb()
		if i < 0:
			i = 0
		x = order[i][0]
		y = order[i][1]
		disp = disponibilite_sur_case(sudoku,(x,y))
		if sudoku[x][y] == 0:
			j = 1
			while j < 10:
				if j in disp:
					sudoku[x][y] = j
					i += 1
					break
				j += 1
			if j == 10:
				sudoku[x][y] = 0
				i -= 1
				continue
		elif sudoku[x][y] != 0:
			j = sudoku[x][y]
			while j < 10:
				if j in disp:
					sudoku[x][y] = j
					i += 1
					break
				j += 1
			if j == 10:
				sudoku[x][y] = 0
				i -= 1
	return sudoku

def main():
	sudoku_initial = interface_debut()
	coord_zeros = coordzero(sudoku_initial)
	fin = remplissage(sudoku_initial, coord_zeros)
	interface_fin(fin)

main()
""""
Changelog :

v2.0 :
Mélange des deux programmes.
Tous les bugs résolus.

v1.0 (Alexandre) :
Passage du mode aléatoire en mode backtracking.
Choix d'une méthode linéaire.
Bug sur les sudokus difficiles.

v1.0 (Ricardo) :
Passage du mode aléatoire en mode backtracking.
Choix d'une méthode récursive.
Bugs aléatoire.

v0.1 :
Fonctions principals ajoutées.
"""

