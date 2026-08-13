from turtle import Turtle

class Scoreboad(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 260)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=('Arial', 24, 'normal'))