#CREATED BY RYCHY, contact me -> jorgeajrhh@gmail.com

import random
from turtle import Turtle, Screen, colormode

tim = Turtle()
screen = Screen()
screen.colormode(255)

def rgb_random():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def move_forwards():
    tim.pencolor(rgb_random())
    tim.forward(20)
     
def move_backwards():
    tim.pencolor(rgb_random())
    tim.backward(20)

def move_counter_clockwise():
    tim.left(10)

def move_clockwise():
    tim.right(10)

def clear_drawing():
    tim.clear()

def up_down():
    if tim.isdown():
        tim.penup()
    else:
        tim.pendown()

def center():
    tim.penup()
    tim.home()
    tim.pendown()

tim.pensize(5)
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.onkey(key="u", fun=up_down)
screen.onkey(key="h", fun=center)




screen.exitonclick()
