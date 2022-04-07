"""
 moyenne.py
 Auteur : Kiekens Romain
 Rôle : Réalise la moyenne de 5 notes
 Saisies : Saisir 5 notes
 Résultat : affiche la moyenne des 5 notes
"""
N=float(input("Rentrer une valeur :")), float(input("Rentrer une valeur :")),float(input("Rentrer une valeur :")),float(input("Rentrer une valeur :")),float(input("Rentrer une valeur :")) #Variable qui demande de rentrer 5 valeurs
C= N[0] +N[1]+N[2]+N[3]+N[4]    #Variable qui calcule la somme des 5 valeurs
M= C/len(N) #Varaible qui calcule la moyenne des 5 valeurs
print('La moyenne est :',M) #Affiche la moyenne des 5 valeurs 
