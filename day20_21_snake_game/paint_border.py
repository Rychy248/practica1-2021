#CREATED BY RYCHY, contact me -> jorgeajrhh@gmail.com

from turtle import Turtle
from snake import random_rgb

def move(turtle, path, direction):
        mark = turtle 
        mark.setheading(direction)
        i = 0
        for _ in range(0,path,16):
            if i % 2 == 0:
                mark.color(random_rgb())
                mark.down()
            else:
                mark.penup()
            mark.forward(16)
            i+=1

def border():
    mark = Turtle()
    mark.color(random_rgb())
    mark.pensize(4)
    mark.shapesize(1,1,5)
    mark.penup()
    mark.goto(-446,-332)
    mark.down()
    move(mark,596,0)
    mark.goto(150,-332)
    move(mark,668,90)
    mark.goto(150,336)
    move(mark,596,180)
    mark.goto(-446,336)
    move(mark,668,270)
    mark.goto(-446,-332)
    mark.hideturtle()
