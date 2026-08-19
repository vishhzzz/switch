import tkinter #inbuilt

window = tkinter.Tk() #similar to screen of turtle, without holding it will vanish, we hold screen via mainloop()

# title
window.title("My 1st GUI program.")

# normally window will scale to include whatever u defined inside it.
# but we have a property called 'min-size'.
window.minsize(width=500, height=300)

# we also have components that we can put into the screen.
# Label
# showing any component requires 2 things:
# creating a component
my_label = tkinter.Label(text="I am a label.")
# # how do we place it inside the screen.
my_label.pack() #pack will place it into the screen and also centralize it.

my_new_label = tkinter.Label(text="I am a new label.", font=("Arila", 24, "bold"))
my_new_label.pack(side='bottom')

my_newest_label = tkinter.Label(text="I am a newest label.", font=("Arila", 24, "bold"))
# expand = True will take whatever space it has. Center p place krta h.
my_newest_label.pack(expand=True)


# always at the end.
# bts: it actively listens for any event/anything that user will be doing, in while loop
window.mainloop() #hold the screen


# the arguement list of pack or label shows kwargs, simply they dont show the whole bunch of args possible.