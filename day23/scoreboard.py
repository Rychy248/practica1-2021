#Talk to me, jorgeajrhh@gmail.com

from turtle import Turtle
import random

def random_rgb():
    r = random.randint(100,255)
    g = random.randint(100,255)
    b = random.randint(100,255)
    return (r,g,b)

class Marker(Turtle):
    """Mark the division in the screen"""

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pensize(2)
        self.speed("fastest")
        self.mark_road()

    def mark_road(self):
        self.clear()
        self.goto(300,-260)
        self.setheading(180)
        
        while self.ycor() <= 240:
            self.goto(self.xcor(),(self.ycor()+20))
            self.marck_line()
            self.left(180)


    def marck_line(self):
        self.penup()
        step = 0
        self.color(random_rgb())
        for _ in range(1,600,5):
            if step%3 == 0:
                self.down()
            else:
                self.penup()
            self.forward(5)
            step +=1

class ScoreBoard(Turtle):
    """Marck the score on the screnn"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.level = 0
        self.goto(-200,250)
        self.color("white")
        self.update_level()

    def print_level(self):
        self.clear()
        self.goto(-200,250)
        self.write(f"L E V E L: {self.level}",font=("Courier",20,"normal"),align="center")

    def update_level(self):
        self.print_level()
        self.level += 1 
    
    def game_over(self):
        self.goto(0,0)
        self.write("G A M E - O V E R",font=("Courier",40,"normal"),align="center")


