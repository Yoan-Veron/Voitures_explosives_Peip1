# -*- coding: utf-8 -*-
"""

@author: Anaïs Lacouture
@author: Yoan Veron

"""

from turtle import *
from random import*
import time

#Fonction pour dessiner la pelouse/rectangle vert  et la route/rectangle gris
def pelouse(t,l,h):
    tracer(0)
    t.up()
    t.goto(-l/2,-h/2)
    t.down()
    t.fillcolor("green")
    t.begin_fill()
    for i in range (2):
        t.forward(l)
        t.left(90)
        t.forward(h/4)
        t.left(90)
    t.end_fill()

#Dessine le terrain
def terrain(t,l,h):
    tracer(0)
    t.up()
    t.goto(-l/2,-h/2 + h/4)
    t.down()
    t.fillcolor("grey")
    t.begin_fill()
    for i in range (2):
        t.forward(l)
        t.left(90)
        t.forward(h/2)
        t.left(90)
    t.end_fill()


#Fonction qui regroupe tous les éléments du décor
def decor(t,l,h):
    tracer(0)
    pelouse(t,l,h)
    terrain(t,l,h)
    pelouse(t,l,-h)
    tribune(t,l,h)
    depart(t,l,h)
    taille = [0.4,0.5,0.3]
    for i in range(4):
        a = choice(taille)
        tasroues(-l/2 + 250 + (i-1)*200,-h/2 + 80,a)

#Dessine des carres pour la grille de depart 
def carre(t,couleur,cote):
    tracer(0)
    t.fillcolor(couleur)
    t.begin_fill()
    for i in range (4):
        t.forward(cote)
        t.left(90)
    t.end_fill()
    t.forward(cote)


#Dessine la grille de départ
def depart(t,l,h):
    tracer(0)
    i = 0
    n = h/2/20
    cotes = 20
    while i < n :
        t.up()
        t.goto(-l/2,-h/4 + cotes*i)
        t.down()
        
        if i % 2 == 0 :
            carre(t,"black",cotes)
            carre(t,"white",cotes)
            carre(t,"black",cotes)
        else :
            carre(t,"white",cotes)
            carre(t,"black",cotes)
            carre(t,"white",cotes)
    
        i = i + 1

#Cette fonction permet de dessiner les flammes ou les voitures ou les carres pour cacher les voitures
def dessin(t,l,h,n,m):
    tracer(0)
    positiony = [50,h/4,h/2-40]
    i = 2
    cpt = 0
    while cpt < n :
        j = 0
        while j < 3 and cpt < n:
            if m == "flammes":
                flammes(t,20,-l/2 + 90*i -100 ,-h/4 + positiony[j])
            elif m == "voitures":
                voiture(t,-l/2 + 90*i -100,-h/4 + positiony[j] ,0.3)
            else:
                cache(t,-l/2 + 90*i -100 ,-h/4 + positiony[j] + 35)
                
            j = j + 1 
            cpt = cpt + 1
        i = i + 2


#Trace un rectangle gris pour cacher la voiture
def cache(t,x,y):
    t.pencolor("grey")
    t.up()
    t.goto(x,y)
    t.down()    
    t.fillcolor("grey")
    t.begin_fill()  
    carre(t,"grey",80)
    t.end_fill()
    
    
     
    
#Dessine une explosion pour remplacer la voiture
def flammes(t,taille,x,y):  
    tracer(0)
    t.up()
    t.goto(x,y)
    t.down()
    t.color("red")
    setheading(270)
    t.begin_fill()
    t.forward(taille/6)
    t.circle(taille/4,140)
    t.right(160)
    for i in range(16):
        t.circle(taille/4,140)
        t.right(160)
    t.circle(taille/4,140)
    t.right(160)
    t.end_fill()
    
    t.up()
    t.goto(x+taille/3,y)
    t.down()
    t.color("orange")
    setheading(270)
    t.begin_fill()
    t.forward(taille/7) 
    t.circle(taille/5,140)
    t.right(160)
    for i in range(16):
        t.circle(taille/5,140)
        t.right(160)
    t.circle(taille/5,140)
    t.right(160)
    t.end_fill()
    
    t.up()
    t.goto(x+taille/2,y)
    t.down()
    t.color("yellow")
    setheading(270)
    t.begin_fill()
    t.forward(taille/8) 
    t.circle(taille/6,140)
    t.right(160)
    for i in range(16):
        t.circle(taille/6,140)
        t.right(160)
    t.circle(taille/6,140)
    t.right(160)
    t.end_fill()
    
    



