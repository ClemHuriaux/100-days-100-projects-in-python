import turtle
MOVE_DISTANCE = 20
DIRECTIONS = {"UP": 90, "DOWN": 270, "LEFT": 180, "RIGHT": 0}
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # get the head in order to control the snake

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # last segment coord.
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_square = turtle.Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)  # Shape of square is 20
        self.segments.append(new_square)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DIRECTIONS["DOWN"]:
            self.head.setheading(DIRECTIONS["UP"])

    def down(self):
        if self.head.heading() != DIRECTIONS["UP"]:
            self.head.setheading(DIRECTIONS["DOWN"])

    def left(self):
        if self.head.heading() != DIRECTIONS["RIGHT"]:
            self.head.setheading(DIRECTIONS["LEFT"])

    def right(self):
        if self.head.heading() != DIRECTIONS["LEFT"]:
            self.head.setheading(DIRECTIONS["RIGHT"])

    def is_lost(self):
        return self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290
