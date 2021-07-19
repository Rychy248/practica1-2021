#Talk to me, jorgeajrhh@gmail.com

from turtle import Turtle
import random

def random_rgb():
    r = random.randint(1,150)
    g = random.randint(1,150)
    b = random.randint(1,150)
    return (r,g,b)

class Marker(Turtle):
    """Mark the division in the screen"""
    def __init__(self,height_board=600):
        super().__init__()
        self.height_board = height_board
        self.hideturtle()
        self.penup()
        self.pensize(5)
        self.setheading(90)
        self.speed("fastest")
        self.marck_line()

    def marck_line(self):
        self.penup()
        self.clear()
        self.goto(0,self.height_board/2*-1)
        step = 0
        for _ in range(1,self.height_board,15):
            if step%3 == 0:
                self.color(random_rgb())
                self.down()
            else:
                self.penup()
            self.forward(15)
            step +=1

class ScoreMark(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.score = 0
        self.goto(position)
        self.__update_score()

    def __update_score(self):
        self.clear()
        self.color(random_rgb())
        self.write(f"{self.score}",font=("Courier",90),align="center")

    def plos_point(self):
        self.score += 1 
        self.__update_score()

class ScoreBoard():
    def __init__(self):
        self.left_mark = ScoreMark((-200,150))
        self.right_mark = ScoreMark((200,150))

    def plos_left(self,point=1):
        self.left_mark.plos_point()

    def plos_right(self,point=1):
        self.right_mark.plos_point()
