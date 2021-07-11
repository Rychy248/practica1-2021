
from turtle import Turtle, Screen
import random
# https://docs.python.org/3.1/library/turtle.html#turtle.textinput
def rgb_random():
    r = random.radint(1,255)
    g = random.radint(1,255)
    b = random.radint(1,255)

    return (r,g,b)

raiwbo = ["red","orange","yellow","green","blue","purple"]
turtles = []

def mark_goal ():
    arbitr = Turtle()
    arbitr.color("black")
    arbitr.pensize(8)
    def mark():
        for _ in range(0,400,20):
            arbitr.color("orange")
            arbitr.forward(10)
            arbitr.color("black")
            arbitr.forward(10)
    arbitr.penup()
    arbitr.goto(320,200)
    arbitr.down()
    arbitr.setheading(270)
    mark()
    arbitr.setheading(180)
    arbitr.penup()
    arbitr.forward(8)
    arbitr.down()
    arbitr.setheading(90)
    mark()
    arbitr.hideturtle()

def create_turtles():
    for t in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.shapesize(3,3,0)
        new_turtle.color(raiwbo[t],raiwbo[t])
        new_turtle.pensize(3)
        new_turtle.penup()
        new_turtle.goto(x=-350,y=(-160+t*60))
        new_turtle.down()
        turtles.append(new_turtle)

def raice():
    some_win = False
    while not some_win:
        turtle_step = random.choice(turtles)
        random_distance = random.randint(5,10)
        turtle_step.forward(random_distance)
        if turtle_step.xcor() >= 320:
            some_win = True
            win_color = turtle_step.pencolor()
            if win_color == user_bet:
                print("Congratulations, You win!")
            else:
                print("Sorry, Yoy lose!")

screen = Screen()
screen.setup(width=760,height=450)

create_turtles()
mark_goal()
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
raice()
screen.exitonclick()
