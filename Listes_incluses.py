"""
 Listes_incluses.py
 Auteur : Kiekens Romain
 Rôle : Détermine si les éléments d'une liste sont tous dans une autre liste'
 Saisies : Acunes saisies
 Résultat : Affiche vrai si les éléments d'une liste sont tous dans une autre liste'
"""
def liste_incluse(li1,li2) :
    b =0
    for i in li1 : #Pourt tout les i dans la première liste
        a = i in li2 #Variable contenant les éléments de la deuxième liste
        if a == True :
            b = b+ 1 #Si les éléments sont égaux alors les compter dans une variable
        else :
            return False #Sinon retourner false
    if b == len(li1):
         return True #Si tout la variable est égal au nombre d'éléments de la première liste alors retourner vrai
            
       
