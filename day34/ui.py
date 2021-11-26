import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizzInterface():
    def __init__(self,quiz_brain:QuizBrain) -> None:
        # quiz_brain:QuizBrain, here we specify the type of parameter
        # in this case, we're especifing the qui_brain as QuizBrain object
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler! By Rychy!")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.labels()
        self.canvas()
        self.buttons()
        
        self.get_next_question()

        self.window.mainloop()

    def labels(self):
        self.score_var = tkinter.StringVar(value="Score: 0")
        self.score_label = tkinter.Label(
            textvariable=self.score_var,
            fg="white",
            bg=THEME_COLOR
            )
        self.score_label.grid(row=0, column=0)

        self.question_var = tkinter.StringVar(value="Question Num: 0/10")
        self.question_num = tkinter.Label(
            textvariable=self.question_var,
            fg="white",
            bg=THEME_COLOR
            )
        self.question_num.grid(row=0, column=1)

    def canvas(self):
        self.canvas = tkinter.Canvas(
            width=300, 
            height=250,
            bg="white"
            )
        self.question_text = self.canvas.create_text(
            150,125, #are x and y position in canvas
            width=200,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial",15,"italic")
            )
        self.canvas.grid(row=1,column=0, columnspan=2, pady=50)
    
    def buttons(self):
        self.true_image = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(
            image=self.true_image,
            highlightthickness=0,
            command=self.true_button_pressed
            )
        self.true_button.grid(row=2,column=0)

        self.false_image = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(
            image=self.false_image,
            highlightthickness=0,
            command=self.false_button_pressed
            )
        self.false_button.grid(row=2,column=1)
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text,fill=THEME_COLOR)

        if self.quiz.still_has_questions():
            quiz = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=f"{quiz}")
        else:
            self.canvas.itemconfig(
                self.question_text,
                text="You've reached the end of the quiz."
                )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def true_button_pressed(self) -> None:
        self.refresh_score(self.quiz.check_answer("True"))

    def false_button_pressed(self) -> None:
        self.refresh_score(self.quiz.check_answer("False"))

    def refresh_score(self,is_right:bool):
        score_txt = f"Score: {self.quiz.score}"
        question_txt = f"Question Num: {self.quiz.question_number}/10"
        self.score_var.set(score_txt)
        self.question_var.set(question_txt)
    
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.itemconfig(self.question_text,fill="white")

        self.window.after(1000,self.get_next_question)
