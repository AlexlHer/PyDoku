# -*- coding: utf-8 -*-

print("--------------------------------------")
print("Auteur : Ricardo Ramos, Rita Dos Santos, Alexandre l'Heritier")
print("--------------------------------------")
print("PyDoku v0.1")
print("--------------------------------------")

import random
from tkinter import *
import sys

def al_erreur_nb():
	"""
	Fonction qui permet d'afficher une fenètre d'erreur avec un texte
	explicatif.
	"""
	# On crée la fenetre.
	fenetreer = Tk()

	# On lui donne un titre.
	fenetreer.title("Erreur")

	# On crée les éléments...
	Label(fenetreer, text="Erreur", height=1, font=('Arial', 16, 'bold')).pack()
	Label(fenetreer, text="Chiffre(s) entré(s) non valide !", height=1, font=('Arial', 13)).pack()
	Button(fenetreer, text="Quitter", font=('Arial', 12, 'italic', 'bold'), command=sys.exit).pack()

	fenetreer.mainloop()
	# Fin : fenetreer.

def traitement_resultat()-> list:
	"""
	Fonction qui à pour but de créer une liste contenant des listes contenant
	chaqu'une les nombres entrés sur chaques lignes.
	"""
	# Permet de créer des variables globales.
	al_varglob = globals()

	# Permet de nommer les variables des cases.
	al_nb_case = 0

	# Liste qui sera retourner à la fin.
	al_liste_fin = []

	# Boucle qui parcourt les colonnes.
	for i in range(9):
		# Liste qui contiendera les lignes une par une.
		al_liste_temp = []
		# Boucle qui parcourt les lignes.
		for j in range(9):
			# Variable qui prend la valeur de la caseX.
			al_temp = al_varglob["al_case" + str(al_nb_case)].get()
			# Liste qui apprend les chiffres de la i ligne.
			al_liste_temp.append(al_temp)

			# Test qui appel la fonction erreur si un chiffre ne convient pas.
			if al_temp < 0 or al_temp > 9:
				al_erreur_nb()

			# Ajoute un 1 pour changer de case.
			al_nb_case += 1

		# La liste final apprend les listes contenant les chiffres des lignes.
		al_liste_fin.append(al_liste_temp)

	# Retourne la liste finale.
	return al_liste_fin

def interface_debut()-> list:
	"""
	Fonction qui crée l'interface nécessaire pour entrer les chiffres imposés
	du sudoku à résoudre.
	"""
	def a_propos():
		# Création de la fenètre.
		al_fenetre1apropos = Tk()

		# Titre de la fenètre.
		al_fenetre1apropos.title("A propos")

		# Ajoute un texte dans la fenètre.
		Label(al_fenetre1apropos, text="Projet Sudoku", font=('Arial', 30, 'italic', 'bold')).pack()
		Label(al_fenetre1apropos, text="Auteurs :", font=('Arial', 12, 'bold')).pack()
		Label(al_fenetre1apropos, text="Ricardo Ramos", font=('Arial', 12, 'bold')).pack()
		Label(al_fenetre1apropos, text="Rita Dos Santos", font=('Arial', 12, 'bold')).pack()
		Label(al_fenetre1apropos, text="Alexandre l'Heritier", font=('Arial', 12, 'bold')).pack()
		Label(al_fenetre1apropos, text="Projet final d'ISN", font=('Arial', 12)).pack()

	def aide():
		# Création de la fenètre.
		al_fenetre1aide = Tk()

		# Titre de la fenètre.
		al_fenetre1aide.title("Aide")

		# Ajoute un texte et un bouton dans la fenètre.
		Label(al_fenetre1aide, text="Entrer dans les cases les chiffres imposés", font=('Arial', 12, 'bold')).pack()
		Label(al_fenetre1aide, text="et appuyer sur GO. Laisser les 0 dans les cases", font=('Arial', 12, 'bold')).pack()
		Label(al_fenetre1aide, text="que vous souhaitez faire remplir par le programme.", font=('Arial', 12,'bold')).pack()
		Button(al_fenetre1aide, text="A propos", command=a_propos, font=('Arial', 12,'bold')).pack()
	# Création de la fenètre.
	al_fenetre1 = Tk()

	# Titre de la fenètre.
	al_fenetre1.title("Projet Sudoku")

	# Permet de créer des variables globales.
	al_varglob = globals()

	# Permet de nommer les variables des cases.
	al_nb_case = 0

	# Ajoute un titre et trois boutons dans la fenètre.
	Label(al_fenetre1, text="Résolution de Sudoku", font=('Arial', 12, 'italic', 'bold')).grid(row=0, column=0, columnspan=11)
	Button(al_fenetre1, text ="Quitter", command=sys.exit, font=('Arial', 12, 'italic', 'bold')).grid(row=12, column=0, columnspan=3)
	Button(al_fenetre1, text ="GO !!!", command=al_fenetre1.destroy, font=('Arial', 12, 'italic', 'bold')).grid(row=12, column=3, columnspan=5)
	Button(al_fenetre1, text ="Aide", command=aide, font=('Arial', 12, 'italic', 'bold')).grid(row=12, column=8, columnspan=3)

	# Boucles qui crée 11 lignes et 11 colonnes (9 pour mettre des chiffres et 2 pour les espace).
	for i in range(11):
		for j in range(11):
			# Test qui permet de mettre des séparations dans la grille.
			if i == 3 or i == 7:
				Label(al_fenetre1, text="", font=('Arial', 1)).grid(row=i+1, column=j)
			elif j == 3 or j == 7:
				Label(al_fenetre1, text="").grid(row=i+1, column=j)
			else:
				# "Transforme" la variable al_caseX en variable int pour tkinter.
				al_varglob["al_case" + str(al_nb_case)] = IntVar()

				# Ajoute 1 case sur la ligne i+1 et la colonne j.
				entrer = Entry(al_fenetre1, textvariable=al_varglob["al_case" + str(al_nb_case)], width=2, font=('Arial', 20, 'bold'))

				# Place la case sur la ligne i+1 et la colonne j.
				entrer.grid(row=i+1, column=j)

				# +1 car on avance d'une case.
				#print(al_nb_case)
				al_nb_case += 1

	# Permet de maintenir la fenètre ouverte (boucle infinie).
	al_fenetre1.mainloop()

	# Retourne la liste que retourne la fonction traitement_resultat().
	return traitement_resultat()

