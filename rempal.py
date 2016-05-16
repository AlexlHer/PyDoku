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
	fin = []
	for i in range(3):
		ia = 0
		if i == 1:
			ia = 3
		if i == 2:
			ia = 6
		liste1 = liste[ia]
		liste2 = liste[ia+1]
		liste3 = liste[ia+2]
		ligne1 = [liste1[0], liste1[1], liste1[2], liste2[0], liste2[1], liste2[2], liste3[0], liste3[1], liste3[2]]
		ligne2 = [liste1[3], liste1[4], liste1[5], liste2[3], liste2[4], liste2[5], liste3[3], liste3[4], liste3[5]]
		ligne3 = [liste1[6], liste1[7], liste1[8], liste2[6], liste2[7], liste2[8], liste3[6], liste3[7], liste3[8]]
		fin.append(ligne1)
		fin.append(ligne2)
		fin.append(ligne3)
	return fin

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
	grande_liste = liste_finale(grande_liste)
	return grande_liste
 
#print(remplissage_total([[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]))