c=["red","green","blue","orange","purple"]



def voiture(t,x,y,taille):
    tracer(0)
    t.width(1)
    roue(t,x,y,taille)
    t.width(1)
    t.up()
    t.goto(x,y)
    t.down()
    chassis(t,x,y,c,taille)
    casque(t,x,y,taille)

def casque(t,x,y,taille):
    tracer(0)
    t.up()
    t.goto(x+150*taille,y)
    t.setheading(270)
    t.down()
    t.begin_fill()
    t.color("black")
    t.width(1)
    t.circle(10*taille)
    t.end_fill()
    
def roue(t,x,y,taille):
    tracer(0)
    t.up()
    t.goto(x+15*taille,y+35*taille)
    t.setheading(0)
    t.down()
    t.color("black")
    t.begin_fill()
    for i in range(0,2):
        for i in range (0,2):
            t.forward(50*taille)
            t.left(90)
            t.forward(25*taille)
            t.left(90)
        t.up()
        t.goto(x+180*taille,y+35*taille)
        t.down()
    t.end_fill()
    t.up()
    t.goto(x+15*taille,y-35*taille)
    t.down()
    t.begin_fill()
    for i in range(0,2):
        for i in range (0,2):
            t.forward(50*taille)
            t.right(90)
            t.forward(25*taille)
            t.right(90)
        t.up()
        t.goto(x+180*taille,y-35*taille)
        t.down()
    t.end_fill()
    t.up()
    t.goto(x+40*taille,y+35*taille)
    t.width(2*taille)
    t.down()
    t.goto(x+40*taille,y-35*taille)
    t.up()
    t.goto(x+205*taille,y+35*taille)
    t.width(2*taille)
    t.down()
    t.goto(x+205*taille,y-35*taille)

def chassis(t,x,y,c,taille,a=1):
    tracer(0)
    t.pencolor("black")
    t.width(taille)
    t.fillcolor(choice(c))
    t.up()
    for i in range (0,2):
        t.begin_fill()
        t.goto(x,y)
        t.setheading(0)
        t.down()
        t.left(90*a)
        t.forward(40*taille)
        t.right(90*a)
        t.forward(10*taille)
        t.right(90*a)
        t.forward(28*taille)
        t.left(90*a)
        t.forward(15*taille)
        t.left(45*a)
        t.forward(20*taille)
        t.right(45*a)
        t.forward(35*taille)
        t.left(90*a)
        t.forward(20*taille)
        t.right(90*a)
        t.forward(90*taille)
        t.right(45*a)
        t.forward(30*taille)
        t.left(45*a)
        t.forward(40*taille)
        t.right(90*a)
        t.forward(20*taille)
        t.left(90*a)
        t.forward(15*taille)
        t.left(90*a)
        t.forward(45*taille)
        t.circle(30*taille*a,45)
        t.setheading(0)
        t.forward(10*taille)
        t.circle(-30*taille*a,45)
        t.setheading(270*a)
        t.forward(63*taille)
        a=-a
        t.up()
        t.end_fill()
   


    
peau=["tan","bisque","navajowhite","darkgoldenrod","saddlebrown","peachpuff"]
f=[10,10,10,10,10,9,9,9,10,10,7,7,8,8,0,0]
y=window_width()
x=window_height()

