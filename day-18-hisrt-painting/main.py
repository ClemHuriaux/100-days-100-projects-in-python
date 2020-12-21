import colorgram
import turtle
import random

turtle.colormode(255)
franklin = turtle.Turtle()

colors = colorgram.extract("image.jpg", 30)
rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors][3:]

franklin.speed("fastest")
franklin.penup()
franklin.hideturtle()
franklin.setheading(225)
franklin.forward(300)
franklin.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    franklin.dot(20, random.choice(rgb_colors))
    franklin.forward(50)

    if dot_count % 10 == 0:
        franklin.setheading(90)
        franklin.forward(50)
        franklin.setheading(180)
        franklin.forward(500)
        franklin.setheading(0)

screen = turtle.Screen()
screen.exitonclick()