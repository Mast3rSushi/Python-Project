"""
 lastchancegas.py
 Auteur : Kiekens Romain
 Rôle : Dire s'il faut reprendre de l'essence 
 Saisies : Saisir la capacité du réervoir, L’indication de la jauge d’essence en pourcentage et la consommation par kilomètre
 Résultat : Affiche s'il faut reprendre de l'essence ou non
"""
cdr= float(input("Rentrer la capacité du réservoir :")) #Demande la capacité du réservoir en litres
pe= float(input("Rentrer le pourcentage actuel de la jauge d'essence restant :"))   #Demande le pourcentage actuel de la jauge d'essence restant
conso= float(input("Rentrer le nombre de km par litre d'essence cosommé :"))    #Demande la consommation en km par litre

l_restant = cdr*(pe/100) #Calcule les litres d'essences restants 
km_restant = l_restant*conso #Calcule le nombre de kilomètre restant
print(km_restant)

if km_restant <= 350 :
    print("Reprenez de l'essence ! ")
else :
    print("Foncez !")
#Affiche le premier résultat si la condition est remplie sinon cela affiche le deuxième résultat