"""
 bornes.py
 Auteur : Kiekens Romain
 Rôle : Détermine la suite de chiffres entre deux entiers
 Saisies : Saisir la valeur d'un entier A et d'un entier B
 Résultat : Affiche la suite de nombres entre ces deux entiers
"""
a = [] #Liste vide
b = int(input("Rentrer vos notes de TP : ")) #Saisir une valeur
a.append(b) #Ajouter à la liste la valeur saisie
if b == -1 :
    del a[-1]
#Si la valeur saisie est égal à -1 alors supprimer cette valeur de la liste
if b == 0 :
    print("La moyenne est de 0")
#Si la valeur saisie est égal à 0 alors afficher la moyenne
else :

    while b != -2 :
        b= int(input("Rentrer vos notes de TP : "))
        a.append(b)
        #Tant que la valeur saisie est différent de -2 alors rentrer une nouvelle valeur
        if b == 0 :
            print("La moyenne est de 0")
            break
        #Si la valeur saisie est égal à 0 alors afficher la moyenne et casser la boucle
   
        elif len(a)  < 4 and b ==-2 :
            print("Nombre de notes insuffisant")
        #Sinon si le nombre de valeur de la liste est strictement inférieur à 4 et que la valeur saisie est égal à 0 alors afficher une erreur
        
        elif b == -1 :
            del a[-1]
        #Sinon si la valeur saisie est égal à -1 alors supprimer cette valeur de la liste
    if b == -2 and len(a) >= 4 :        
        del a[-1]
        moy = sum(a)/len(a) #Calcul de la moyenne 
        print(moy)   
    #Si la valeur saisie est égal à -2 et que le nombre de valeur dans la liste est supérieur ou égal à 4 alors
    #Supprimer la dernière valeur de la liste et afficher la moyenne
    
        