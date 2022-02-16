from tkinter import *

window = Tk()
window.title("Miles to KM converter")
window.config(pady=30)

# miles input
miles_input = Entry(width = 10)
miles_input.grid(column = 2, row =0)

miles_label = Label(text = "  Miles ")
miles_label.grid(column = 3, row = 0)

to_label = Label(text = "  Is equal to ")
to_label.grid(column = 0, row = 2)

# km result label
km_result_label = Label(text = "0")
km_result_label.grid(column = 2, row = 2)

km_label = Label(text = "  Kms ")
km_label.grid(column = 3, row = 2)

def process():
    miles_value = int(miles_input.get())
    km_value = miles_value * 1.6
    km_result_label["text"] = km_value

#button
calc= Button(text="Calculate", command= process)
calc.grid(column = 2, row = 4)

window.mainloop()
