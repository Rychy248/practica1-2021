#CREATED BY RYCHY, contact me -> jorgeajrhh@gmail.com
import time

from turtle import Screen
from snake import Snake
from paint_border import border
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=900, height =680) # for snake is width = 600, height = 680
screen.bgcolor("black")
screen.title("My Snake Game")
screen.colormode(255)
screen.tracer(0)

border()
food = Food()
score_board = ScoreBoard()
snake = Snake() 
screen.update()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

speed = 0.2
levels = 1
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move()

    if snake.snake_body[0].distance(food) < 20: #collated
        food.refresh()
        score_board.refresh()
        snake.add_body()
        levels+=1
        if levels == 5:
            levels = 1
            if speed > 0:
                speed -= 0.02
            score_board.up_level()  
    #now we're using a slicen into the list
    for segment in snake.snake_body[1:]: 
        if segment.distance(snake.snake_body[0]) < 10:
            score_board.game_over()
            game_is_on = False

screen.exitonclick()
