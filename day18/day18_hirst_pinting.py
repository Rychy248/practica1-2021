#Documentation
#https://pypi.org/project/colorgram.py/
#pip install colorgram.py

import colorgram
import turtle as t
import random 

"""
b a s i c   d o c u m e n t a t i o n
# Extract 6 colors from an image.
colors = colorgram.extract('sweet_pic.jpg', 6)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
first_color = colors[0]
rgb = first_color.rgb # e.g. (255, 151, 210)
hsl = first_color.hsl # e.g. (230, 255, 203)
proportion  = first_color.proportion # e.g. 0.34

# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
red = rgb[0]
red = rgb.r
saturation = hsl[1]
saturation = hsl.s
"""

rgb_colors = []
colors = colorgram.extract('day18_picture.jpg', 33)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))
for index in range(5): #removing the first colors because there the background
    rgb_colors.pop(0)

timmy = t.Turtle()
t.colormode(255)

def paint(dots=4,diameter=20):
    size_square = dots
    total_dots = dots*dots
    diameter_dot = diameter 
    space_into_dot = diameter/5
    timmy.setheading(0)
    timmy.speed("fastest")

    timmy.penup()
    timmy.backward(diameter_dot*(size_square//2))
    timmy.left(90)
    timmy.forward(diameter_dot*(size_square//2))
    timmy.right(90)
    timmy.pendown()

    def next_line():
        timmy.penup()
        if timmy.heading() > 0:
            #timmy see the west
            timmy.left(90)
            timmy.forward(diameter_dot+space_into_dot)
            timmy.left(90)
        elif timmy.heading() == 0:
            timmy.right(90)
            timmy.forward(diameter_dot+space_into_dot)
            timmy.right(90)
        timmy.pendown()
 
    for _ in range(size_square):
        for dot in range(size_square):
            timmy.dot(diameter_dot,random.choice(rgb_colors))
            timmy.penup()
            if dot+1 < size_square: #dot plos one, beacause de last num from the range is one less
                # dot 0, 1, 2 ... size_square-1
                timmy.forward(diameter_dot+space_into_dot)
            timmy.pendown()
        next_line()


paint(dots=50,diameter=10)

screen = t.Screen()
screen.exitonclick()




