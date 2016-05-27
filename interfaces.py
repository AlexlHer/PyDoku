# -*- coding: utf-8 -*-
#--------------------------------------
# Auteur : Alexandre l'Heritier
# PyDoku : Module interface v6.0
#--------------------------------------

from tkinter import *
import sys

def verif_ligne(liste, pos):
	"""
	Fonction qui verifie si il y a des doublons sur la pos ligne.
	"""
	# Ligne prend la ligne voulu.
	ligne = liste[pos]

	# Liste temp pour vérifier les doublons.
	temp = []

	# Boucle qui verifie chaque éléments de la ligne.
	for i in range(9):
		if ligne[i] == 0:
			pass
		else:
			# Retourne True si doublon.
			if ligne[i] in temp:
				return True
			temp.append(ligne[i])
	# Retourne False si il n'y a pas de doublon.
	return False

def verif_colonne(liste, pos):
	"""
	Fonction qui verifie si il y a des doublons sur la pos colonne.
	"""
	# Liste qui va contenir les éléments de la pos colonne.
	colonne = []

	# Boucle qui explore les 9 ligne de la liste.
	for i in range(9):
		colonne.append(liste[i][pos])
	# Liste temp pour vérifier les doublons.
	temp = []

	# Boucle qui verifie chaque éléments de la colonne.
	for i in range(9):
		if colonne[i] == 0:
			pass
		else:
			# Retourne True si doublon.
			if colonne[i] in temp:
				return True
			temp.append(colonne[i])
	# Retourne False si il n'y a pas de doublon.
	return False

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

def verif_bloc(liste, pos):
	"""
	Fonction qui verifie si il y a des doublons sur la pos bloc.
	"""
	liste = total_ligne_vers_bloc(liste)
	# Ligne prend la ligne voulu.
	ligne = liste[pos]

	# Liste temp pour vérifier les doublons.
	temp = []

	# Boucle qui verifie chaque éléments du bloc.
	for i in range(9):
		if ligne[i] == 0:
			pass
		else:
			# Retourne True si doublon.
			if ligne[i] in temp:
				return True
			temp.append(ligne[i])
	# Retourne False si il n'y a pas de doublon.
	return False

def verif_tout(liste):
	for i in range(9):
		ligne = verif_ligne(liste, i)
		colonne = verif_colonne(liste, i)
		bloc = verif_bloc(liste, i)
		if ligne == True or colonne == True or bloc == True:
			return True
	return False

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
	global save_liste
	save_liste = 0
	def a_create_save():
		# Créer un fichier .csv.
		ecrire = open("mettre_sudoku_ici.csv", "w")

		# Ecrit dedans.
		ecrire.write("Remplacer;les zeros par;les chiffres;voulu. Laisser;les zeros;dans les cases;à faire;remplir par;le programme;\n")
		ecrire.write("0;0;0;0;0;0;0;0;0;\n")
		ecrire.write("0;0;0;0;0;0;0;0;0;\n")
		ecrire.write("0;0;0;0;0;0;0;0;0;\n")
		ecrire.write("0;0;0;0;0;0;0;0;0;\n")
		ecrire.write("0;0;0;0;0;0;0;0;0;\n")
		ecrire.write("0;0;0;0;0;0;0;0;0;\n")
		ecrire.write("0;0;0;0;0;0;0;0;0;\n")
		ecrire.write("0;0;0;0;0;0;0;0;0;\n")
		ecrire.write("0;0;0;0;0;0;0;0;0;")


	def a_open_save():
		global save_liste
		# Ouvre le fichier .csv.
		lire = open("mettre_sudoku_ici.csv", "r")
		# Met toutes les lignes dans liste.
		liste = []
		for ligne in lire:
			liste.append(ligne)
		# Converti les lignes en liste puis réuni tous.
		liste1 = liste[1]
		liste1 = liste1.split(";")
		liste2 = liste[2]
		liste2 = liste2.split(";")
		liste3 = liste[3]
		liste3 = liste3.split(";")
		liste4 = liste[4]
		liste4 = liste4.split(";")
		liste5 = liste[5]
		liste5 = liste5.split(";")
		liste6 = liste[6]
		liste6 = liste6.split(";")
		liste7 = liste[7]
		liste7 = liste7.split(";")
		liste8 = liste[8]
		liste8 = liste8.split(";")
		liste9 = liste[9]
		liste9 = liste9.split(";")
		save_liste = [liste1, liste2, liste3, liste4, liste5, liste6, liste7, liste8, liste9]
		for i in range(9):
			for j in range(9):
				if len(save_liste[i][j]) != 1:
					save_liste[i][j] = save_liste[i][j][0]
				save_liste[i][j] = int(save_liste[i][j])

	def a_save():
		# Création de la fenètre.
		al_save = Tk()

		# Titre de la fenètre.
		al_save.title("Sauvegarde")

		# Ajoute les éléments dans la fenètre.
		Label(al_save, text='Le bouton "Créer un .csv" permet de créer', font=('Arial', 12, 'bold')).pack()
		Label(al_save, text="un fichier dans lequel vous pourrez mettre", font=('Arial', 12, 'bold')).pack()
		Label(al_save, text='votre sudoku a résoudre. Le bouton "Ouvrir', font=('Arial', 12, 'bold')).pack()
		Label(al_save, text='un .csv" permet de résoudre le sudoku', font=('Arial', 12, 'bold')).pack()
		Label(al_save, text="contenu dans le .csv. Après avoir pressé le bouton,", font=('Arial', 12, 'bold')).pack()
		Label(al_save, text="fermer les deux fenètre et appuyer sur GO !!!", font=('Arial', 12, 'bold')).pack()
		Button(al_save, text="Créer un .csv", command=a_create_save, font=('Arial', 12,'bold')).pack()
		Button(al_save, text="Ouvrir un .csv", command=a_open_save, font=('Arial', 12,'bold')).pack()

	def a_propos():
		# Création de la fenètre.
		al_fenetre1apropos = Tk()

		# Titre de la fenètre.
		al_fenetre1apropos.title("A propos")

		# Ajoute un texte dans la fenètre.
		Label(al_fenetre1apropos, text="PyDoku v2.0", font=('Arial', 30, 'italic', 'bold')).pack()
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
		Button(al_fenetre1aide, text="Sauvegarde", command=a_save, font=('Arial', 12,'bold')).pack()
		Button(al_fenetre1aide, text="A propos", command=a_propos, font=('Arial', 12,'bold')).pack()
	# Création de la fenètre.
	al_fenetre1 = Tk()

	# Titre de la fenètre.
	al_fenetre1.title("PyDoku v2.0")

	# Permet de créer des variables globales.
	al_varglob = globals()

	# Permet de nommer les variables des cases.
	al_nb_case = 0

	# Ajoute un titre et trois boutons dans la fenètre.
	Label(al_fenetre1, text="Résolution de Sudoku", font=('Arial', 12, 'italic', 'bold')).grid(row=0, column=0, columnspan=11)
	Button(al_fenetre1, text ="Quitter", command=sys.exit, font=('Arial', 12, 'italic', 'bold'), relief=FLAT).grid(row=12, column=0, columnspan=3)
	Button(al_fenetre1, text ="GO !!!", command=al_fenetre1.destroy, font=('Arial', 12, 'italic', 'bold'), relief=FLAT).grid(row=12, column=3, columnspan=5)
	Button(al_fenetre1, text ="Aide/Save", command=aide, font=('Arial', 12, 'italic', 'bold'), relief=FLAT).grid(row=12, column=8, columnspan=3)

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

	# Verifie et retourne la liste que retourne la fonction traitement_resultat() ou save_liste 
	# si une sauvegarde est ouverte, si problème dans liste, retourne une erreur.
	if save_liste == 0:
		liste_a_retourner = traitement_resultat()
		if verif_tout(liste_a_retourner) == True:
			al_erreur_nb()
		else:
			return liste_a_retourner
	else:
		if verif_tout(save_liste) == True:
			al_erreur_nb()
		else:
			return save_liste

