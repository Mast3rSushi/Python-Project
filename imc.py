"""
 imc.py
 Auteur : Kiekens Romain
 Rôle : Réalise l'imc d'une personne
 Saisies : Saisir le poids et la taille de la personne
 Résultat : affiche l'imc d'une personne
"""

taille = float(input("Rentrer la taille de la personne :"))     #Demande la taille de la personne
kg = float(input("Rentrer le poids de la personne :"))      #Demande le poids de la personne 

imc = round(kg/taille**2,4)         #Calcule l'imc d'une personne en fonction du poids et de la taille de la personne

print("Indice de masse corporelle")
print("Poids :",kg,"kg")
print("Taille :",taille,"m")
print("IMC :",imc)
#Affiche le poids, la taille et l'imc d'une personne