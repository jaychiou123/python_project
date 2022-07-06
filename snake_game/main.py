from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

flag = True
while flag:
    time.sleep(0.1)
    screen.update()
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.plus_score()


    # Detect collision with wall
    if snake.head.xcor() > 280 or  snake.head.xcor() < -280 or  snake.head.ycor() > 280 or  snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()















screen.exitonclick()
