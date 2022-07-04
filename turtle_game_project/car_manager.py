from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.segments=[]
        
    def spawn(self, x, y):
        rand_number = random.randint(1,6)
        if rand_number == 1:
            turtle = Turtle(shape="square")
            turtle.shapesize(stretch_len=2, stretch_wid=1)
            turtle.color(random.choice(COLORS))
            turtle.pu()
            turtle.setheading(180)
            turtle.goto(x, y)
            self.segments.append(turtle)

    def car_move(self):
        for i in self.segments:
            i.fd(STARTING_MOVE_DISTANCE)