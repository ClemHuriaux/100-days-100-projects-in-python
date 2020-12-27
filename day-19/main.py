import turtle
import random as r

is_race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


# TODO: add a restart system
def clear(message, winning):
    screen.textinput(title=message, prompt=f"The {winning} turtle won the race ! Press any key to close the game")
    turtle.done()


for turtle_index in range(0, 6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                clear(f"You've won !", winning_color)
            else:
                clear(f"You've lost !", winning_color)
                screen.textinput(title="You've lost !", prompt="You can exit now")
        rand_distance = r.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
