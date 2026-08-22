# Canvas widget of tkinter is responsible for adding images on ui.
# allows to layer things on top of others.

from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# 8800483748
# ------------------------------ TIMER RESET ---------------------------------- # 

# ----------------------------- TIMER MECHANISM ------------------------------- # 

# ------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# -------------------------------- UI SETUP ----------------------------------- #
# window
window = Tk()
window.title("Pomodoro")
# we r just seeing tomato image.
window.config(padx=100, pady=50, bg=YELLOW)

# Label
timer = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'normal'))
timer.grid(row=0, column=1)

# canvas
canvas = Canvas()

# we can set this in constructor also and can later modify too.
# highlightthickness is to remove border across the image.
canvas.config(width=200, height=224, bg=YELLOW, highlightthickness=0)

# canvas requires photo in form of photo image not as path to image.
img = PhotoImage(file='./DAY28-Pomodoro/tomato.png')

# we have devloped the screen of canvas, now its time to add image on top of it.
canvas.create_image(100, 112, image=img)
canvas.grid(row=1, column=1)

# adding text on top of image
canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))

def button_clicked_start():
    pass

def button_clicked_reset():
    pass

# Button
# sometimes for button, there is issue: instead of bg, highlightbackground works.
start = Button(text='Start', command=button_clicked_start, highlightbackground=YELLOW)
start.grid(row=2, column=0)

# Label
tick = Label(text='✅', fg=GREEN, bg=YELLOW)
tick.grid(row=3, column=1)

# Button
reset = Button(text='Reset', command=button_clicked_reset, 
    highlightbackground=YELLOW)
reset.grid(row=2, column=2)

window.mainloop()