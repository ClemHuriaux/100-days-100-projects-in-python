from tkinter import *
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
TITLE_CARD = {"Position": (400, 150), "Text": ("Arial", 40, "italic")}
WORD_CARD = {"Position": (400, 263), "Text": ("Arial", 60, "bold")}
df_cards = ""
TIME_TO_ANSWER = 3000
current_card = {}
# TODO 1: Add a "no card left" message


def word_list_to_use():
    global df_cards
    try:
        df_cards = pd.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        df_cards = pd.read_csv("data/french_words.csv")
    except pd.errors.EmptyDataError:
        df_cards = pd.read_csv("data/french_words.csv")


def pick_card(is_right=False):
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = df_cards.sample().to_dict(orient="index")
    if is_right:
        df_cards.drop(current_card.keys(), inplace=True)
        df_cards.to_csv("data/words_to_learn.csv", index=False)
    current_card = list(current_card.values())[0]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(canvas_image, image=card_img_front)
    flip_timer = window.after(3000, func=change_side)


def change_side():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(canvas_image, image=card_img_back)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
word_list_to_use()

flip_timer = window.after(3000, func=change_side)

canvas = Canvas(width=800, height=526)
card_img_front = PhotoImage(file="images/card_front.png")
card_img_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_img_front)
card_title = canvas.create_text(TITLE_CARD["Position"], text="Title", font=TITLE_CARD["Text"])
card_word = canvas.create_text(WORD_CARD["Position"], text="word", font=WORD_CARD["Text"])
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


right_img_button = PhotoImage(file="images/right.png")
wrong_img_button = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_img_button, highlightthickness=0, command=lambda: pick_card(True))
wrong_button = Button(image=wrong_img_button, highlightthickness=0, command=pick_card)

right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)
pick_card()
window.mainloop()
