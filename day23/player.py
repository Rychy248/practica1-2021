#Talk to me, jorgeajrhh@gmail.com
import random
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    MOVE_STEPS = 20

    """Here is created our Player"""
    def __init__(self,position=(0,0)):
        """Create a Turtle"""
        super().__init__()
        self.penup()
        self.shape("turtle") #natural is 20 * 20
        self.change_color()
        self.speed("fastest")
        self.shapesize(1,1,1)
        self.goto(position)
        self.setheading(90)

    def __rgb_dark(self):
        """Return a random dark rgb color"""
        return (random.randint(1,150), random.randint(1,150), random.randint(1,150))

    def __rgb_light(self):
        """Return a random light rgb color"""
        return (random.randint(150,200), random.randint(150,200), random.randint(150,200))

    def change_color(self):
        self.color(self.__rgb_dark(),self.__rgb_light())

    def move_up(self):
        if 300>= self.ycor():
            self.setheading(90)
            self.forward(self.MOVE_STEPS)
        else:
            self.change_color()
         
    def move_down(self):
        if -300 + 40 <= self.ycor():
            self.setheading(90)
            self.backward(self.MOVE_STEPS)
        else:
            self.change_color()

    def move_left(self):
        if -300+40 <= self.xcor():
            self.setheading(180)
            self.forward(self.MOVE_STEPS)
        else:
            self.change_color()
         
    def move_right(self):
        if 300-40 >= self.xcor():
            self.setheading(0)
            self.forward(self.MOVE_STEPS)
        else:
            self.change_color()


    def restart(self):
        self.goto(0,-280)
        self.change_color()
