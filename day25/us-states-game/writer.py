import random
from turtle import Turtle

class Progress(Turtle):
    """write the progress"""
    FONT = ("Courier", 12, "normal")
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pensize(10)
        self.color("black")
        self.goto(-40,-270)
        messegue = "Right Answers: 0/50 - intents: 0"
        self.update_progress(messegue)

    def update_progress(self,messegue):
        self.clear()
        self.write(f"{messegue}",align="center",font=self.FONT)

class Writer(Turtle):
    """Write the name into a the map"""
    FONT = ("Courier", 8, "normal")
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_name(self,state,coor=(0,0)):
        """Write a state's name on the screen"""
        self.goto(coor)
        self.color(self.__random_rgb())
        self.write(f"{state}",align="center",font=self.FONT)

    def __random_rgb(self):
        r = random.randint(10,120)
        g = random.randint(10,120)
        b = random.randint(10,120)

        return (r,g,b)
