THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.canvas_text = Canvas(width=300, height=250, bg="white")
        self.c_text = self.canvas_text.create_text(150, 125, text="hello world", width=280, font=("Ariel", 20, "italic"), fill=THEME_COLOR)
        self.canvas_text.grid(column=0, row=1, columnspan=2, pady=50)

        self.check = PhotoImage(file="./images/true.png")
        self.yes_butt = Button(image=self.check, highlightthickness=0, command=self.choose_true)
        self.yes_butt.grid(column=0, row=2)
        self.no = PhotoImage(file="./images/false.png")
        self.no_butt = Button(image=self.no, highlightthickness=0, command=self.choose_false)
        self.no_butt.grid(column=1, row=2)

        self.label = Label(text="Score:0", fg="white", bg=THEME_COLOR)
        self.label.grid(column=1, row=0)


        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas_text.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            qtext = self.quiz.next_question()
            self.canvas_text.itemconfig(self.c_text, text=qtext)
        else:
            self.canvas_text.itemconfig(self.c_text, text="You have reached the end of the questions")
            self.yes_butt.config(state="disable")
            self.no_butt.config(state="disable")
    def choose_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def choose_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas_text.config(bg="green")
        else:
            self.canvas_text.config(bg="red")
        self.window.after(1000, func=self.get_next_question)

