#Talk to me, jorgeajrhh@gmail.com
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard, Marker

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Raice")
screen.tracer(0)
screen.colormode(255)
screen.bgcolor(0,0,0)

player = Player((0,-280))
cars = CarManager(max_cars=1)
score = ScoreBoard()
lines = Marker()

screen.onkey(player.move_up,"Up")
screen.onkey(player.move_down,"Down")
screen.onkey(player.move_left,"Left")
screen.onkey(player.move_right,"Right")
screen.listen()

time_sleep = 0.1
game_is_on = True
while game_is_on:
    time.sleep(time_sleep)
    screen.update()
    cars.move()
    if player.ycor() >= 300:
        time_sleep *= 0.9
        player.restart()
        cars.level_up()
        score.update_level()

    for car in cars.cars_in_screen:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()
