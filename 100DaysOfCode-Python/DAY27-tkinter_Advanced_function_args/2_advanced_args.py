import tkinter

window = tkinter.Tk()

# title
window.title("My 1st GUI program.")

window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a label.")
my_label.pack()

my_new_label = tkinter.Label(text="I am a new label.", font=("Arila", 24, "bold"))
my_new_label.pack(side='bottom')

my_newest_label = tkinter.Label(text="I am a newest label.", font=("Arila", 24, "italic"))
# expand = True will take whatever space it has. screen k center p place krta h.
my_newest_label.pack(expand=True)

window.mainloop() #hold the screen

# There is something called 'Advanced Arguements'
# These r nothing but optional args., which r not necessary to provide and hence is not shown in function description. They r simply taken care of by args, kwargs.

# We can set default arguements:
# in function definition, we set the arguements value
# def my_funct(a=1, b, x):
# pass