# -*- coding: utf-8 -*-
#--------------------------------------
# Auteur : Alexandre
# Projet Sudoku : Module colonne
#--------------------------------------

def disponibilite_sur_colonne(coord, liste):
    """
    Fonction qui cherche les chiffres qui ne sont pas dans la colonne
    voulu et renvoi ces chiffres.
    """
    
    # Crée une liste avec neuf zero.
    temp = [0]*9
    
    # Boucle qui remplacent les zero par les chiffres de la colonne.
    for i in range(9):
        # Prend la i ligne.
        ligne = liste[i]
        
        # Prend le chiffre qui appartient a la colonne et a la i ligne.
        temp[i] = ligne[coord[1]]
        
    # Créer une liste dans fin.
    fin = []
    
    # Boucle qui prend les chiffres qui ne sont pas dans la liste temp.
    for i in range(9):
        if i+1 != temp[i]:
            fin.append(i+1)
    
    # Retourne la liste fin.
    return fin
