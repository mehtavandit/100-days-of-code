from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# *********************************************************** Password Generator *********************************************************** #


def create_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# *********************************************************** Writing to file *********************************************************** #


def save():
    website = website_input.get().lower()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please fill all the fields")
    else:
        is_data_correct = messagebox.askokcancel(title=f"{website}",
                                                 message=f"These are the detail entered\nEmail: {email}\nPassword: {password}\nIs the information correct? ")
        if is_data_correct:
            try:
                with open("data.json","r") as file:
                    data = json.load(file)
                    # print(data)
                    data.update(new_data)
                    # print(data)

            except FileNotFoundError:
                with open("data.json","w") as file:
                    json.dump(new_data, file, indent=4)

            else:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)

# *********************************************************** Searching for the password *********************************************************** #

def search():
    website = website_input.get().lower()

    try:
        with open("data.json", "r") as file:
            data=json.load(file)
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            # print(data[website]["email"])
            # print(email)
            # print(password)
    except KeyError:
        messagebox.showinfo(title="Error", message="Password of this website is not stored in the database")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Your database is empty")


# *********************************************************** GUI *********************************************************** #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(110, 100, image=photo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)

# website_input = Entry(width=40)
# website_input.grid(row=1, column=1, columnspan=2)
# website_input.focus()
website_input = Entry(width=33)
website_input.grid(row=1, column=1)

search_button = Button(text="Search", padx=32, command = search)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
#
email_input = Entry(width=52)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "xyz@gmail.com")

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

password_input = Entry(width=33)
password_input.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=create_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