def interface_fin(liste:list, save:list):
	"""
	Fonction qui crée l'interface nécessaire pour afficher les chiffres
	du sudoku résolu.
	"""
	def al_save_fin():
		# Créer un fichier .csv. 
		ecrire = open("sudoku_resolu.csv", "w")

		# Ecrit dedans.
		ecrire.write("Sudoku;résolu !!!;\n")
		for i in range(9):
			for j in range(9):
				ecrire.write(str(liste[i][j]))
				ecrire.write(";")
			ecrire.write("\n")

	# Création de la fenètre.
	al_fenetre2 = Tk()

	# Titre de la fenètre.
	al_fenetre2.title("PyDoku v2.0")

	# Ajoute un titre et un bouton dans la fenètre.
	Label(al_fenetre2, text="Sudoku résolu", font=('Arial', 12, 'italic', 'bold')).grid(row=0, column=0, columnspan=9)
	Button(al_fenetre2, text ="Fermer", command=sys.exit, font=('Arial', 12, 'italic', 'bold'), relief=FLAT).grid(row=10, column=0, columnspan=4)
	Button(al_fenetre2, text ="Sauvegarder dans .csv", command=al_save_fin, font=('Arial', 12, 'italic', 'bold'), relief=FLAT).grid(row=10, column=4, columnspan=5)

	# Boucles qui crée 9 lignes et 9 colonnes.

	for i in range(9):
		for j in range(9):
			# Gère la couleur des cases, si le chiffre a été entrer par l'user, la couleur sera noir sinon rouge ou orange.
			if liste[i][j] == save[i][j]:
				affiche = Label(al_fenetre2, text=liste[i][j], width=2, font=('Arial', 20, 'bold'), fg="black")
			else:
				if (i in range(0,3) or i in range(6,9)) and (j in range(0,3) or j in range(6,9)):
					fond = "red"
				if (i in range(3,6) or i in range(6,9)) and j in range(3,6):
					fond = "red"
				if (i in range(0,3) or i in range(6,9)) and j in range(3,6):
					fond = "orange"
				if i in range(3,6) and (j in range(0,3) or j in range(6,9)):
					fond = "orange"

				# Affiche le chiffre de la ligne i et de la colonne j
				affiche = Label(al_fenetre2, text=liste[i][j], width=2, font=('Arial', 20, 'bold'), fg=fond)

			# Place le chiffre.
			affiche.grid(row = i+1, column = j)

	# Boucle infinie pour la fenètre.
	al_fenetre2.mainloop()

"""
Changelog :
v6.0 :
Ajout une verification de grille pour éviter les doublons.

v5.0 :
Ajout de couleur pour l'interface de fin.

v4.0 :
Ajout de possibilité de sauvegardes.

v3.0 :
Interface avec plus d'instruction pour l'utilisateur.

v2.1 :
Correction d'un bug avec les espaces dans la grille de l'interface_debut().

v2.0 :
Commentaires ajoutés.
Interface amélioré.
Ajout de l'interface de fin (interface_fin()) et d'erreur.

v1.0 :
Version fonctionnel de l'interface de début du sudoku.
"""
