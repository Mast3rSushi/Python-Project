
"""
         note.py
         Auteur : Kiekens Romain
  	    Rôle : Calcul la moyenne de l'UE'
  	    Saisies : Saisir la note de contrôle continu (CC) et la note de contrôle terminal (CT)
  	    Résultat : Affiche la note finale à l'UE'

 
"""
CC = float(input("Saisir la note de contrôle continu : "))  #Demande la note du contrôle continu
CT = float(input("Saisir la note de contrôle terminal : ")) #Demande la note du contrôle terminal

sup = 2/3*CT+1/3*CC     #Calcul de la moyenne de l'UE pour la première session

print("Note première session : ",sup) #Affiche la moyenne de la première session


if sup < 10 :   #Si la moyenne de la première session est inférieur à 10 alors faire la suite 
    CT2 = float(input("Saisir la note de la deuxième session : "))  #Demande la note de la deuxième session
    sup2 = 2/3*CT2+1/3*CC   #Calcul la moyenne de l'UE pour la deuxième session
    print("Note à l'issue de la deuxième session : ",sup2)  #Affiche la moyenne de la deuxième session