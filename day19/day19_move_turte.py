import turtle as t
import random

def rgb_random():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)
tim.color("white","yellow")
tim.pensize(5)

screen = t.Screen()
screen.title("Welcome to the turtle zoo!")
screen.bgcolor("black")

def move_up():
    tim.pencolor(rgb_random())
    tim.setheading(90)
    tim.forward(10)

def move_left():
    tim.pencolor(rgb_random())
    tim.setheading(180)
    tim.forward(10)

def move_right():
    tim.pencolor(rgb_random())
    tim.setheading(0)
    tim.forward(10)

def move_down():
    tim.pencolor(rgb_random())
    tim.setheading(270)
    tim.forward(10)


screen.listen()
screen.onkey(key="Up",fun=move_up)
screen.onkey(key="Down",fun=move_down)
screen.onkey(key="Left",fun=move_left)
screen.onkey(key="Right",fun=move_right)

screen.exitonclick()

