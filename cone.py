"""
 cone.py
 Auteur : Kiekens Romain
 Rôle : Calcul le volume d'un cône'
 Saisies : Saisir la hauteur et le rayon du cône
 Résultat : Affiche le volume du cône
"""

rayon = float(input("Rentrer le rayon du cône :"))  #Demande de rentrer le rayon du cône 
hauteur = float(input("Rentrer la hauteur du cône :"))  #Demande de rentrer la hauteur du cône
PI = 3.14159    #Variable contenant une valeur approché de Pi
volume = 1/3*PI*rayon**2*hauteur    #Calcul du volume du cône

print("Calcul du volume d'un cône :")   
print("Le rayon est :",rayon)
print("La hauteur est :",hauteur)
print("Le volume du cône est :",volume,"cm³")
#Affiche le rayon, la hauteur et le volume du cône