# Projet Final ISN
## Ricardo, Rita et Alexandre
Projet final d'ISN 2016 :

Résolution d’une grille de Sudoku

On propose d’implémenter un algorithme permettant la résolution d’un sudoku : il s’agit de compléter une grille 9 X 9 à l’aide des chiffres 1 à 9, chaque chiffre ne pouvant être utilisé qu’une fois dans chaque ligne, dans chaque colonne et dans chacun des neufs blocs 3 X 3 constituant le sudoku.

## Comment Faire

- [x] Fonction DisponibiliteSurLigne qui va donner les chiffres disponibles sur une ligne.
- [x] Fonction DisponibiliteSurColonne qui va donner les chiffres disponibles sur une colonne.
- [x] Fonction DisponibiliteSurBloc qui va donner les chiffres disponibles sur bloc.
- [x] Fonction DisponibiliteSurCase qui va donner les chiffres disponibles sur une case.
- [x] Fonction Doub qui trouve le nombre de doublants par ligne.
- Fonction Doub_bloc qui dit combien de doublons il y a sur chaque bloc.
- [x] Fonction RempAl qui va remplir aleatoirement selon les disponibilites dans chaque case.
- [x] Fonction CoordZero qui va garder en memoire les coordonnees des zeros.
- Fonction Remplacer_Bloc qui va modifier aléatoirement le bloc avec le plus de doublons.
- Fonction Main
http://www-igm.univ-mlv.fr/~dr/XPOSE2013/sudoku/stochastique.html#principe
