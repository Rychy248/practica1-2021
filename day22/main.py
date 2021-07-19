#Talk to me, jorgeajrhh@gmail.com

import time
import random
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Marker, ScoreBoard

def random_rgb():
    """Return a random light color"""
    r = random.randint(200,200)
    g = random.randint(200,255)
    b = random.randint(200,255)

    return (r,g,b)


WIDTH = 800
HEIGHT = 600
screen = Screen()

screen.setup(WIDTH,HEIGHT)
screen.title("PONG GAME")
screen.colormode(255)
screen.bgcolor(random_rgb())
screen.tracer(0)

player_left = Paddle(HEIGHT,(350,0))
player_right = Paddle(HEIGHT,(-350,0))
ball = Ball(HEIGHT,WIDTH)
mark = Marker(HEIGHT) 
score = ScoreBoard()

screen.onkey(player_left.move_up,"Up")
screen.onkey(player_left.move_down,"Down")
screen.onkey(player_right.move_up,"w")
screen.onkey(player_right.move_down,"s")
screen.listen()

time_sleep = 0.08
def order():
    screen.bgcolor(random_rgb())
    ball.restart()
    player_right.clear()
    player_left.clear()
     
screen.tracer(3)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(time_sleep)
    #80 because, tge padle is 20px and is 50px separated from the wall
    if ball.xcor() >= WIDTH/2-80 and ball.xcor() <= WIDTH/2-50:
        if ball.distance(player_left) < 100:
            player_left.change_color_border()
            ball.rebot_x()
            if time_sleep > 0.005:
                time_sleep -= 0.005
    elif ball.xcor() >= WIDTH/2:
        score.plos_left()
        time_sleep = 0.04
        order()

    if ball.xcor() <= WIDTH/2*-1+80 and ball.xcor() >= WIDTH/2*-1+50:
        if ball.distance(player_right) < 100:
            player_right.change_color_border()
            ball.rebot_x()
            if time_sleep > 0.005:
                time_sleep -= 0.005
    elif ball.xcor() <= WIDTH/2*-1:
        score.plos_right()
        time_sleep = 0.04
        order()
    ball.move()

screen.exitonclick()


