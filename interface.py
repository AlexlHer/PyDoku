# -*- coding: utf-8 -*-
# Auteur : Alexandre
# Projet final : Module interface v1.0

from tkinter import *

def traitement_resultat():
	"""
	Fonction qui à pour but de créer une liste contenant des listes contenant
	chaqu'une les nombres entrés sur chaques lignes.
	"""
	al_varglob = globals()
	al_nb_case = 0
	al_liste_fin = []
	for i in range(9):
		al_liste_temp = []
		for j in range(9):
			al_liste_temp.append(al_varglob["al_case" + str(al_nb_case)].get())
			al_nb_case += 1
		al_liste_fin.append(al_liste_temp)
	return al_liste_fin

def interface_debut():
	"""
	Fonction qui crée l'interface necessaire pour entrer les chiffres imposés
	du sudoku à résoudre.
	"""
	al_fenetre1 = Tk()
	al_varglob = globals()
	al_nb_case = 0
	for i in range(9):
		for j in range(9):
			al_varglob["al_case" + str(al_nb_case)] = IntVar()
			entrer = Entry(al_fenetre1, textvariable=al_varglob["al_case" + str(al_nb_case)])
			entrer.grid(row = i, column = j)
			al_nb_case += 1
	al_fenetre1.mainloop()

	return traitement_resultat()

#interface_debut()

"""
Changelog :
v2.0 (changelog provisoire) :
Commentaires ajoutés.
Interface amélioré.
Ajout de l'interface de fin (interface_fin()).

v1.0 :
Version fonctionnel de l'interface de début du sudoku.
"""