from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
CANVAS_SIZE = (300, 250)  # width, height


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizlet")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=CANVAS_SIZE[0], height=CANVAS_SIZE[1], bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="Some Question Text",
                                                     fill=THEME_COLOR,
                                                     font=FONT,
                                                     width=280)  # 280 to wrap the text
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        right_img_button = PhotoImage(file="images/true.png")
        wrong_img_button = PhotoImage(file="images/false.png")
        self.right_button = Button(image=right_img_button, highlightthickness=0, command=self.true_pressed)
        self.wrong_button = Button(image=wrong_img_button, highlightthickness=0, command=self.false_pressed)
        self.right_button.grid(column=0, row=2)
        self.wrong_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz !")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            color = "green"
        else:
            color = "red"
        self.canvas.config(bg=color)
        self.window.after(1000, self.get_next_question)
