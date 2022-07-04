from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        self.time_delay = 0.1
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(-220, 250)
        self.level = 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def arrive_line(self):
        self.clear()
        self.time_delay *= 0.9
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)
