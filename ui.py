from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


# creates a QuizInterface class to handle the GUI
class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        # configures canvas
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250)
        # displays question text
        self.question_text = self.canvas.create_text(150, 125, text="Question", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"), width=280)
        # assigns true and false images
        true = PhotoImage(file=r"images/true.png")
        false = PhotoImage(file=r"images/false.png")
        # creates true and false buttons
        self.true_button = Button(image=true, highlightthickness=0, command=self.true)
        self.false_button = Button(image=false, highlightthickness=0, command=self.false)
        # creates a label for displaying the score
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Calibri", 15, "bold"))
        # arranges the widgets
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        self.score_label.grid(row=0, column=1)
        self.get_next_question()

        self.window.mainloop()

    # updates the score and text of the question
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            # buttons are made active to allow the user to answer the questions
            self.buttons_state("active")
        else:
            # if no questions are remaining, updates the text and score
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz!")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            # disables the buttons to prevent the user from pressing them and giving an answer
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    # checks answer when user presses 'True'
    def true(self):
        self.buttons_state("disabled")
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    # checks answer when user presses 'False'
    def false(self):
        self.buttons_state("disabled")
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    # changes the background based on the accuracy of the answer
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # gets the next question
        self.window.after(1000, self.get_next_question)

    def buttons_state(self, state:str):
        self.true_button.config(state=state)
        self.false_button.config(state=state)
