import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

pad1 = Paddle(1)
pad2 = Paddle(2)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(pad1.up, "z")
screen.onkey(pad1.down, "s")
screen.onkey(pad2.up, "Up")
screen.onkey(pad2.down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(pad2) < 40 and ball.xcor() > 320 or ball.distance(pad1) < 40 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect misses
    if (cords := ball.xcor()) > 380 or (cords := ball.xcor()) < -380:
        ball.reset_position()
        scoreboard.add_points(cords)


screen.exitonclick()
