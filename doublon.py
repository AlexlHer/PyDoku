# -*- coding: utf-8 -*-
#--------------------------------------
# Auteur : Alexandre
# Projet Sudoku : Module error
#--------------------------------------

def Doublon(l):
	resligne = []
	rescolonne = []
	for x in range(9):
		for i in range (9):
			if l[x].count(i) != 1:
				repetition = l[x].count(i)
				resinter = [x,i,repetition]
				resligne.append(resinter)
	for y in range(9):
		listinter = []
		for x in range(9):
			listinter.append(l[x][y])
		for i in range(9):
			if listinter..count(i) != 1:
				repetition = listinter.count(i)
				resinter = [y,i,repetition]
				rescolonne.append(resinter)
	return (rescolonne,resligne)