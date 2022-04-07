"""
 Somme_argent.py
 Auteur : Kiekens Romain
 Rôle : Détermine la décomposition d'une somme d'argent en billets et en pièces
 Saisies : Saisir la somme à décomposer
 Résultat : Affiche la décomposition de la somme d'argent rentré'
"""


def décomposition1() :
    decom = [100, 50, 20, 10, 5, 2, 1] #Liste de valeur
    somme = int(input("Entrer la somme à convertir : ")) #Variable contenant une somme à convertir
    a = 0 #Variable contenant 0
    b = 0   #Variable contenant 0
    c = 0   #Variable contenant 0
    d = 0   #Variable contenant 0
    e = 0   #Variable contenant 0
    f = 0   #Variable contenant 0
    g = 0   #Variable contenant 0
    while somme !=0 :
        if somme >= decom[0] :
            somme = somme - decom[0]
            a = a +1 
        elif somme >= decom[1] :
            somme = somme - decom[1]
            b = b+1
        elif somme >= decom[2] :
            somme = somme - decom[2]
            c = c+1
        elif somme >=  decom[3]:
            somme = somme - decom[3]
            d = d+1
        elif somme >= decom[4] :
            somme = somme - decom[4]
            e = e+1
        elif somme >= decom[5] :
            somme = somme - decom[5]
            f = f+1
        elif somme >= decom[6] :
            somme = somme - decom[6]
            g = g+1
    #Tant que la somme est différente de 0 alors enlever le nombre corespondant si celui si est inférieur ou égal à la somme et le stocker dans une variable
    print("Décomposition :", a ,"*100 + ", b ,"*50 + " , c ,"*20 + ", d ,"*10 + ",e,"*5 + ", f,"*2 + ",g ,"*1")
        
def décomposition2() :
    billet = [100, 50, 10, 5] #Liste de valeur
    somme = int(input("Entrer la somme à convertir : ")) #Variable contenant une somme à convertir
    res ="" #Chaine de caractère
    il = 0    
    for i in billet : #Pour tout les élément de billet
        while somme >= i :
            somme -= i 
            il += 1 #Tant que la somme est supérieur ou égal à i alors soustraire l'élément corespondant de la somme et la stocker dans une variable
        res = res +(str(i)+"*"+str(il)+" + ") #Chaine de caractère contenant les valeurs stockés avec leur élément corespondant de la liste billet
        il = 0
    res = res + ("reste : "+" "+str(somme)) #Chaine de caractères contenant le reste de la somme qui n'a pas pu être décomposé
    return res