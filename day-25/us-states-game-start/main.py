import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
write_turtle = turtle.Turtle()
write_turtle.penup()
write_turtle.hideturtle()
df = pd.read_csv("50_states.csv")

correct_guesses = []

while len(correct_guesses) < 50:
    title = f"{len(correct_guesses)}/50 States Correct" if len(correct_guesses) else "Guess the State"
    answer_state = (screen.textinput(title=title, prompt="What's another state's name")).title()

    if answer_state == "Exit":
        not_guessed_states = df[~df["state"].isin(correct_guesses)].state.values
        new_df = pd.DataFrame(not_guessed_states)

        # In the example is just did it with 1 state
        new_df.to_csv("states_to_learn.csv")
        break

    if (df_condition := df["state"] == answer_state).any():
        x = df[df_condition].x
        y = df[df_condition].y
        write_turtle.goto(int(x), int(y))
        write_turtle.write(answer_state, align="center")
        correct_guesses.append(answer_state)



