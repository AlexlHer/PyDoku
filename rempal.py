# -*- coding: utf-8 -*-
#--------------------------------------
# Auteur : Alexandre
# Projet Sudoku : Module rempal
#--------------------------------------

import random
    
def bloc(x, y, l:list)->list:
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

def nb_dispo(liste):
	liste2 = []
	fin = []
	for i in range(9):
		if liste[i] != 0:
			liste2.append(liste[i])
	for i in range(9):
		if i+1 not in liste2:
			fin.append(i+1)
	return fin

def liste_finale(liste):
	liste_fin = []
	for i in range(3):
		if i == 1:
			x = 3
		if i == 2:
			x = 6
		liste1 = liste[x]
		liste2 = liste[x+1]
		liste3 = liste[x+2]
		for j in range(3):
			for k in range(3):
				liste_fin.append(liste1)
				liste_fin.append(liste1)
				liste_fin.append(liste1)

def remplissage_total(liste):
	grande_liste = []
	for x in range(3):
		for y in range(3):
			liste9 = []
			liste_bloc = bloc(x, y, liste)
			liste_dispo = nb_dispo(liste_bloc)
			for z in range(9):
				if liste_bloc[z] == 0:
					liste9.append(liste_dispo[0])
					del liste_dispo[0]
				else:
					liste9.append(liste_bloc[z])
			grande_liste.append(liste9)
	grande_liste
	return liste
 
print(remplissage_total([[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]))