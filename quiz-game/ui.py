from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=30, pady=30, background=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="helo",
            font=FONT,
            fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.score_label = Label(text="Score:", fg="white", bg=THEME_COLOR, font=10)
        self.score_label.grid(column=1, row=0)
        check_image = PhotoImage(file="images/true.png")
        self.check_button = Button(image=check_image, highlightthickness=0, command=self.true_pressed)
        self.check_button.grid(column=0, row=2)
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the game")
            self.check_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
