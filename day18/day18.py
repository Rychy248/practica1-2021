#CREATED BY RYCHY, contact me -> jorgeajrhh@gmail.com

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

######## Challenge 1 - Draw a Square ############
def square(steps,color):
    """Draw a Dashed line square"""
    tim.pensize(5)
    tim.pencolor(color)

    if steps % 2 != 0:
        steps += 1

    for side in range(4):
        bit_line = 0
        size_bit_line = 10
        for _ in range(0,steps,size_bit_line):
            if bit_line % 2 != 0:
                tim.penup()
            else:
                tim.pendown()
            tim.forward(size_bit_line)
            bit_line += 1
        tim.right(90) 
#Second Challange
def differents_shapes(large_side,shapes_num):
    """Draw diferentes shapes"""
    CIRCLE = 360
    size_bit_line = 10
    grades_turn = 0
    shapes_num = shapes_num + 3
    tim.pensize(2)

    if large_side % 2 != 0:
        large_side += 1

    for cardinals_points in range(4):
        for a_shape in range(3,shapes_num,1):
            grades_turn = CIRCLE / a_shape
            tim.pencolor(random_rgb())
            for side in range(a_shape):
                bit_line = 0
                for _ in range(0,large_side,size_bit_line):
                    if bit_line % 2 != 0:
                        tim.penup()
                    else:
                        tim.pendown()
                    if cardinals_points in [0,1]:
                        tim.forward(size_bit_line)
                    if cardinals_points in [2,3]:
                        tim.backward(size_bit_line)
                    bit_line += 1
                if cardinals_points in [0,2]:
                    tim.right(grades_turn)
                if cardinals_points in [1,3]:
                    tim.left(grades_turn)

def random_walk(steps):
    """Random Walk"""
    tim.speed("fastest")
    tim.pensize(2)
    for step in range(steps):
        tim.pencolor(random_rgb())
        tim.pensize(random.choice([2,3,4]))
        if step % 50 == 0:
            print("Step ",step)
        tim.forward(random.choice([6,8,10,12,14,16]))
        tim.setheading(random.choice([0,90,180,270]))
        #tim.left(random.choice([0,90,180,270])) 

#square(100,"DarkBlue")
#differents_shapes(40,10)
random_walk(1500)

screen = Screen()
screen.exitonclick()
