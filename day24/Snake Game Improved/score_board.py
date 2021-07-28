#CREATED BY RYCHY, contact me -> jorgeajrhh@gmail.com

import random
from turtle import Turtle 

FONT = ("Arial",24,"normal")
ALIGMENT = "center"

def random_rgb():
    r = random.randint(100,255)
    g = random.randint(100,255)
    b = random.randint(100,255)
    return (r,g,b)

class high_score():
    """Administratate de high_score"""


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = self.__read_high_s()
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
        self.goto(250,40)
        self.color(random_rgb())
        self.write(f"High Score: {self.high_score}",align=ALIGMENT,font=FONT)
        self.goto(250,0)
        self.color(random_rgb())
        self.write(f"Score : {self.score}",align=ALIGMENT,font=FONT)
        self.goto(250,-40)
        self.color(random_rgb())
        self.write(f"Level : {self.level}",align=ALIGMENT,font=FONT)

    def refresh(self):
        self.score += 1
        self.update_board()
     
    def up_level(self):
        self.level += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.__write_high_s(self.high_score)
        self.score = 0
        self.update_board()

    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write("G A M E   O V E R",align=ALIGMENT,font=FONT)

    def __read_high_s(self):
        """Return the last high_score"""
        high_s = 0
        with open("high_score.txt","r") as file:
            high_s = int(file.read())
        return high_s

    def __write_high_s(self,score):
        """Write in the file"""
        with open("high_score.txt","w") as file:
            file.write(f"{score}")
