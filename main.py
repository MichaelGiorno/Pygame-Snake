import pygame
import turtle
import time
import random

delay = 0.1#ritardo dei tasti

score = 0#punteggio
high_score = 0#Punteggio massimo

wn = turtle.Screen()#Quello che crea il campo di gioco
wn.title("Il mio giochino")#Il titolo
wn.bgcolor("black")#Colore del monitor
wn.setup(width=600, height=600)#grandezza monitor
wn.tracer(0) #Disattiva le animazioni

head = turtle.Turtle()#rappresenta la sua testa
head.speed(0)#velocità a cui va
head.shape("square")#forma che gli diamo
head.color("yellow") #il colore che gli diamo
head.penup()#Solleva la penna in modo che non disegni mentre si sposta. (?)
head.goto(0,0)# Muove la testa del serpente alla posizione (0, 0) sullo schermo. (?)
head.direction = "stop"#appena iniziato il gioco questo codice fa si che non si deve muovere

food = turtle.Turtle()#rappresenta il suo cibo
food.speed(0)#velocita
food.shape("square")#forma
food.color("brown")#colore
food.penup()#Solleva la penna in modo che non disegni mentre si sposta. (?)
food.goto(20,100)# (?)

segmenti = []#tiene traccia dai suoi movimenti

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Terminal", 20, "normal"))#Il carattere, e dove lo allieamo il punteggio e il punteggio massimo.

def go_up():
    head.direction = "up"                  

def go_down():
    head.direction = "down"

def go_left():                                 #Le loro funzioni
    head.direction = "left"

def go_right():
    head.direction = "right"




def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":                     #Le loro funzioni
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_down, "Down")


while True:
    wn.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-256: #Se la testa del serpente è fuori dal campo di gioco, per prevenire ciò si usano le coordinate, Xcor significa la cordinata x, Ycor, coordinata Y. (?)
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for segmento in segmenti:
            segmento.goto(1000, 1000)

        segmenti.clear()
        score = 0

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Terminal", 20, "normal"))

    if head.distance(food) < 30:
        x = random.randint(-290,290)
        y = random.randint(-240,290)
        food.goto(x,y)
        new_segmento = turtle.Turtle()
        new_segmento.speed(2)
        new_segmento.shape("square")
        new_segmento.color("purple")
        new_segmento.penup()
        segmenti.append(new_segment)

        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Terminal", 20, "normal"))


    for index in range(len(segmenti)-1, 0, -1):
        x = segmenti[index-1].xcor()
        y = segmenti[index-1].ycor()
        segmenti[index].goto(x, y)
                                                    #Fa si che il cibo ingerito del serpente, i blocchi dietro lo seguano (?)
    if len(segmenti) > 0:
        x = head.xcor()
        y = head.ycor()
        segmenti[0].goto(x,y)



    move()

    for segmento in segmenti:
        if segmento.distance(head) < 20:
            head.goto(0,0)
            head.direction = "stop"
            segmenti.clear()


            score = 0

            pen.clear() #prima di scrivere il miglior punteggio, verifica prima se prima c'è ne uno migliore, poi dopo lo scrive con questo qua sotto:-->
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Terminal", 20, "normal"))

