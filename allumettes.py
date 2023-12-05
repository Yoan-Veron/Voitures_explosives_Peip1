# -*- coding: utf-8 -*-
"""

@author: Yoan Veron
@author: Anaïs Lacouture

"""

from random import*
from dessin import*
import time


#Fonction pour le tour du joueur 
# a représente le nombre d'allumettes courantes 
# r représente la règle
def coup_joueur(a,r):
    j = numinput("Joueur","Combien de voitures retirez vous ? ")
    while j not in(r) or j > a :
        j = numinput("Joueur","Retirez un nombre de voiture permis par la regle et qu'il est possible de retirer dans le jeu : ") 
        
    return j


#Fonction pour le tour de l'ordinateur
# a représente le nombre d'allumettes courantes 
# r représente la règle
def coup_ordi(a,r):
    if a<min(r):
        gagner = False
    elif a>0 and a>=min(r):
        o=0
        i=0
        while a-o!=0 and i<len(r) and o<=a:
            o=r[i]
            i=i+1
        if a-o!=0:
            o=choice(r)
    return o



#Fonction pour redessiner les voitures et les remplacer après chaque coups
#l et h repésente la largeur et la hauteur de la fenetre 
#t1 et t2 sont des tortues 
# a représente le nombre d'allumettes courantes
def Maj(t1,t2,l,h,a):
    #On peut mettre en commentaire la ligne suivante pour avoir la voiture combinée à l'explosion est pas seulement l'explosion
    dessin(t1,l,h,a,"cache")
    dessin(t2, l, h, a,"flammes")
    update()
   

#l et h repésente la largeur et la hauteur de la fenetre 
#t est la tortue qui affiche le nombre d'allumettes courantes
# a représente le nombre d'allumettes courantes
def Maj_texte(t,n,l,h):
    t.clear()
    t.up()
    t.goto(-l/2 + 100,h/2 - 30)
    t.down()
    t.write(int(n),font=("arial",15,"normal"))
    update()


#Decor et initialisation des tortues
hideturtle()
tortue_decor = Turtle()
tortue_voiture = Turtle()
tortue_texte = Turtle()
tortue_cache = Turtle()
tortue_nombre = Turtle()
tortue_partie = Turtle()

tf = Turtle()
tf.hideturtle()

tortue_texte.hideturtle()
tortue_voiture.hideturtle()
tortue_decor.hideturtle()
tortue_cache.hideturtle()
tortue_nombre.hideturtle()
tortue_partie.hideturtle()


#On définit la taille de l'écran
setup(1440,720)
title("Explosion de voitures")

#On récupère la taille de l'écran
hauteur =  720
largeur = 1440


#Initialisation
partie = 1
continuer = True
score = 0


