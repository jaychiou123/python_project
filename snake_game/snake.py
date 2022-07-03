from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.segments.append(turtle)

    def reset(self):
        for i in self.segments:
            i.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())           # add a segment at the last segment position

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):  # if len = 2, seg = 2, 1
            x_new = self.segments[seg - 1].xcor()
            y_new = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_new, y_new)
        self.segments[0].fd(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)