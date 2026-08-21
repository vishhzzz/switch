from tkinter import *

def button_clicked():
    print("Button got clicked.")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My 1st program.")
window.minsize(width=500, height=300)
# padding to all components.
window.config(padx=20, pady=10)

# Label
my_label = Label(text="I am a label", font=('Arial', 24, 'bold'))
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0) #will not work, becoz it works with reference to other widgets. right now there is no one so it will place at 0, 0.
# same can be done to widgets too
my_label.config(padx=30, pady=20)


# Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# Button 2
button_2 = Button(text='Click Me', command=button_clicked)
button_2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3, row=2)

# if we dont specify any layout then it will not be shown.

# There r 3 diff layout managers
# 1. pack : pack each widgets next to each other in logical format
#           will start from top and will place one below other.
# 2. place : all about precise position. we can specify x, y positions.
#            0,0 means top left corner.
#            its all about positions, very difficult if we have multiple widgets.
# 3. grid : imagine your available screen into n-n grid, divide it into any no. 
#           of rows-columns. We can place it to n col and n row.

# Basically its simple, jo co-ordinate m pehle h wo pehle aaega and then dusre...


window.mainloop()