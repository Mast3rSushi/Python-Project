
"""
         heure.py
         Auteur : Kiekens Romain
  	    Rôle : Convertir les secondes en heures, minutes et secondes
  	    Saisies : Saisir le nombre de secondes
  	    Résultat : Affiche les secondes sous forme d'heures, minutes et secondes'

 
"""

sec=float(input("Saisir le nombre de secondes :"))  #Variable contenant une saisie pour de secondes 
H = 0   #Variable contenant 0 heure
M=0     #Variable contenant 0 minute
S=0     #Variable contenant 0 seconde
while sec >= 3600 :      #Tant que le nombre de secondes est supérieur ou égal à 3600, faire la suite
    H= H+1      #Variable contenant le nombre d'heures qui augmente tant que la condition n'est pas rempli
    sec = sec -3600     #Variable contenant le nombre de secondes total qui diminue tant que la condtion n'est pas rempli
while sec >= 60 :   #Tant que le nombre de secondess est supérieur ou égal à 60, faire la suite
    M = M + 1       #Variable contenant le nombre de minutes qui augmente tant que la condition n'est pas rempli
    sec = sec -60   #Variable contenant le nombre de secondes total qui diminue tant que la condition n'est pas rempli
    S= sec          #Variable contenant le reste de secondes

if H==0 :       #Si le nombre d'heures est égal à 0, faire la suite
    print(M,"'",S,"''") #Affiche le résultat
elif S==0 :     #Sinon si le nombre de secondes est égal à 0, faire la suite
    print(H,"h",M,"'")  #Affiche le résultat
else :  #Sinon faire la suite
    print(H,"h",M,"'",S,"''")   #Affiche le résultat
    