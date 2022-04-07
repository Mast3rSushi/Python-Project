"""
 Loi_concentrée.py
 Auteur : Kiekens Romain
 Rôle : Détermine la densité d'une population'
 Saisies : Saisir t
 Résultat : Affiche la densité d'une population d'une variable t
"""
from math import sqrt,exp,pi     #Importe les fonctions racine carrée, exponentielle et pi

def densité(t):     #Fonction de la densité
    f = (1/(sqrt(2*pi)))*exp(-t*t/2)    #Calcul de la densité
    return(f)   #Retourne le résultat du calcul de la densité