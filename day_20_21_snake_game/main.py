from turtle import Screen, Turtle 

screen = Screen()
screen.setup(width=600, height =680)
screen.bgcolor("black")
screen.title("My Snake Game")

class Snake():
    snake_body = []
    def __init__(self):
        x = 0
        y = 0
        for _ in range(3):
            peace_of_body = Turtle()
            peace_of_body.penup()
            peace_of_body.shape("square")
            peace_of_body.shapesize(0.5,0.5,3)
            peace_of_body.color("blue","yellow")
            peace_of_body.goto(x,y)
            x+=13
            self.snake_body.append(peace_of_body)

snake = Snake() 






screen.exitonclick()
