"""
Woking whit Turtle library
Documentation https://docs.python.org/3/library/turtle.html
Colors        https://cs111.wellesley.edu/labs/lab01/colors
color tk      https://trinket.io/docs/colors
"""

#####Turtle Intro######
import turtle as t
from turtle import Screen, pensize
import random 

tim = t.Turtle()
# modify the module, fro rgb
t.colormode(255)

tim.shape("turtle")
tim.color("DarkOrange3")
tim.setheading(0)

##### RANDOM COLOR
def random_rgb():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def draw_circle(size_of_gap):
    tim.speed("fastest")
    for head_position in range(368//size_of_gap):
        tim.setheading(tim.heading()+size_of_gap)
        tim.color(random_rgb())
        tim.circle(100)

draw_circle(1)
screen = Screen()
screen.exitonclick()
