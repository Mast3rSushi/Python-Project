"""
 suite2.py
 Auteur : Kiekens Romain
 Rôle : Détermine l'élément le plus petit et le plus grand d'une suite
 Saisies : Saisir des entiers positifs
 Résultat : Affiche l'élément le plus petit et le plus grand d'une suite d'entier positif'
"""
a =[] #Liste vide
b = int(input("Saisir un entier positif : "))   #Saisir un entier positif
a.append(b) #Ajouter l'entier positif à la liste
while b !=0 :   
    b = int(input("Saisir un entier positif : "))
    a.append(b) 
    #Tant que b est différent de 0 alors saisir un un autre entier et l'ajouter à la liste
del a[-1] # Supprimer le dernier élément de la liste
if len(a) == 0 :
    print("Il n'y a pas assez d'éléments dans cette suite pour pouvoir trouver un minimum et un maximum")
#SI le nombre d'entier de la liste est égal à 0 alors afficher une erreur
else :
    print(min(a),max(a))
    #Sinon afficher la valeur minimal et la valeur maximale de la liste