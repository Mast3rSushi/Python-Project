"""
 concert.py
 Auteur : Kiekens Romain
 Rôle : Calcul le tarif d'une place de concert'
 Saisies : Saisir le tarif de base, l'âge et la réservation par internet'
 Résultat : Affiche le cout total de la place de concert 
"""
tarif = float(input("Saisir le tarif de base : "))  #Demande de rentrer le tarif basique de la place
age = float(input("Votre âge : "))   #Demande l'âge de la personne
internet = input("Réservation par internet oui/non : ")     #Demande si la personne a commandé sur internet
reduc1 = 0.3    #Variable contenant une réduction de 30%
reduc2 =0.2     #Variable contenant une réduction de 20%
reduci = 0.05   #Variable contenant une réduction de 5%
re=0            #Variable contenant le prix de la réduction en fonction de l'âge
prix = tarif    #Variable contenant le tarif de la place

if age < 14 :
    prix = tarif - tarif
    re=tarif
#Si l'âge d ela personne est strictement inférieur à 14 alors le prix de la place est égal à 0 et la réduction de la place est le prix de la place
  
elif age < 18 or age > 70 :
    re = tarif*reduc1
    prix = tarif - re
#Sinon si l'âge de la personne est strictement inférieur à 18 ou strictement supérieur à 70 alors la réduction est le prix de la place fois la réduction de 30%
#Le prix de la place est donc le prix de base moins la réduction
   
elif  age < 25 :
    re = tarif*reduc2
    prix = tarif -re
#Sinon si l'âge de la personne est strictement inférieur à 25 alors la réduction est le pmrix de la place fois la réduction de 20 %
#Le prix de la place est égale au tarif moins la réduction de l'âge
print("Réduction en fonction de l'âge : ", re)  #Affiche la réduction en fonction de l'âge
if internet == "oui" and prix > 0 :
    ri =   prix*reduci
    prix = prix - ri
    print("Réduction résa Internet : ",ri)
#Si la place a été commandé sur internet alors on ajoute une réduction de 5% au prix total de la place avec les autres réductions si il en a eu    
    
print("Prix de la place :",prix) #Affiche le prix total de la place de concert
