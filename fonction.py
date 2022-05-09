from tabulate import tabulate


def entree_sortie (n,nombre_initial,nombre_final,etat_initial,etat_final):
    e_s=""
    for i in range (0,nombre_initial):
        if n == etat_initial[i]:
            e_s= e_s +"E"
    for j in range (0,nombre_final):
        if n == etat_initial[j]:
            e_s= e_s +"S"
    return e_s

alphabet = ['a','b','c','d'] #on peut continuer l'alphabet pour les différents lien

def lien (lien,alphabet,nombre_epsilon):
    for i in range(0, nombre_epsilon):
        if (lien==alphabet[i]):
            return 1
    return -1

def lettre (etat,aphabet,nombre_epsilon,lines):
    tab=[]
    for i in range(0,nombre_epsilon):
        tab.append([])
    n=0
    i=1
    for ligne in lines:
        if i>=6:
            if etat==int(ligne[0]):
                link= lien(ligne[1], aphabet,nombre_epsilon)
                tab[link].append(ligne[2])
        i=i+1

        return tab


l=['E/S','Etats']
x=0
y=0
z=0

l1=[]

def var_lien (nombre_initial,etat_initial, nombre_final, etat_final,nombre_etat, nombre_epsilon, lines):
    temp=1
    true=0

    for i in range (0,nombre_epsilon):
        l.append(alphabet[i])
    for ligne in lines:
        if temp>=6:
            l2=0
            while l2<0:
                if ligne[l2]=="*":
                    true=1
                l2=l2+1
        temp=temp+1

        if true==1:
            l.append("epsilon")
            nombre_epsilon=nombre_epsilon+1
        l1.append(0,nombre_etat)

        for j in range (0,nombre_etat):
            l2=[]
            l2.append(entree_sortie(j,nombre_initial,nombre_final,etat_initial,etat_final))
            l2.append(j)

            for h in range (0,len(lettre(j,alphabet, nombre_epsilon,lines))):
                l2.append(lettre(j,alphabet,nombre_epsilon)[h])

            l1.append(l2)
        #print_var_lien(l1)

def afficher_lien(l1):
    print(tabulate(l1))



