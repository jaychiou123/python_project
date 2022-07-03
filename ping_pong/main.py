from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Paddle setup
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# Screen listen
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "x")
# Scoreboard setup
scoreboard = Scoreboard()

# Draw middle line
tim = Turtle()
tim.goto(x=0, y=270)
tim.hideturtle()
tim.setheading(270)
tim.color("white")
tim.pensize(5)
while tim.distance((0, -270)) > 5:
    tim.pendown()
    tim.forward(15)
    tim.penup()
    tim.forward(15)
# Ball setup
ball = Ball()


flag = True
while flag:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()
    # hit top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_horizontal()
    # hit paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_vertical()

    # right miss
    if ball.xcor() > 380:
        ball.reset_lw()
        scoreboard.l_point()
    # left miss
    if ball.xcor() < -380:
        ball.reset_rw()
        scoreboard.r_point()





















screen.exitonclick()