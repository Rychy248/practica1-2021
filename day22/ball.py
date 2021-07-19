#Talk to me, jorgeajrhh@gmail.com

from turtle import Turtle
import random
import time

class Ball(Turtle):
    MOVE_STEPS = 10

    def __init__(self,height_board=600,weight=800):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.shapesize(1,1,8)
        self.color(self.__random_rgb(),"white")
        self.penup()
        self.height_board = height_board/2
        self.weight_board = weight/2
        self.x_move = self.MOVE_STEPS
        self.y_move = self.MOVE_STEPS

    def restart(self):
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
        time_init = 0.001
        for random_color in range(13):
            self.color(self.__random_rgb(),"white")
            time.sleep(time_init)
            time_init+=0.01

    def __random_rgb(self):
        """Return a dark random color"""
        r = random.randint(1,150)
        g = random.randint(1,150)
        b = random.randint(1,150)
        return(r,g,b)

    def move(self):
        """decide de direction"""
        if self.ycor() > self.height_board-20 or self.ycor() < self.height_board*-1 +20: 
            self.y_move *= -1
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x,new_y)

    def rebot_x(self):
        self.x_move *= -1 
        for jump in range(4):
            self.move()
