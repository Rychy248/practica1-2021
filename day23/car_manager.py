#Talk to me, jorgeajrhh@gmail.com
from turtle import Turtle
import random
import time

class Car(Turtle):
    """Create a Car"""
    def __init__(self,speed_step,position=(0,0),weith=(1,1,2)):
        """Create a Turtle"""
        super().__init__()
        self.speed_step = speed_step
        self.body_color = self.__rgb_light()
        self.change_color()
        self.penup()
        self.shape("square")
        self.speed("fastest")
        self.shapesize(weith[0],weith[1],weith[2])
        self.goto(position)
        self.setheading(180)

    def reset(self,speed_step,position=(0,0),weith=(1,1,2)):
        """Create a Turtle"""
        self.speed_step = speed_step
        self.body_color = self.__rgb_light()
        self.change_color()
        self.shapesize(weith[0],weith[1],weith[2])
        self.goto(position)

    def __rgb_dark(self):
        """Return a random dark rgb color"""
        return (random.randint(1,250), random.randint(1,250), random.randint(1,250))

    def __rgb_light(self):
        """Return a random light rgb color"""
        color = random.choice([
        (random.randint(100,255), random.randint(100,255), random.randint(0,20)),
        (random.randint(100,255), random.randint(0,20), random.randint(100,255)),
        (random.randint(0,20), random.randint(100,255), random.randint(100,255)),
        ])
        return color 

    def change_color(self):
        self.color(self.__rgb_dark(),self.body_color)

    def move(self):
        delete = False
        if -300 <= self.xcor():
            self.forward(self.speed_step)
            self.change_color()
        else:
            self.forward(self.speed_step)
            delete = True
        return delete

class CarManager():
    """Manage Cars"""
    MOVE_STEPS = [1,3,5,7,9]
    WEITH = [(1,1,2),(1,2,2),(1,3,3)]
    y_positions = [-230,-210,-190,-170,-150,-130,-110,-90,-70,-50,-30,-10,
                   10,30,50,70,90,110,130,150,170,190,210,230]
    cars_in_screen = []

    def __init__(self,max_cars=10):
        """Create a number 'max_cars'"""
        self.max_cars = max_cars
        for _ in range(self.max_cars):
            self.new_car()

    def parameters_for_car(self):
        step_speed = random.choice(self.MOVE_STEPS)
        position = (300,random.choice(self.y_positions)) 
        weith = random.choice(self.WEITH)
        list_return = [step_speed,position,weith]

        return list_return

    def new_car(self):
        p = self.parameters_for_car()
        self.cars_in_screen.append(Car(p[0],p[1],p[2]))

    def move(self):
        """Moving all cars"""

        for car in self.cars_in_screen:
                #self.cars_in_screen.remove(car)
            if car.move():
                p = self.parameters_for_car()
                car.reset(p[0],p[1],p[2])

    def level_up(self):
        self.new_car()
        for step_index in range(len(self.MOVE_STEPS)):
            self.MOVE_STEPS[step_index] += 1
            

