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
	 # Affecte à x le numéro de la ligne
	x = coord[0]
 
	 # Crée une liste pour garder les disponibilités de la ligne
	res = []
 
	 # Boucle qui vérifie les disponibilités
	for i in range(1,10):
		if i not in l[x]:
	  
	 # Rajoute les disponibilités dans la liste
			res.append(i)
   
	 # Retourne la fin de la liste 
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

def total_ligne_vers_bloc(l:list)->list:
	"""
	Transforme la liste qui contient les lignes en liste qui contient les blocs.
	"""
	# Créer une liste a retourner a la fin.
	fin = []

	# Boucle qui étudie les 9 blocs du sudoku.
	for x in range(3):
		for y in range(3):
				# Tests pour définir le bloc à traiter.
				if x == 1:
					x = 3
				if x == 2:
					x = 6
				if y == 1:
					y = 3
				if y == 2:
					y = 6

				# Prend les trois listes qui composent le bloc.
				ligne1 = l[x]
				ligne2 = l[x+1]
				ligne3 = l[x+2]

				# Liste qui append les chiffres du bloc.
				liste = []
				for i in range(3):
					liste.append(ligne1[y+i])
				for i in range(3):
					liste.append(ligne2[y+i])
				for i in range(3):
					liste.append(ligne3[y+i])

				# Append tous les blocs.
				fin.append(liste)
	# Retourne la liste fin.
	return fin


def disponibilite_sur_bloc(coord:tuple, l:list)->list:
	"""
	Fonction qui va chercher les disponibilités dans le bloc pour la case,
	dont on donne les coordonnées sous forme de tuple dans les arguments,
	dans la grille donnée sous forme de liste dans la grille.
	""" 
	# On fait appel à la fonction total_ligne_sur_bloc   
	liste = total_ligne_vers_bloc(l)
	 
	# On récupere les coordonnées de la case dans le tuple
	x = coord[0]
	y = coord[1]
 
	# On donne les blocs possibles suivant les coordonnées de x et de y
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
  
	# On cherche le bloc commun aux blocs disponibles pour x et pour y
	for i in range(1,10):
		if i in x and i in y:
	# On affecte à une variable la liste correspondant au bloc 
			liste_bloc = liste[i-1]
	# Créer une liste dans fin.
	fin = []

	# Boucle qui prend les chiffres qui ne sont pas dans la liste temp.
	for i in range(1,10):
		if i not in liste_bloc:
			fin.append(i)
	# Retourne la liste fin
	return fin

def disponibilite_sur_case(l:list, coord:tuple):
	"""
	Cette fonction cherche les disponibilités dans le cases
	"""
	 # Crée une liste pour garder les disponibilités
	res = []
 
	 # On affecte à une variable les disponibilités de la ligne 
	ligne = disponibilite_sur_ligne(coord, l)
 
	 # On affecte à une variable les disponibilités de la colonne
	colonne = disponibilite_sur_colonne(coord,l)
 
	 # On affecte à une variable les disponibilités du bloc
	bloc = disponibilite_sur_bloc(coord, l)

	# Boucle qui vérifie les chiffres communs dans les trois listes...
	for i in range(1,10):
		if i in ligne and i in colonne and i in bloc:
	  # ... et les rajoute dans la liste 
			res.append(i)
   
   	# Retourne la liste res
	return res
