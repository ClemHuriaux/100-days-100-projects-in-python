from turtle import Turtle
SCORE_POSITIONS = {"Player1": (-100, 200), "Player2": (100, 200)}


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_1 = 0
        self.player_2 = 0
        self.create_score()

    def create_score(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(SCORE_POSITIONS["Player1"])
        self.write(self.player_1, align="center", font=("Courier", 80, "normal"))
        self.goto(SCORE_POSITIONS["Player2"])
        self.write(self.player_2, align="center", font=("Courier", 80, "normal"))

    def add_points(self, cords):
        if cords > 380:
            self.player_1 += 1
        elif cords < -380:
            self.player_2 += 1
        self.update_scoreboard()