def interface_fin(liste:list):
	"""
	Fonction qui crée l'interface nécessaire pour afficher les chiffres
	du sudoku résolu.
	"""
	# Création de la fenètre.
	al_fenetre2 = Tk()

	# Titre de la fenètre.
	al_fenetre2.title("Projet Sudoku")

	# Ajoute un titre et un bouton dans la fenètre.
	Label(al_fenetre2, text="Sudoku résolu", font=('Arial', 12, 'italic', 'bold')).grid(row=0, column=0, columnspan=9)
	Button(al_fenetre2, text ="Fermer", command=sys.exit, font=('Arial', 12, 'italic', 'bold')).grid(row=10, column=0, columnspan=9)

	# Boucles qui crée 9 lignes et 9 colonnes.
	for i in range(9):
		# Prend la i liste.
		al_temp = liste[i]
		for j in range(9):
			# Affiche le chiffre de la ligne i et de la colonne j
			affiche = Label(al_fenetre2, text=al_temp[j], width=2, font=('Arial', 20, 'bold'))

			# Place le chiffre.
			affiche.grid(row = i+1, column = j)

	# Boucle infinie pour la fenètre.
	al_fenetre2.mainloop()

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


def bloc_vers_ligne(liste):
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

def remplissage_total(liste):
	grande_liste = []
	for x in range(3):
		for y in range(3):
			liste9 = []
			liste_bloc = ligne_vers_bloc(x, y, liste)
			liste_dispo = nb_dispo(liste_bloc)
			for z in range(9):
				if liste_bloc[z] == 0:
					liste9.append(liste_dispo[0])
					del liste_dispo[0]
				else:
					liste9.append(liste_bloc[z])
			grande_liste.append(liste9)
	grande_liste = bloc_vers_ligne(grande_liste)
	return grande_liste

def coordzero(l: list):
	"""
	Fonction qui permet de garder en memoire les coordonnées des zeros.
	"""
	l = total_ligne_vers_bloc(l)
	res = []
    
	for x in range(9):
		for y in range(9):
			if l[x][y] == 0:
				res.append([x, y])
	return res

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


def bloc_double(l:list):
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
	
	if blocs[inter] == 0:
		return False
	else:
		return inter

def remplace_bloc(liste:list, coordzero:list):
	bloc = bloc_double(liste)
	liste_inter = total_ligne_vers_bloc(liste)
	memoire_chiffre = []
	for i in range(9):
		if [bloc,i] not in coordzero:
			chiffre = randint(1, 10)
			while chiffre in memoire_chiffre:
				chiffre = random.randint(1, 10)
			memoire_chiffre.append(chiffre)
			liste_inter[bloc][i] = chiffre

	return bloc_vers_ligne(liste_inter)

def main():
	sudoku_initial = interface_debut()
	coord_zeros = coordzero(sudoku_initial)
	sudoku_rempli = remplissage_total(sudoku_initial)
	while bloc_double(sudoku_rempli) != False:
		sudoku_rempli = remplace_bloc(sudoku_rempli, coord_zeros)
	print(sudoku_rempli)
	interface_fin(sudoku_rempli)

main()
""""
Changelog :

v0.1 :
Fonctions terminées ajoutées.
"""
