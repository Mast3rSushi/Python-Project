"""
 suite_bizarre.py
 Auteur : Kiekens Romain
 Rôle : Détermine les n premiers nombres positifs impairs
 Saisies : Saisir le nombre de nombre premier positif impairs à afficher
 Résultat : Affiche les n premiers nombres positifs impairs
"""
n = int(input("Rentrer le nombre de nombre premier positif impairs à afficher : ")) #Saisir une valeur

for i in range(n*2) : #Pour tout i dans n multiplié par 2 faire la suite
    if i >= 1 : #SI i est supérieur ou égal à 1 alors faire la suite
        for m in range(1,i) : #Pour tout m dans i 
            if (i % m) ==0 and (i % 2) ==0 :
                break
                
            #Si la division euclidienne de i par m est égal à 0 et que la division euclidienne de i par 2 est égal à 0 alors casser la boucle
            if i%3 == 0 :
                break
            #Si la division euclidienne de i par 3 est égal à 0 alors casser la boucle
        else :
        
            print(i)
            #Sinon afficher i