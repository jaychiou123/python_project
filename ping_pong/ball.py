from turtle import Turtle
import time
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.new_heading = random.randint(0, 360)
        self.move_speed = 0.1
    def move(self):
        self.setheading(self.new_heading)
        self.fd(20)

    def bounce_horizontal(self):
        self.new_heading = self.heading()*(-1)

    def bounce_vertical(self):
        self.new_heading = 180 - self.heading()
        self.move_speed *= 0.9

    def reset_lw(self):
        self.goto(0, 0)
        self.new_heading += random.randint(115, 255)
        self.move_speed = 0.1

    def reset_rw(self):
        self.goto(0, 0)
        self.new_heading += random.randint(-75, 75)
        self.move_speed = 0.1