#CREATED BY RYCHY, contact me -> jorgeajrhh@gmail.com
import random 
from turtle import Turtle

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5) # normal size is 20px, if wi multiply for 0.5 it will be 10px
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Set the food a new random location"""
        random_x = random.randint(-440,140) #less 10px
        random_y = random.randint(-330,330) #less 10px
        self.goto(random_x,random_y)

