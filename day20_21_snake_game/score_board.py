import random
import time
from turtle import Screen, Turtle 

screen = Screen()
screen.setup(width=600, height =680)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.colormode(255)
screen.tracer(0)

def random_rgb():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    return (r,g,b)

class Snake():
    snake_body = []
    def __init__(self):
        x = 0
        y = 0
        for body_peace in range(3):
            self.snake_body.append(self.__body_part(x,y))
            x += 20
    def __body_part(self,x,y):
        body = Turtle()
        body.penup()
        body.shape("square")
        body.shapesize(1,1,5)
        body.color(random_rgb(),"white")
        body.goto(x,y)
        screen.update()
        return body

    def move(self):
        #for i in range(start=, stop, step)
        for peace in range(len(self.snake_body)-1,0,-1):
            new_x = self.snake_body[peace-1].xcor()
            new_y = self.snake_body[peace-1].ycor()
            self.snake_body[peace].color(random_rgb(),"white")
            self.snake_body[peace].goto(new_x,new_y)
             
        if self.snake_body[0].xcor() > 540:
            self.snake_body[0].hideturtle()
            self.snake_body[0].goto(-300,self.snake_body[0].ycor())
            self.snake_body[0].showturtle()

        self.snake_body[0].forward(20)
        self.snake_body[0].left(90)
        screen.update()
        time.sleep(0.2)

snake = Snake() 
game_is_on = True
x = 0

while game_is_on:
    snake.move()
    if x == 40:
        game_is_on = False
    x += 1





screen.exitonclick()
