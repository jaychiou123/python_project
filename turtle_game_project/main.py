import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

# Screen initialize
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
# player initialize
player = Player()
# Scoreboard initialize
scoreboard = Scoreboard()
# Carmanageer initialize
car_manager = CarManager()
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(scoreboard.time_delay)
    screen.update()
    y_new = random.randint(-250, 300)
    car_manager.spawn(300, y_new)
    car_manager.car_move()
    # corss end line
    if player.ycor() > 290:
        player.restart()
        scoreboard.arrive_line()
    # game over condition
    for i in car_manager.segments:
        if player.distance(i) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()