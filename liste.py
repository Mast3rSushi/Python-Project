"""
 liste.py
 Auteur : Kiekens Romain
 Rôle : Détermine une saisie de liste, un affichage, une moyenne et un écart type d'une liste'
 Saisies : Saisir les éléments de la liste
 Résultat : Affiche la liste, sa moyenne et son écart type'
"""
from math import sqrt  #Importe la fonction racine carré

def saisie_liste() :
    liste = []  #Liste vide
    n = int(input("Saisir la taille de la liste : "))   #Variable contenant une valeur à saisir
    for i in range(n) : #Pour tout lles élément de n saisir un élément m qui sera ajouté à la liste
        m = int(input("Saisir un élément : "))
        liste.append(m)
    return(liste) #Retourner la liste

def affiche_liste(liste):
    
    for i in liste :
        print(i)
    return(liste) #Pour tout les éléments de la liste, les afficher

def moyenne_liste(liste):
    
    a = 0
    for i in liste:
        a+= i
    moyenne = a/len(liste)  
    return(moyenne) #Pour tout les éléments de la liste, faire la somme puis la moyenne de celle-ci

def ecart_type(liste):
    
    a = 0
    for i in liste : #Pour tout les éléments de la liste, faire la suite
        a = a + ((i - moyenne_liste(liste)))**2     #Calcul de la somme des éléments de la liste moins la moyenne de la liste au carré
    a = a/len(liste) #Calcul de la moyenne
    a = sqrt(a)     #Calcul de la racine carré de la moyenne
    return(a)   #Retourner a 

list = saisie_liste()
print("Element(s) de la liste : ")
affiche_liste(list)
print("Moyenne des elements de la liste :",moyenne_liste(list))
print("écart-type des éléments de la liste",ecart_type(list))