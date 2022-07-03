from turtle import Turtle
import pandas
data = pandas.read_csv("50_states.csv")

class Data(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.state = data.state.to_list()
    def find_location(self, answer):
        """return x,y tuple"""
        x_location = int(data[data.state == answer].x)
        y_location = int(data[data.state == answer].y)
        return (x_location, y_location)

    def set_location(self, answer):
        self.penup()
        self.goto(self.find_location(answer))
        self.write(answer, move="False", align="center", font=['Arial', 8, 'normal'])