def bonhomme(t,x,y,f):
    tracer(0)
    t.up()
    t.goto(x,y)
    t.down()
    t.pencolor("black")
    t.fillcolor((randint(0,255)/255,randint(0,255)/255,randint(0,255)/255))
    t.setheading(0)
    t.down()
    t.begin_fill()
    t.forward(1*f)
    t.left(90)
    t.forward(2*f)
    t.left(30)
    t.forward(2*f)
    t.up()
    t.goto(x,y)
    t.down()
    t.setheading(180)
    t.forward(1*f)
    t.right(90)
    t.forward(2*f)
    t.right(30)
    t.forward(2*f)
    t.end_fill()
    t.up()
    t.goto(x,y+3*f)
    t.setheading(0)
    t.down()
    t.pencolor("black")
    t.fillcolor(choice(peau))
    t.begin_fill()
    t.circle(1*f)
    t.end_fill()
    t.up()
    
def tribune(t,x,y):
    for j in range (0,3):
        for i in range (0,58):
            tracer(0)
            bonhomme(t,-(x-110)/2+24*i+12*(j%2)-40,y/2-110-30*j,choice(f))



       
def feueteint(t,l,L,x,y):
    t.setheading(0)
    rectangle(t,l,L,x,y)
    feubas(t,l,L,x,y,couleur="lightslategrey")
    t.setheading(0)
    feuhaut(t,l,L,x,y)
    x+=L*1.5

def rectangle(t,l,L,x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.pencolor("black")
    t.fillcolor("black")
    t.begin_fill()
    for i in range(0,2):
        t.forward(l)
        t.right(90)
        t.forward(L)
        t.right(90)
    t.end_fill()

def feubas(t,l,L,x,y,couleur="red"):
    t.up()
    t.goto(x+l/4,y-L*0.1)
    t.down()
    t.setheading(0)
    t.pencolor("black")
    t.fillcolor(couleur)
    t.begin_fill()
    t.circle(-L*0.8/2)
    t.end_fill()

def feuhaut(t,l,L,x,y):
    t.up()
    t.goto(x+l*3/4,y-L*0.1)
    t.down()
    t.setheading(0)
    t.pencolor("black")
    t.fillcolor("lightslategrey")
    t.begin_fill()
    t.circle(-L*0.8/2)
    t.end_fill()

def feuligne(t,l,L,x,y):
    for i in range(0,5):
        feueteint(t,l,L,x,y)
        y-=1.5*L

def feuderoute(t,l,L,x,y):
    for i in range(0,5):
        feubas(t,l,L,x,y,couleur="red")
        y-=1.5*L
        update()
        time.sleep(0.35)
        



def pave(x,y,f):
    width(f)
    up()
    goto(x,y)
    down()
    setheading(0)
    pencolor("grey")
    begin_fill()
    for i in range(0,2):
        forward(100*f)
        left(90)
        forward(50*f)
        left(90)
    end_fill()

def r(x,y,f):
    color("black")
    setheading(0)
    pave(x,y,f)
    pencolor("grey")
    width(f)    
    up()
    goto(x,y)
    down()
    setheading(110)
    begin_fill()
    circle(-76*f,39)
    up()
    goto(x+100*f,y)
    down()
    setheading(70)
    circle(76*f,39)
    end_fill()
    lignetriangle(x+10,y+5,f/2,6)
    y+=12*f
    for i in range(0,3):
        lignetriangle(x+3,y,f/2,7)
        y+=10*f
    lignetriangle(x+10,y,f/2,6)

def roueface(x,y,f):
    up()
    color("black")
    goto(x,y)
    down()
    pencolor("silver")
    begin_fill()
    setheading(0)
    circle(50*f)
    end_fill()
    up()
    color("silver")
    goto(x,y+20*f)
    down()
    begin_fill()
    circle(30*f)
    end_fill()

def triangle(x,y,f):
    up()
    goto(x,y)
    down()
    begin_fill()
    for i in range(0,3):
        forward(10*f)
        left(120)
    end_fill()

def lignetriangle(x,y,f,l):
    color("dimgray")
    begin_fill()
    for i in range(0,l):
        a=0
        setheading(0)
        for i in range(0,2):
            triangle(x,y,f)
            up()
            goto(x+12*f,y)
            down()
            setheading(a+60)
            x+=14*f
    end_fill()
   
def tasroues(x,y,f):
    b=y
    for i in range(0,3):
        r(x,b,f)
        b-=50*f
    roueface(x-10*f,y-100*f,f)

