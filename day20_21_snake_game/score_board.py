#CREATED BY RYCHY, contact me -> jorgeajrhh@gmail.com

import random
from turtle import Turtle 
FONT = ("Arial",34,"normal")
ALIGMENT = "center"

def random_rgb():
    r = random.randint(100,255)
    g = random.randint(100,255)
    b = random.randint(100,255)
    return (r,g,b)

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.color(random_rgb())
        self.hideturtle()
        self.penup()
        self.update_board()
        #frame  w=900, h=680, w=450, h=340
        #snake  w=600, h=680, w=150, h=340
        #border w=300, h=680, w=350, h=0

    def update_board(self):
        self.clear()
        self.goto(250,0)
        self.color(random_rgb())
        self.write(f"Score : {self.score}",align=ALIGMENT,font=FONT)
        self.goto(250,40)
        self.color(random_rgb())
        self.write(f"Level : {self.level}",align=ALIGMENT,font=FONT)

    def refresh(self):
        self.score += 1
        self.update_board()
     
    def up_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write("G A M E   O V E R",align=ALIGMENT,font=FONT)

