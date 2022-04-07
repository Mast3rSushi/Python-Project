"""
 conjecture_de_syracuse.py
 Auteur : Kiekens Romain
 Rôle : Détermine la conjecture de syracuse'
 Saisies : Saisir les fonctions et n
 Résultat : Affiche la conjecture de syracuse de l'entier n'
"""

def syracuse(n) :   #Fonction de la syracuse
    
    print(n)    #Affiche n
    while n != 1 :  #Tant que n est différent de 1
        
       
        if n%2 == 0 : #Si n est paire alors
            n= n/2    #La valeur de n change
            print(n)  #Afficher n
           
        else :
            n = 3*n+1 #Sinon n prend une autre valeur
            print(n)    #Afficher n
            
    
    return(syracuse)    #Retourne la fonction syracuse

def syracuse2(n) :      #Fonction du nombre de saut de la syracuse
   
    a=0     #Variable contenant le nombre de saut
    while n != 1 :  #Tant que n est différent de 1 alors faire la suite
        
       
        if n%2 == 0 :
            n= n/2
            
            a=a+1   #Si n est paire alors changer la valeur de n et de a
        else :
            n = 3*n+1
            
            a=a+1   #Sinon changer n par une autre valeur et ajouter un saut

    return(a)   #Retourner la valeur de a

def syracuse3(n) :  #Fonction du nombre moyen de saut 
   
    a=0     #Variable contenant le nombre de saut
    e=n     #Variable contenant la valeur de base de n
    while n != 1 :  #Tant que n est différent de 1 alors faire la suite
        
       
        if n%2 == 0 :    
            n= n/2
            
            a=a+1 #Si n est paire alors changer la valeur de n et de a
        else :
            n = 3*n+1
            
            a=a+1 #Sinon mettre une autre valeur à a et n
    b = e/a #Calcul de la moyenne de sauts
    return(b) #Retourne le résultat de la moyenne de sauts


def temps_de_vol(n) : #fonction du nombre de saut de la 
    
    m = syracuse2(n)    #calcul du nombre de saut
    return(m)   #Retourne le nombre de sauts

def temps_de_vol_moyen(n):  #Fonction du nombre moyen de saut 
    
    m = syracuse3(n)    #Calcul du nombre moyen de saut
    return(m)   #Retourne le résultat du calcul du nombre de saut moyen
 