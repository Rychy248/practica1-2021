#CREATED BY RYCHY, contact me -> jorgeajrhh@gmail.com

import random
from turtle import Turtle 

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20

def random_rgb():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    return (r,g,b)

class Snake():
    snake_body = []
    def __init__(self):
        """Create the initial body snake"""
        x = 60
        y = 0
        for body_peace in range(3):
            self.snake_body.append(self.__body_part(x,y))
            x -= 20

    def __body_part(self,x,y):
        """return a peace of snake body"""
        body = Turtle()
        body.penup()
        body.shape("square")
        body.shapesize(1,1,5)
        body.color(random_rgb(),"white")
        body.goto(x,y)
        return body

    def add_body(self):
        """Add a peace of the body"""
        x = self.snake_body[-1].xcor()
        y = self.snake_body[-1].ycor()
        self.snake_body.append(self.__body_part(x,y))

    def move(self):
        "Move the snake"
        #for i in range(start=, stop, step)
        for peace in range(len(self.snake_body)-1,0,-1):
            new_x = self.snake_body[peace-1].xcor()
            new_y = self.snake_body[peace-1].ycor()
            self.snake_body[peace].color(random_rgb(),"white")
            self.snake_body[peace].goto(new_x,new_y)
             
        if self.snake_body[0].xcor() > 130:
            self.snake_body[0].goto(-450,self.snake_body[0].ycor())
        elif self.snake_body[0].xcor() < -430:
            self.snake_body[0].goto(150,self.snake_body[0].ycor())

        if self.snake_body[0].ycor() > 320:
            self.snake_body[0].goto(self.snake_body[0].xcor(),-340)
        elif self.snake_body[0].ycor() < -320:
            self.snake_body[0].goto(self.snake_body[0].xcor(),340)
        
        self.snake_body[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)

