from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
            if inside := f.read():
                self.high_score = int(inside)
            else:
                self.high_score = 0
        self.goto(0, 275)
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_in_file(self.high_score)
        self.score = 0
        self.update_scoreboard()

    @staticmethod
    def write_in_file(high_score):
        with open("data.txt", "w") as f:
            f.write(str(high_score))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
