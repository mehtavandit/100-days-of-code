from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    terms_to_learn = data.to_dict(orient="records")
    current_term = {}


def next_term():
    global current_term, flip_time
    window.after_cancel(flip_time)
    current_term=random.choice(terms_to_learn)
    french_term = current_term["French"]
    canvas.itemconfig(photo, image_=front_photo)
    canvas.itemconfig(french_word_on_canvas, text="French", fill = "black")
    canvas.itemconfig(english_word_on_canvas, text=french_term, fill="black")
    flip_time = window.after(3000, func=turn_card)


def turn_card():

    english_term = current_term["English"]
    canvas.itemconfig(photo, image_=back_photo)
    canvas.itemconfig(french_word_on_canvas, text="English", fill="white")
    canvas.itemconfig(english_word_on_canvas, text=english_term, fill="white")


def correct():
    terms_to_learn.remove(current_term)
    data = pandas.DataFrame(terms_to_learn)
    data.to_csv("data/words_to_learn.csv", index = False)
    print(len(terms_to_learn))
    next_term()


window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_time = window.after(3000, func=turn_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_photo = PhotoImage(file="images/card_front.png")
back_photo = PhotoImage(file="images/card_back.png")
photo = canvas.create_image(400, 263, image=front_photo)
french_word_on_canvas = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
english_word_on_canvas = canvas.create_text(400, 263, text="Answer", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, borderwidth=0, command=next_term)
wrong_button.grid(row=1, column=0)

right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, borderwidth=0, command=correct)
right_button.grid(row=1, column=1)

next_term()

window.mainloop()
