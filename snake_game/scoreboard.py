from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.ht()
        self.penup()
        self.goto(x=0, y=250)
        with open("data.txt") as data:
            self.highest = int(data.read())
        self.write("Score: 0, Highest score: 0", False, align="center", font=FONT)
        self.score = 0

    def reset(self):
        self.clear()
        if self.score > self.highest:
            self.highest = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.highest))
        self.score = 0
        self.write(f"Score: {self.score}, Highest score: {self.highest}", False, align=ALIGNMENT, font=FONT)

    def plus_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}, Highest score: {self.highest}", False, align=ALIGNMENT, font=FONT)