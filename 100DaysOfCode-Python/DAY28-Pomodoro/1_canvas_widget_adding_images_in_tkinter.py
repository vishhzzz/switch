# Canvas widget of tkinter is responsible for adding images on ui.
# allows to layer things on top of others.

# GUI programs r event driven... they actively listen to events on screen.
# This is managed and goverend by mainloop.

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
reps = 0
timer = None

# ------------------------------ TIMER RESET ---------------------------------- # 
def reset_timer():
    global timer, reps
    if timer is not None:
        window.after_cancel(timer)

    canvas.itemconfig(text, text="00:00")
    timer_text.config(text='Timer', font=(FONT_NAME, 35, 'normal'), fg=GREEN)
    tick.config(text="")
    reps = 0
    timer = None

# ----------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps%8 == 0:
        timer_text.config(text='Break', fg=RED)
        count_down(long_break_sec)
    # if its 1, 3, 5, 7
    elif reps%2 != 0:
        timer_text.config(text='Work', fg=GREEN)
        count_down(work_sec)
    else: #2, 4, 6
        timer_text.config(text='Break', fg=PINK)
        count_down(short_break_sec)

# ------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# we cant have another loop in my program for GUI.
# It already runs a loop - mainloop which checks in every ms did something happen.?
# if we add another loop then it will never reach mainloop.

# tkinter has a method named: after.
# it takes amount of time it should wait in ms, then after tht amout of time, it calls another function with/without args.
def count_down(count):
    min = int(count / 60)
    sec = int(count % 60)
    print(min, sec)
    # this is how we get to text of the canvas
    # canvas.itemconfig(text, text=count)

    if sec < 10:
        sec = f"0{sec}"
    if min < 10:
        min = f"0{min}"
    canvas.itemconfig(text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    elif count == 0:
        tick_text = '✅' * ((reps+1)//2) #// int division
        tick.config(text=tick_text)
        start_timer()

# -------------------------------- UI SETUP ----------------------------------- #
# window
window = Tk()
window.title("Pomodoro")
# we r just seeing tomato image.
window.config(padx=100, pady=50, bg=YELLOW)

# Label
timer_text = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'normal'))
timer_text.grid(row=0, column=1)

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
text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))

# Button
# sometimes for button, there is issue: instead of bg, highlightbackground works.
start = Button(text='Start', command=start_timer, highlightbackground=YELLOW)
start.grid(row=2, column=0)

# Label
tick = Label(fg=GREEN, bg=YELLOW)
tick.grid(row=3, column=1)

# Button
reset = Button(text='Reset', command=reset_timer, 
    highlightbackground=YELLOW)
reset.grid(row=2, column=2)

window.mainloop()