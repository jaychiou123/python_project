from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
screen = Screen()
screen.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    my_tuple = (r, g, b)
    tim.pencolor(my_tuple)
heading = 0
tim.speed("fastest")
while heading < 360:
    random_color()
    tim.circle(50)
    heading += 1
    tim.setheading(heading)
    # choose_dir()
























screen.exitonclick()
