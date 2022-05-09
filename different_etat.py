#nombre des différents termes du tableau

def etat_initial(lines):
    n = 1
    etat_ini=[]

    for ligne in lines:
        p = 2
        if n == 3:
            nbre_ini = int(ligne[0])
            for i in range(nbre_ini):
                etat_ini.append(int(ligne[p]))
                p = p + 2
        n = + 1
        return etat_ini

def etat_final(lines):
    n = 1
    etat_fin= []

    for ligne in lines:
        d = 2
        if n == 4:
            nbre_fin = int(ligne[0])
            for i in range(nbre_fin):
                etat_fin.append(int(ligne[d]))
                d = d + 2
        n = n + 1
        return etat_fin

def nombre_initial(lines):
    n = 1
    temp = ""
    m = 0
    for ligne in lines:
        if n == 3:
            while ligne[m] !=" ":
               temp = temp+ligne[m]
               m += 1
        nbre_ini = temp
        n = n + 1
    return nbre_ini


def nombre_final(lines):
    n = 1
    temp = ""
    m = 0
    for ligne in lines:
        if n == 4:
            while ligne[m] != " ":
                temp = temp+ligne[m]
                m += 1
        nbre_fin = temp
        n =+ 1

        return nbre_fin

def nombre_etat(lines):
    n = 1
    nbre_etat =0
    for ligne in lines:
        if n == 2:
            nbre_etat = int(ligne[0])
        n = n + 1
        return nbre_etat

def nombre_epsilon(lines):
    nbre_eps = lines[0]
    return nbre_eps

def nombre_lien(lines):
    n = 1
    nbre_lien=0
    for ligne in lines:
        if n == 5:
            nbre_lien = int(ligne)
        n = n + 1
    return nbre_lien





