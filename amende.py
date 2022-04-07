"""
 amende.py
 Auteur : Kiekens Romain
 Rôle : Détermine le montant d'une amende pour excès de vitesse'
 Saisies : Saisir la vitesse réelle, la vitesse autorisée, infraction en ville et infraction en zone limitée
 Résultat : Affiche l'amende à payer '
"""

vitm = int(input("Saisir la vitesse réelle : "))    #Demande de saisir la vitesse du véhicule
vita =int(input("Saisir la vitesse autorisée : "))  #Demande la vitesse autorisé
infractv = input("Infraction en ville Oui / Non : ")    #Demande si c'est une infraction en ville
infractz = input("Infraction en zone limitée à 50 km/h Oui / Non : ")   #Demande si c'est une infraction dans une zone à 50km/h
ex = vitm - vita #Varible contenant le calcul de l'excès de vitesse (20km/h de plus par exemple)
p = 20  #Variable contenant une limite d'excès de vitesse
b = 50  #Variable contenant une limite d'excès de vitesse
a =60   #Variable contenant une limite d'excès de vitesse

if vitm > vita and ex < p :    #Si la vitesse du véhicule est  strictement supérieur à celle autorisé et que l'excès de vitesse est strictement inférieur à 20km/h  alors faire la suite
    if infractv == "oui" or infractv =="oui" :
        print("Amende de 90 euros")     #Si c'est une infraction produite dans une ville ou dans une zone limitée alors afficher l'amende à payer
    else :
        print("Amende de 45 euros") #Sinon afficher l'autre amende à payer


elif vitm > vita and p < ex < b : 

        print("Amende de 90 euros") #Sinon si la vitesse du véhicule est  strictement supérieur à celle autorisé et que l'excès de vitesse est entre 20km/h et 50km/h alors afficher l'amende à payer

elif vitm > vita and b <= ex :

        print("Amende de 1500 euros") #Sinon si la vitesse du véhicule est supérieur ou égal à celle autorisé et que l'excès de vitesse est supérieur ou égal à 50km/h alors afficher l'amende à payer
    
else :
    print("Pas d'amende") #Sinon afficher qu'il n'y a pas d'amende à payer
    
##################################################################################    
#Saisir la vitesse réelle : 90

#Saisir la vitesse autorisée : 80

#Infraction en ville Oui / Non : oui

#Infraction en zone limitée à 50 km/h Oui / Non : non
#Amende de 90 euros
##################################################################################

##################################################################################
#Saisir la vitesse réelle : 90

#Saisir la vitesse autorisée : 110

#Infraction en ville Oui / Non : oui

#Infraction en zone limitée à 50 km/h Oui / Non : non
#Pas d'amende
##################################################################################

##################################################################################
#Saisir la vitesse réelle : 130

#Saisir la vitesse autorisée : 90

#Infraction en ville Oui / Non : non

#Infraction en zone limitée à 50 km/h Oui / Non : oui
#Amende de 90 euros
###################################################################################

###################################################################################
#Saisir la vitesse réelle : 150

#Saisir la vitesse autorisée : 50

#Infraction en ville Oui / Non : non

#Infraction en zone limitée à 50 km/h Oui / Non : non
#Amende de 1500 euros
###################################################################################

###################################################################################
#Saisir la vitesse réelle : 90

#Saisir la vitesse autorisée : 80

#Infraction en ville Oui / Non : non

#Infraction en zone limitée à 50 km/h Oui / Non : non
#Amende de 45 euros
####################################################################################