"""
 Marche.py
 Auteur : Kiekens Romain
 Rôle : Passe une commande sur internet
 Saisies : Saisir le nom du produit, son prix, l'envoie express et le code secret'
 Résultat : Affiche le cout total de la commande 
"""
print("Saisie de votre commande :") #Affiche le message
produit = input("Rentrer le nom du produit :") #Demande le nom du produit 
prix = float(input("Rentrer le prix du produit :")) #Demande le prix du produit
code_secret = input("Rentrer le code secret si vous en disposez d'un :") #Demande le code produit
envoie_express = input("Rentrer yes ou no si vous voulez une commande express :") #Demande si vous voulez une livraison express

MONTANT = 100  #Variable contenant un montant
ENVOIE1 = 10    #Variable contenant un montant d'envoie de commande
ENVOIE2 = 16    #Variable contenant un montant d'envoie de commande
SOLDES = 0.03   #Variable contenant un montant de solde

print("Récapitulatif de la commande :") #Affiche le résultat   
if envoie_express == "yes" :    #Si il y a un envoie express alors faire la suite
    if prix <= 100 :            #Si le prix de la commande est en dessous ou égal à 100 euros alors faire la suite
        fe=ENVOIE1 + 10         #Calcul les frais d'envoies de la commande 
        if code_secret == "soldes":     #Si il y a un code secret alors faire la suite 
            pp = prix-prix*SOLDES       #Calcul le prix du produit avec les soldes
            cout_total = pp + fe        #Calcul le cout total de la commande
            print(produit, pp)          #Affiche le nom du produit avec son prix total
            print("Frai d'envoi :",fe)  #Affiche les frais d'envoies de la commande
        else :
            cout_total = prix + fe      #Calcul le cout total de la commande si le code secret n'est pas valide
            print(produit, prix)        #Affiche le nom du produit avec son prix total
            print("Frai d'envoi :",fe)  #Affiche les frais d'envoies de la commande
    else :
        fe= ENVOIE2 +10         #Calcul les frais d'envoies de la commande si celle-ci est supérieur à 100 euros
        if code_secret == "soldes":      #Si il y a un code secret alors faire la suite 
            pp = prix-prix*SOLDES        #Calcul le prix du produit avec les soldes
            cout_total = pp + fe         #Calcul le cout total de la commande
            print(produit, pp)           #Affiche le nom du produit avec son prix total
            print("Frai d'envoi :",fe)       #Affiche les frais d'envoies de la commande
        else :
            cout_total = prix + fe           #Calcul le cout total de la commande si le code secret n'est pas valide
            print(produit, prix)             #Affiche le nom du produit avec son prix total
            print("Frai d'envoi :",fe)      #Affiche les frais d'envoies de la commande
        
elif envoie_express == "no" :           #Sinon si il n'y a pas d'envoi express alors faire la suite
    if prix <= 100 :                    #Si le prix de la commande est en dessous ou égal à 100 euros alors faire la suite
        fe=ENVOIE1                      #Calcul les frais d'envois de la commande
        if code_secret == "soldes":     #Si il y a un code secret alors faire la suite
            pp = prix-prix*SOLDES       #Calcul le prix du produit avec les soldes
            cout_total = pp + fe         #Calcul le cout total de la commande
            print(produit, pp)           #Affiche le nom du produit avec son prix total
            print("Frai d'envoi :",fe)   #Affiche les frais d'envoies de la commande
        else :
            cout_total = prix + fe       #Calcul le cout total de la commande si le code secret n'est pas valide
            print(produit, prix)         #Affiche le nom du produit avec son prix total
            print("Frai d'envoi :",fe)   #Affiche les frais d'envoies de la commande
        
    else :
        fe=ENVOIE2              #Calcul les frais d'envoies de la commande si celle-ci est supérieur à 100 euros
        if code_secret == "soldes":      #Si il y a un code secret alors faire la suite
            pp = prix-prix*SOLDES        #Calcul le prix du produit avec les soldes
            cout_total = pp + fe         #Calcul le cout total de la commande
            print(produit, pp)           #Affiche le nom du produit avec son prix total
            print("Frai d'envoi :",fe)  #Affiche les frais d'envoies de la commande
        else :
            cout_total = prix + fe      #Calcul le cout total de la commande si le code secret n'est pas valide
            print(produit, prix)        #Affiche le nom du produit avec son prix total
            print("Frai d'envoi :",fe)   #Affiche les frais d'envoies de la commande


print("Cout total :",cout_total)    #Affiche le cout total de la commande 