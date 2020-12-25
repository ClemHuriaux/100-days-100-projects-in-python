from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_score = -1
        self.create_score()

    def create_score(self):
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.player_score += 1
        self.clear()
        self.goto(x=-280, y=250)
        self.write(f'Level: {self.player_score}', align="left", font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write('Game over !', align="center", font=FONT)
