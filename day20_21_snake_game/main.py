#CREATED BY RYCHY, contact me -> jorgeajrhh@gmail.com

import time

from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height =680)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.colormode(255)
screen.tracer(0)

snake = Snake() 
screen.update()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

x = 0
game_is_on = True
while game_is_on:
    for step in range(140):
        screen.update()
        time.sleep(0.2)
        snake.move()
        if x == 10:
            game_is_on = False 
        x += 1

screen.exitonclick()

