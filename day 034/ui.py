from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class UserInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score : 0", fg="white", bg=THEME_COLOR, font=(20))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,width=280, text="Some question text", fill=THEME_COLOR, font=("Arial",18,"italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        check_mark_image = PhotoImage(file="images/true.png")
        self.check_mark = Button(image=check_mark_image, highlightthickness=0, command=self.check_mark_pressed, border=0)
        self.check_mark.grid(row=2, column=0)

        cross_mark_image = PhotoImage(file="images/false.png")
        self.cross_mark = Button(image=cross_mark_image, highlightthickness=0, command=self.cross_mark_pressed, border=0)
        self.cross_mark.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.check_mark.config(state="disabled")
            self.cross_mark.config(state="disabled")


    def check_mark_pressed(self):
        is_correct = self.quiz.check_answer("True")
        print(is_correct)
        self.feedback(is_correct)

    def cross_mark_pressed(self):
        is_correct = self.quiz.check_answer("False")
        print(is_correct)
        self.feedback(is_correct)

    def feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)