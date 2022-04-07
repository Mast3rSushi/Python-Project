"""
 Loi_concentrée.py
 Auteur : Kiekens Romain
 Rôle : Détermine la densité d'une population'
 Saisies : Saisir t
 Résultat : Affiche la densité d'une population d'une variable t
"""
from math import sqrt,exp,pi    #Importe les fonctions racine carrée, exponentielle et pi
 
t = int(input("Rentrer la valeur de t : "))     #Demande de rentrer une valeur

densité = (1/(sqrt(2*pi)))*exp(-t*t/2)          #Calcul de la densité de la population

print("densité : ",densité)     #Affiche la densité