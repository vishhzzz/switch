from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

with open("Day24-Files_Directories_PATH/high_score.txt", 'r') as file:
    high_score = file.read()

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(high_score)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self): # we dont need this anymore, we need to reset the game.
    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Day24-Files_Directories_PATH/high_score.txt", 'w+') as file:
                file.write(str(self.high_score))
        # self.clear()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        # self.clear() #right now we r using it at 2 places here and in reset game so instead we can write this at one place and remove from others.
        self.update_scoreboard()

    def end_game(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
        with open("Day24-Files_Directories_PATH/high_score.txt", 'w+') as file:
            file.write(self.high_score)
