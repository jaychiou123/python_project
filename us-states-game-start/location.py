from turtle import Turtle
import pandas
data = pandas.read_csv("50_states.csv")

class Data(Turtle):
    def __init__(self, answer):
        super().__init__()
        self.answer = answer
    def find_location(self):
        """return x,y tuple"""
        x_location = int(data[data.state == self.answer].x)
        y_location = int(data[data.state == self.answer].y)
        return (x_location, y_location)

    def set_location(self):
        self.penup()
        self.goto(self.find_location())
        self.hideturtle()
        self.write(self.answer, move="False", align="center", font=['Arial', 8, 'normal'])
