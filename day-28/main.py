from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.1
reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    reps = 1
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    if reps == 8:
        time_to_count = LONG_BREAK_MIN * 60
        title_label.config(text="Break", fg=RED)
        reps += 1
    elif reps % 2 == 0:
        time_to_count = SHORT_BREAK_MIN * 60
        reps += 1
        title_label.config(text="Break", fg=PINK)
    else:
        time_to_count = WORK_MIN * 60
        reps += 1
        title_label.config(text="Work", fg=GREEN)
    count_down(time_to_count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    formatted_time = time.strftime("%M:%S", time.gmtime(count))
    canvas.itemconfig(timer_text, text=formatted_time)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    if reps % 2 != 0:
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