#Début du jeux
while continuer:
    
    #Mise en place du décor
    decor(tortue_decor, largeur, hauteur)
    
    feuligne(tf, 100, 50, largeur/2 -150 , hauteur/4 - 5)
        
    #Initialisation de la règle
    regle = [5,7,8]
    
    #Mise en place des voitures
    nb_voitures_depart = randrange(15,21)
    nb_voitures_courant = nb_voitures_depart
    dessin(tortue_voiture,largeur,hauteur,nb_voitures_depart,"voitures")
    
    #Initialisation partie
    gagner = False
    
    #Affiche nombre de voitures
    tortue_texte.up()
    tortue_texte.goto(-largeur/2 + 50,hauteur/2 - 30)
    tortue_texte.down()
    tortue_texte.write("Il y a " ,font=("arial",15,"normal"))
    tortue_nombre.up()
    tortue_nombre.goto(-largeur/2 + 100,hauteur/2 - 30)
    tortue_nombre.down()
    tortue_nombre.write(nb_voitures_depart,font=("arial",15,"normal"))
    tortue_texte.up()
    tortue_texte.goto(-largeur/2 + 130,hauteur/2 - 30)
    tortue_texte.down()
    tortue_texte.write("voitures",font=("arial",15,"normal"))
    
    #Affiche la règle
    tortue_texte.up()
    tortue_texte.goto( -150,hauteur/2 - 30)
    tortue_texte.down()
    tortue_texte.write("Vous pouvez retirer",font=("arial",15,"normal"))
    tortue_texte.up()
    tortue_texte.goto(30,hauteur/2 - 30)
    tortue_texte.down()
    tortue_texte.write(regle[0],font=("arial",15,"normal"))
    tortue_texte.up()
    tortue_texte.goto(50,hauteur/2 - 30)
    tortue_texte.down()
    tortue_texte.write(regle[1],font=("arial",15,"normal"))
    tortue_texte.up()
    tortue_texte.goto(70,hauteur/2 - 30)
    tortue_texte.down()
    tortue_texte.write(regle[2],font=("arial",15,"normal"))
    tortue_texte.up()
    tortue_texte.goto(90,hauteur/2 - 30)
    tortue_texte.down()
    tortue_texte.write("voitures",font=("arial",15,"normal"))
    
    tortue_texte.up()
    tortue_texte.goto(largeur/2 - 350,hauteur/2 - 30)
    tortue_texte.down()
    tortue_texte.write("Partie(s) : " ,font=("arial",15,"normal"))
    tortue_partie.up()
    tortue_partie.goto(largeur/2 - 250,hauteur/2 - 30)
    tortue_partie.down()
    tortue_partie.write(partie ,font=("arial",15,"normal"))
    
    
    
    #Debut jeux
    while not(gagner):
        
        #Tour joueur
        if(nb_voitures_courant >= min(regle)):
            nb_voitures_courant = nb_voitures_courant - coup_joueur(nb_voitures_courant,regle)
            nb_voitures_enlevees = nb_voitures_depart - nb_voitures_courant
            Maj(tortue_voiture,tortue_cache,largeur,hauteur,nb_voitures_enlevees)
            
           
        #Cas où l'ordinateur est gagnant ?
        else:
            tortue_texte.up()
            tortue_texte.goto(0,-hauteur/2 + 40)
            tortue_texte.down()
            tortue_texte.write("L'ordinateur a gagné", font=("arial",20,"normal"))
            gagner = True
          
        #Temporise le coup de l'ordinateur
        feuderoute(tf, 100, 50, largeur/2 -150 , hauteur/4 - 5)
        update()
        
          
        
        if not(gagner) : 
            
            #Tour ordinateur
            if(nb_voitures_courant >= min(regle)):
                nb_voitures_courant = nb_voitures_courant - coup_ordi(nb_voitures_courant,regle)
                nb_voitures_enlevees = nb_voitures_depart - nb_voitures_courant    
                
                
                feuligne(tf, 100, 50, largeur/2 -150 , hauteur/4 - 5)
                
                Maj(tortue_voiture,tortue_cache,largeur,hauteur,nb_voitures_enlevees)
                Maj_texte(tortue_nombre,nb_voitures_courant,largeur,hauteur)
            
            #Cas où le joueur est gagnant 
            else:
                tortue_texte.up()
                tortue_texte.goto(0,-hauteur/2 + 40)
                tortue_texte.down()
                tortue_texte.write("Le joueur a gagné", font=("arial",20,"normal"))
                gagner = True
                score = score + 1
               
            
    c = textinput("Joueur","Voulez vous continuer ? o/n ")
    if c == "n" :
        continuer = False
    else:
        gagner = False
        partie = partie + 1
        
        tortue_partie.up()
        tortue_partie.goto(largeur/2 - 250,hauteur/2 - 30)
        tortue_partie.down()
        tortue_partie.write(partie ,font=("arial",15,"normal"))
        update()

#Affiche le score du joueur
speed(0) 
decor(tortue_decor, largeur, hauteur)
tortue_texte.up()
tortue_texte.goto(-50,0)
tortue_texte.down()
tortue_texte.write("Vous avez gagné", font=("arial",20,"normal"))
tortue_texte.up()
tortue_texte.goto(-50,-30)
tortue_texte.down()
tortue_texte.write(score, font=("arial",20,"normal"))
tortue_texte.up()
tortue_texte.goto(-50,-60)
tortue_texte.down()
tortue_texte.write("partie(s) sur", font=("arial",20,"normal"))
tortue_texte.up()
tortue_texte.goto(-50,-90)
tortue_texte.down()
tortue_texte.write(partie, font=("arial",20,"normal"))
tortue_texte.up()
tortue_texte.goto(-50,-120)
tortue_texte.down()
tortue_texte.write("partie(s)", font=("arial",20,"normal"))

      


