"""
 suite.py
 Auteur : Kiekens Romain
 Rôle : Détermine l’élément le plus grand et l’élément le plus petit d’une suite d’entiers positifs
 Saisies : Saisir la valeur d'un entier A et d'un entier B
 Résultat : Affiche le plus grand et le plus petit élément d'une suite d'entiers positifs
""" 
a = int(input("Saisir un entier positif : "))
b= 0
c= 0
ab = 1
while ab != 0 :
    b = a
    mina = b
    ab = int(input("Saisir un entier positif : "))
    if b < ab:
        c = ab
        mina = b
        maxa = c
        
    else :
        c = b
        maxa = ab
        mina = c
        
   
print(ab,b)
        
   
