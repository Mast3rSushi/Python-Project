"""
 jour.py
 Auteur : Kiekens Romain
 Rôle : Détermine la date du lendemain d'un jour donné'
 Saisies : Saisir le jour, le mois et l'année'
 Résultat : Affiche la date du lendemain
"""
j = int(input("Saisir le jours : "))    #Demande de saisir un jour
m = int(input("Saisir le mois :"))      #Demande de saisir un mois
a = int(input("Saisir l'année :"))      #Demande de saisir un mois

if m in (4,6,9,11):     #Si le mois choisi est égal à 4,6,9 ou 11 alors faire la suite
    if j == 30 :        
        j = 1
        l = j           #Si le jour est égal à 30 alors remettre le jour à 1
        if m == 12 :
            m = 1
            a = a + 1
            p = m
            e = a   #Si le mois est égal à 12 alors mettre le mois à 1, l'année à l'année choisi plus 1
        else :
            m = m + 1
            p= m
            l=j
            e=a     #Sinon mettre le mois au mois choisi plus 1
    elif j!=30 :
        l = j+ 1
        p = m
        e = a       #Sinon si le jour est différent de 30 alors mettre le jour au jour choisi plus 1
elif m in (1,3,5,7,8,10,12) :   #Sinon si le mois est égal à 1,3,5,7,8,10 et 12 alors faire la suite
    if j == 31 :
        j = 1
        l = j
        #Si le jour est égal à 31 alors remettre le jour à 1
        if m == 12 :
            m = 1
            a = a + 1
            p = m
            e = a    #Si le mois est égal à 12 alors mettre le mois à 1, l'année à l'année choisi plus 1
        else :
            m = m + 1
            p= m
            l=j
            e=a      #Sinon mettre le mois au mois choisi plus 1
    else :
        l = j+ 1
        p = m
        e = a       #Sinon mettre le jour au jour choisi plus 1
elif m == 2 :       #Sinon si le mois est égal à 2 alors faire la suite
    if (a%4==0 and a%100!=0 or a%400==0) and j <=28:
        
            j = j +1
            l = j
            p = m
            e =a 
            #Si l'année est une année bisextile et que le jour est inférieur ou égal à 28 alors mettre le jour au jour choisi plus 1
    elif (a%4!=0 and a%100==0 or a%400!=0) and j ==28 :
        j=1
        l=j
        p = m+1
        e = a
        #Sinon si l'année n'est pas une année bisextile et que le jour est égal à 28 alors le jour se met à 1 et on passe au mois suivant
    elif (a%4==0 and a%100!=0 or a%400==0) and j ==29:
        j= 1
        l=j
        p=m+1
        e=a
    #Sinon si l'année est une année bisextile et que le jour est égal à 29 alors le jour se met à 1 et on passe au mois suivant  
   
if m==2 and (a%4!=0 and a%100==0 or a%400!=0) and j>=29 :
    print("Cette date n'existe pas. Impossible de donner le lendemain. Veiller à rentrer une date valide !")    #Si le mois est égal à 2 et que l'année n'est pas bisextile et que le jour est supérieur ou égal à 29 alors afficher une erreur
elif j >= 31 or m >= 12 :
    print("Cette date n'existe pas. Impossible de donner le lendemain. Veiller à rentrer une date valide !") #Sinon si le jour est strictement supérieur à 31 ou que le mois est strictement supérieur à 12 alors afficher une erreur
elif j == 31 and m in(4,6,9,11) : 
    print("Cette date n'existe pas. Impossible de donner le lendemain. Veiller à rentrer une date valide !") #Sinon si le jour est égal à 31 et que le mois est égal à 4,6,9 ou 11 alors afficher une erreur
else :         
    print("J+1 : ",l,p,e) #Sinon afficher le lendemain de la date rentré 