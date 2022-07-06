from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)


# Label, font=("Arial", 24, "bold")
my_label = Label(text="Miles")
my_label.grid(column=2, row=0)

my_label_1 = Label(text="is equal to")
my_label_1.grid(column=0, row=1)

my_label_2 = Label(text="0")
my_label_2.grid(column=1, row=1)

my_label_3 = Label(text="Km")
my_label_3.grid(column=2, row=1)

def button_clicked():
    km = int(input.get())*1.6
    my_label_2.config(text=km)
# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


# Entry

input = Entry(width=10)
input.grid(column=1, row=0)
input.focus()
print(input.get())





















window.mainloop()