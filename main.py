from different_etat import*
from fonction import*

lines = []
with open("fichier.txt", "r") as x:
    lines = x.readline()
    
nbre_init = (nombre_initial(lines))
nbre_fin = (nombre_final(lines))
nbre_etat = (nombre_etat(lines))
nbre_epsilon = (nombre_epsilon(lines))
nbre_lien = nombre_lien(lines)
etat_ini = (etat_initial(lines))
etat_fin = (etat_final(lines))

print("etats initiaux:",nbre_init)
print("etats ficaux:",nbre_fin)
































































