# -*- coding: utf-8 -*-
# Auteurs : Ricardo Ramos, Rita Dos Santos, Alexandre l'Heritier
print("----------------------------------------------------------------------")
print("PyDoku v3.0")
print("----------------------------------------------------------------------")

from interfaces import *
from disponibilite import *
from copy import deepcopy

def coordzero(liste: list):
	"""
	Fonction qui permet de garder en memoire les coordonnées des zéros d'une grille donnée
	en argument et qui renvoie le tout sous forme de liste.
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
	"""
	Fonction qui va donner l'ordre de traitement des cases vides d'une grille donnée
	en argument grâce à l'aide d'une liste qui répertorie les coordonnées des zéros
	et des disponibilités pour chaque case, puis renvoie cet orde sous forme de liste.
	"""

	# Création d'une liste intermédiaire qui va sauvegarder le résultat
	res = []
	# Parcourt de la grille
	for x in range(9):
		for y in range(9):
			# On vérifie si les coordonnées de la case sont dans 
			# les coordonnées correspondant aux zéros
			if [x, y] in coordzero:
				# Si c'est le cas on ajoute à la liste intermédiaire
				# les coordonnées ainsi que les disponibilités
				disp = disponibilite_sur_case(sudoku, (x,y))
				res_inter = [(x,y), disp]
				res.append(res_inter)
	# Création de la liste finale
	final = []
	# Initialisation d'un compteur pour la boucle
	i = 1
	# Boucle qui va trier la liste par ordre croissant du nombre de disponibilité des cases
	while i < 10:
		# Boucle qui parcourt la liste intermédiaire
		for x in range (len(res)):
			if len(res[x][1]) == i:
				final.append(res[x][0])
		i += 1
	# On retourne la liste donnant l'ordre
	return final




def remplissage(sudoku:list, coordzero:list):
	"""
	Fontion qui va remplir les cases à traiter d'une grille donnée en argument dans
	l'ordre croissant du nombre de disponibilités par case, ordre donné grâce à la 
	fonction ordre() qui nécessite la grille et les coordonnées des zéros, données aussi
	en argument.
	"""
	
	# On détermine l'ordre de traitement grâce à la fontion ordre()
	order = ordre(sudoku, coordzero)
	# Initialisation du compteur pour la boucle
	i = 0
	# Boucle qui va remplir les cases à traiter
	while i < len(order):
		# Si le compteur i repasse en dessous de 0, on le remet à 0
		if i < 0:
			i = 0
		# On récupère les coordonnées de la case dans la liste de l'ordre
		x = order[i][0]
		y = order[i][1]
		# On récupère les disponibilités actuelles de la case
		disp = disponibilite_sur_case(sudoku,(x,y))
		# Dans le cas où la case n'a pas été modifiée, c'est à dire que la valeur est égale à 0
		if sudoku[x][y] == 0:
			# Initialisation d'un compteur
			j = 1
			# Boucle qui fait que si j atteind une valeur disponible pour la case,
			# elle va affecter cette valeur à la case, augmenter i de 1 puis s'arrêter
			while j < 10:
				if j in disp:
					sudoku[x][y] = j
					i += 1
					break
				j += 1
			# Si j atteind 10, cela veut dire qu'il n'y a pas de disponibilité pour la 
			# case actuellement donc on revient à la case d'avant en enlevant 1 à i
			if j == 10:
				sudoku[x][y] = 0
				i -= 1
				continue
		# Dans le cas où la valeur de la case est non nulle, cela veut dire que nous revenons 
		# sur la case et que donc nous devons trouver une autre possibilité
		elif sudoku[x][y] != 0:
			# Initialisation d'un compteur avec la valeur de la case
			j = sudoku[x][y]
			# Boucle qui fait que si j atteind une valeur disponible pour la case,
			# elle va affecter cette valeur à la case, augmenter i de 1 puis s'arrêter
			while j < 10:
				if j in disp:
					sudoku[x][y] = j
					i += 1
					break
				j += 1
			# Si j atteind 10, cela veut dire qu'il n'y a pas de disponibilité pour la 
			# case actuellement donc on revient à la case d'avant en enlevant 1 à i
			if j == 10:
				sudoku[x][y] = 0
				i -= 1
	# On retourne la grille finale sous forme de liste
	return sudoku

def main():
	# On récupère la grille iniciale dans l'interface
	sudoku_initial = interface_debut()
	# Copie de la grille dans une autre variable pour la sauver.
	save_sudoku = deepcopy(sudoku_initial)
	# On récupère les coordonnées des zéros de la case
	coord_zeros = coordzero(sudoku_initial)
	# On remplis grâce à la fonction remplissage
	fin = remplissage(sudoku_initial, coord_zeros)
	# On affiche la grille finale à l'aide de l'interface
	interface_fin(fin, save_sudoku)

main()
""""
Changelog :
v3.0 :
Ajout des commentaires.

v2.0 :
Mélange des deux programmes.
Tous les bugs résolus.

v1.0 (Alexandre) :
Passage du mode aléatoire en mode backtracking.
Choix d'une méthode itératif.
Bug sur les sudokus difficiles.

v1.0 (Ricardo) :
Passage du mode aléatoire en mode backtracking.
Choix d'une méthode récursive.
Bugs aléatoire.

v0.1 :
Fonctions principals ajoutées.
"""

