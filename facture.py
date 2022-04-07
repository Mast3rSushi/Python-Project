"""
 facture.py
 Auteur : Kiekens Romain
 Rôle : Réalise la facture d'un produit donné'
 Saisies : Saisir le nom du produit, sa quantité et son prix
 Résultat : affiche la facture du produit donné
"""

produit = input("Rentrer le nom du produit :")  #Demande le nom du produit
quantité = int(input("Rentrer la quantité du produit voulu :")) #Demande le nombre de produits
prix = float(input("Rentrer le prix du produit :")) #Demande le prix du produit
TVA = 0.2 #Variable contenant la TVA actuelle (20%)

pst = quantité*prix     #Prix sans TVA en fonction du nombre de produits
jtva = pst*TVA          #Prix de la TVA des produits          
pat = pst + jtva        #Prix des produits avec la TVA

print("-------------Facture-------------")
print("Produit   :",produit)
print("Quantité  :",quantité)
print("Prix ht   :",prix,"euros")
print("Total ht  :",pst,"euros")
print("Taux TVA  :",TVA)
print("Total TVA :",jtva,"euros")
print("Total TTC :",pat,"euros")
print("---------------------------------")  
#Affiche la facture du ou des produits