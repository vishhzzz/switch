import tkinter

window = tkinter.Tk()
window.title("My 1st GUI")

window.minsize(width=500, height=300)

my_label = tkinter.Label(text='I am a label', font=("Arial", 24, "bold"))
my_label.pack()

# changing args...
my_label.config(text="New Text") #either this
my_label['text'] = "Newest Text"

# event listener - button click
def button_click():
    print("I got called...")
    # i needed to do: 'change label txt to 'my button got clicked' when clicked on button.'
    my_label['text'] = "Button got Clicked"
    my_label.config(text=input.get())

# button
button = tkinter.Button(text="Click Me", command=button_click) #just need function name hence no ()
button.pack()


# entry or user input
input = tkinter.Entry(width=10)
input.pack()
# to hold the value that come via Entry.
print(input.get())


window.mainloop()