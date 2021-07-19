#Talk to me, jorgeajrhh@gmail.com

import random
from turtle import Turtle

class Paddle(Turtle):
    MOVE_STEPS = 60
    """This class define our paddle"""
    def __init__(self,height_board=600,position=(0,0)):
        """Need the height, of your screen"""
        super().__init__()
        self.change_color_border()
        self.penup()
        self.height_board = height_board/2
        self.shape("square") #natural is 20 * 20
        self.speed("fastest")
        self.shapesize(1,5,3)
        self.goto(position)
        self.pensize(4)
        self.down()
        self.setheading(90)

    def __random_rgb(self):
        r = random.randint(1,255)
        g = random.randint(1,200)
        b = random.randint(1,200)
        return(r,g,b)

    def change_color_border(self):
        self.color(self.__random_rgb(),"white")

    def move_up(self):
        if self.height_board - 60> self.ycor():
            self.forward(self.MOVE_STEPS)
        else:
            self.change_color_border()
         
    def move_down(self):
        if self.height_board*-1 +60 < self.ycor():
            self.backward(self.MOVE_STEPS)
        else:
            self.change_color_border()
