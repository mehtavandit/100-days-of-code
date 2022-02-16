import tkinter

window = tkinter.Tk()
window.title("GUI Practice")
window.minsize(width=500, height=500)
window.config(padx = 20, pady=20) # overall padding

# Label

label_1 = tkinter.Label(text="Label first", font=("Arial", 16, "bold"))
label_1.grid(column = 0, row = 0)  # to show label

label_1["text"] = "Hello User"
label_1["font"] = ("Arial", 16, "italic")
label_1.config(padx = 20, pady=20)


def button_1_click():
    label_1["text"] = input.get()


button_1 = tkinter.Button(text="Intitiate the operation", command=button_1_click)
button_1.grid(column = 1, row = 1)

button_2= tkinter.Button(text="New button", command=button_1_click)
button_2.grid(column = 2, row = 0)

# entry component

input = tkinter.Entry(width=10)
input.grid(column =3,row = 3)

# text box
text = tkinter.Text(height=5, width=30)
text.focus()  # Puts cursor in text box
text.insert(tkinter.END, "Multi-line text entry")
text.pack()

# spinbox
spinbox = tkinter.Spinbox(from_=0, to=25)
spinbox.pack()


# scale
def scale_value(value):
    print(value)


scale = tkinter.Scale(from_=0, to=10, command=scale_value)
scale.pack()
window.mainloop()

# checkbutton
check_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is on?", variable=check_state)
checkbutton.pack()

# radiobutton

radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option 1", variable = radio_state)
radiobutton2 = tkinter.Radiobutton(text="Option 2", variable = radio_state)
radiobutton1.pack()
radiobutton2.pack()

# list box
listbox = tkinter.Listbox(height = 4)
fruits = ["Apple", "Banana", "Orange", "Mango"]
for i in fruits:
    listbox.insert(i)

listbox.pack()

window.mainloop()
