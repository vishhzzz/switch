from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=100)

# label
converter_text = Label(text='is equal to')
converter_text.grid(row=1, column=0)

# input text
input = Entry(width=10)
input.grid(row=0, column=1)

# label
value = Label(text=0)
value.grid(row=1, column=1)

def button_clicked():
    # pass
    miles = int(input.get())
    miles_to_km = miles * 1.60934
    value.config(text=miles_to_km)

# button
button = Button(text='Calculate', command=button_clicked)
button.grid(row=3, column=1)

# label
miles = Label(text='Miles')
miles.grid(row=0, column=2)

# label
km = Label(text='Km')
km.grid(row=1, column=2)

window.mainloop()