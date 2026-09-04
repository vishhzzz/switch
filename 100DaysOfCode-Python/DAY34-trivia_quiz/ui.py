'''
We attach self to those which we were gonna use later.
'''


# we will UI but in class style

# import tkinter or
from tkinter import *
from PIL import Image, ImageTk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
MY_FONT = ('Arial', 20, 'italic')

class Quizzler:

    # we could have just passed quiz but by doing this we r helping user as now if someone tries to pass something other than quizbrain then it will get an error and also
    # by doing this: user gets to see all the methods of this class in this file while writing.
    def __init__(self, quiz : QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title('Quizz App')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
    

        self.label = Label(text='Score: 0', font=MY_FONT, fg='white', bg=THEME_COLOR)
        self.label.grid(row=0, column=1)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg='white')
        self.text = self.canvas.create_text(
            150, 
            125,
            width=280,#text-wrap : question will not go out of boundaries
            text='dummy_text', 
            font=MY_FONT, 
            fill=THEME_COLOR
        ) #fill is color of text.
        self.canvas.grid(row=1, column=0, columnspan=2, pady= 50)

        true = Image.open('./DAY34-trivia_quiz/images/true.png')
        true = true.resize((100, 100))
        true = ImageTk.PhotoImage(true)

        false = Image.open('./DAY34-trivia_quiz/images/false.png')
        false = false.resize((100, 100))
        false = ImageTk.PhotoImage(false)

        true_button = Button(self.window, image=true, command=self.true_clicked, highlightthickness=0)
        true_button.grid(row=2, column=0)
        false_button = Button(self.window, image=false, command=self.false_clicked, highlightthickness=0)
        false_button.grid(row=2, column=1)

        # fetch and display next question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.text, text=q_text)

    def true_clicked():
        pass
    def false_clicked():
        pass