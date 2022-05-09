#nombre des différents termes du tableau

def etat_initial (lines):
    n = 1
    etat_initial=[]

    for ligne in lines:
        p = 2
        if n == 3:
            nombre_initial=int(ligne[0])
            for i in range (nombre_initial):
                etat_initial.append(int(ligne[p]))
                p = p + 2
            n = + 1
        return etat_initial

def etat_final (lines):
    n = 1
    etat_final= []

    for ligne in lines:
        d = 2
        if n == 4:
            nombre_final = int(ligne[0])
            for i in range(nombre_final):
                etat_final.append(int(ligne[d]))
                d = d + 2
            n = n + 1
        return etat_final

def nombre_initial (lines):
    n=1
    temp=""
    m=0
    for ligne in lines:
        if n==3:
            while ligne[m] !=" ":
               temp=temp+ligne[m]
               m+=1
        nbre_ini=temp
        n=n+1
    return nbre_ini


def nombre_final (lines):
    n = 1
    temp=""
    m=0
    for ligne in lines:
        if n == 4:
            while ligne[m] !=" ":
                temp = temp+ligne[m]
                m+=1
            nbre_final = temp
        n =+ 1

        return nbre_final

def nombre_etat (lines):
    n = 1
    for ligne in lines:
        if n == 2:
            nombre_etat = int(ligne[0])
        n = n + 1

        return nombre_etat

def nombre_epsilon (lines):
    nombre_epsilon= lines[0]
    return nombre_epsilon

def nombre_lien (lines):
    n=1
    for ligne in lines:
        if n == 5:
            nombre_lien = int(ligne)
        n = n + 1
    return nombre_lien





