"""
 Factorielle_arrangement.py
 Auteur : Kiekens Romain
 Rôle : Détermine le factorielle ou l'arrangement'
 Saisies : Saisir les fonctions, n et p
 Résultat : Affiche le factorielle ou l'arrangement des variables n et p 
"""
def fac(n) :    #Fonction du factorielle
    if n <0 :
        print("n doit être positif") #Si n est strictement supérieur à 0 alors affiche une erreur
    else : #Sinon faire la suite
        fact = 1    #Variable contenant 1
        for i in range(1,n+1):  #Pour tout i dans 1 à n+1
           fact = fact*i #Calcul du factorielle
        
        return(fact) #Retourne le résultat du factorielle
    
def arrangement(n,p) :      #Fonction de l'arrangement
    ar = fac(n)/fac(n-p)    #Calcul de l'arrangement avec le factorielle
    return(ar)      #Retourne le résultat de l'arrangement