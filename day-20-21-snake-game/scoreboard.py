from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.clear_score_and_refresh()

    def clear_score_and_refresh(self):
        self.clear()
        self.score += 1
        self.goto(0, 275)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER ! ", align=ALIGNMENT, font=FONT)