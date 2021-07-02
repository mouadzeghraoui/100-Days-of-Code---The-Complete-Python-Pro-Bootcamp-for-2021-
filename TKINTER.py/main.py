from tkinter import *


def action():
    miles = entry.get()
    km = float(miles) * 1.61
    my_label_4.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=100, width=200)
window.config(padx=20, pady=20)

# Entries
entry = Entry(width=5)
entry.insert(INSERT, string="0")
entry.grid(column=1, row=1)
#
my_label_1 = Label(text="Miles", font=("arial", 24))
my_label_1.config(text="Miles")
my_label_1.grid(column=2, row=1)
#
my_label_2 = Label(text="is equal to", font=("arial", 24))
my_label_2.config(text="is equal to")
my_label_2.grid(column=1, row=2)


# Entries
my_label_4 = Label(text="0", font=("arial", 18))
my_label_4.grid(column=2, row=2)

my_label_3 = Label(text="Km", font=("arial", 24))

my_label_3.grid(column=3, row=2)

# Button
button = Button(text="Calculate", command=action)
button.grid(column=2, row=3)


window.mainloop()
