from turtle import Turtle
PADDLE_WIDTH = 5
PADDLE_HEIGHT = 1
STARTING_POSITIONS = {"Player1": (-350, 0), "Player2": (350, 0)}
MOVE_UNIT = 20


class Paddle(Turtle):

    def __init__(self, player_number):
        super().__init__()
        self.create_paddle(player_number)

    def create_paddle(self, player_number):
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
        if player_number == 1:
            self.goto(STARTING_POSITIONS["Player1"])
        elif player_number == 2:
            self.goto(STARTING_POSITIONS["Player2"])
        else:
            raise ValueError("You did not specified a correct player's number")

    def up(self):
        new_y = self.ycor() + MOVE_UNIT
        self.goto(x=self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - MOVE_UNIT
        self.goto(x=self.xcor(), y=new_y)
