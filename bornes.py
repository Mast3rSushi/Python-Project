"""
 bornes.py
 Auteur : Kiekens Romain
 Rôle : Détermine la suite de chiffres entre deux entiers
 Saisies : Saisir la valeur d'un entier A et d'un entier B
 Résultat : Affiche la suite de nombres entre ces deux entiers
"""
a = int(input("Saisir A : ")) #Rentrer la valeur de A
b = int(input("Saisir B : ")) #Rentrer la valeur de B

if a - b > 20 or b-a > 20 : 
    print("La différence entre a et b ne doit pas dépasser 20") 
#Si a - b est strictement supérieur à 20 ou que b-a est strictement supérieur à 20 alors afficher une erreur

else :
    print(a) #Afficher a
    while a != b : #Tant que a est différent de b alors faire la suite
        if a >b :
            
            a = a-1
            print(a)
            #Si a est strictement inférieur à b alors a est égal à a - 1 et afficher a
        else :
            
            a = a+1
            print(a)
            #Sinon a est égal à a -1 et afficher a 