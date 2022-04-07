# -*- coding: utf-8 -*-
"""
TK_figure.py 
Auteur : Kikens Romain 
Role : Figure triangle et pyramide 
  Entree :  
  Sortie : 2 triangles et un pyramide
Résultat : Affiche les figures
  
  
   
"""

# importe le module graphique TK
from tkinter import Tk,Canvas
 
hauteur = int(input("Saisir la hauteur de la figure : ")) 
if hauteur > 10 :
    print("La hauteur ne peut pas dépasser 10")
else :  
# Creation d'une fenêtre
    fen = Tk()
 
    yDim=500
    xDim=500

# Creation d'un canvas (tableau ou toile pour le dessin)
#  fen :  fenetre attachée
#  height width   hauteur et largeur du Canvas en pixels (point)
    can = Canvas(fen, height=yDim, width=xDim)

    lg = 10
    base = hauteur
    
    for i in range(hauteur) :  #Pour tout i dans hauteur faire la suite
        can.create_rectangle(xDim/2 ,yDim/2, xDim/2 + lg , yDim/2 -lg , fill='blue')
        yDim = yDim + 24
    #Crée un rectangle et changer les valeurs en y
    
    for i in range(hauteur) :   #Pour tout i dans hauteur faire la suite
        can.create_rectangle(xDim/2 ,yDim/2 , xDim/2 + lg , yDim/2 -lg , fill='blue')
        xDim = xDim +24
    #Crée un rectangle et changer les valeurs en x 
    
    for i in range(hauteur-2):  #Pour tout i dans hauteur faire la suite moins 2
        can.create_rectangle(xDim/2 - 108 ,yDim/2 - 22  , xDim/2  + lg -108  , (yDim/2 ) -lg -2   , fill='blue')
        xDim = xDim +24
    #Crée un rectangle et changer les valeurs en x
    
    for i in range(hauteur - 1):    #Pour tout i dans hauteur faire la suite moins 1
        can.create_rectangle(xDim/2 - 204 ,yDim/2 - 22  , xDim/2  + lg -204  , (yDim/2 ) -lg -2   , fill='blue')
        yDim = yDim - 24
    #Crée un rectangle et changer les valeurs en y
    
    for i in range(hauteur - 4) :   #Pour tout i dans hauteur faire la suite moins 4
        can.create_rectangle(xDim/2 - 192 ,yDim/2 + 84  , xDim/2  + lg -192  , (yDim/2 ) -lg +84   , fill='blue')
        xDim = xDim +24
    #Crée un rectangle et changer les valeurs en x    
        
    for i in range (hauteur - 3) : #Pour tout i dans hauteur faire la suite moins 3
        can.create_rectangle(xDim/2 - 264 ,yDim/2 + 84  , xDim/2  + lg -264  , (yDim/2 ) -lg +84   , fill='blue')
        yDim = yDim  -24
    #Crée un rectangle et changer les valeurs en y    
        
    for i in range (hauteur - 5):   #Pour tout i dans hauteur faire la suite moins 5
        can.create_rectangle(xDim/2 - 264 ,yDim/2 + 156  , xDim/2  + lg -264  , (yDim/2 ) -lg +156   , fill='blue')      
        xDim = xDim + 24
    #Crée un rectangle et changer les valeurs en x    
        
    for i in range(hauteur - 4):    #Pour tout i dans hauteur faire la suite moins 4
        can.create_rectangle(xDim/2 - 324 ,yDim/2 + 156  , xDim/2  + lg -324  , (yDim/2 ) -lg +156   , fill='blue')
        yDim = yDim -24
    #Crée un rectangle et changer les valeurs en y    
        
    for i in range(hauteur - 6):    #Pour tout i dans hauteur faire la suite moins 6
        can.create_rectangle(xDim/2 - 324 ,yDim/2 + 216  , xDim/2  + lg -324  , (yDim/2 ) -lg +216   , fill='blue')
        xDim = xDim +24
     #Crée un rectangle et changer les valeurs en x   
        
    for i in range(hauteur - 6):    #Pour tout i dans hauteur faire la suite moins 6
        can.create_rectangle(xDim/2 - 360 ,yDim/2 + 216  , xDim/2  + lg -360  , (yDim/2 ) -lg +216   , fill='blue')
        yDim = yDim -24
    #Crée un rectangle et changer les valeurs en y    
        
    for i in range(hauteur - 8):    #Pour tout i dans hauteur faire la suite moins 8
        can.create_rectangle(xDim/2 -348 ,yDim/2 + 252  , xDim/2  + lg -348  , (yDim/2 ) -lg +252   , fill='blue')
        yDim = yDim -24
    #Crée un rectangle et changer les valeurs en y    
        

# on adapte la fenetre principale au dessin 
    can.pack()

#lance TK et affiche la fenêtre
    fen.mainloop()
