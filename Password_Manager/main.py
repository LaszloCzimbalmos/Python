from tkinter import *
from tkinter import messagebox
import random
import json

# constants
BG = "#B7C4CF"
ENTRY_BG = "#E5B299"
BUTTON_BG = "#D27685"
DEFAULT_EMAIL = "sample@mail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_gen():
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$', '%', '^', '&', '*',
            '(', ')', '-', '_', '=', '+','[', ']', '{', '}', ';', ':',',', '.', '<', '>', '/', '?', '|']

    pw = random.choices(nums, k=12)
    str_pw = ''.join(pw)
    entry_password.delete(0, END)
    entry_password.insert(0, str_pw)

# ---------------------------- SAVE/SHOW PASSWORD ------------------------------- #

def save_data():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()
    data_line = f"{website} | {username} | {password}\n"

    new_data = {
        website: {
            "username": username,
            "password": password,
        }

    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please fill in every field!")

    else:
        is_ok = messagebox.askokcancel(title="Save Data", message=f"Want to save?\n{data_line}")

        if is_ok:
            try:
                with open("data.json", "r") as data:
                    loaded = json.load(data)
            except FileNotFoundError:
                with open("data.json", "w") as data:
                    json.dump(new_data, data, indent=4)
            else:
                loaded.update(new_data)
                with open("data.json", "w") as data:
                    json.dump(loaded, data, indent=4)
            finally:
                entry_password.delete(0, END)
                entry_website.delete(0, END)


def show_data():
    with open("data.json", "r") as file:
        data = json.load(file)

    out = "\n".join(list(data))
    new_window = Toplevel(window, height=300, width=300, pady=20, padx=20, bg=BG)
    label_data = Label(new_window, text=f"Saved websites:\n{out}", bg=BG, font=("Inter", 12, "bold"), justify="left")
    label_data.grid(row=0, column=0, sticky=W)


def find_password():
    try:
        with open("data.json", "r") as data:
            website = entry_website.get()
            dict = json.load(data)
            values = list(dict[website].values())
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="The database is empty.\nTry to add new data.")
    except KeyError:
        messagebox.showinfo(title="Not Found", message="The searched website is not found.")
    else:
        values = list(dict[website].values())
        messagebox.showinfo(title=website, message=f"username/email: {values[0]}\npassword: {values[1]}")



# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.config(padx=20, pady=20, bg=BG)
window.title("Password Manager")


# canvas
canvas = Canvas(height=200, width=200, bg=BG, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=1, column=1)


# labels
label_website = Label(text="Website:", font=("Inter", 12, "bold"), bg=BG)
label_website.grid(row=2, column=0, sticky=E)

label_username = Label(text="Email/Username:", font=("Inter", 12, "bold"), bg=BG)
label_username.grid(row=3, column=0, sticky=E)

label_password = Label(text="Password:", font=("Inter", 12, "bold"), bg=BG)
label_password.grid(row=4, column=0, sticky=E)


# entries
entry_website = Entry(width=22, bg=ENTRY_BG)
entry_website.grid(row=2, column=1, columnspan=2, sticky=W)
entry_website.focus()

entry_username = Entry(width=36, bg=ENTRY_BG)
entry_username.grid(row=3, column=1, columnspan=2)
entry_username.insert(0, DEFAULT_EMAIL)

entry_password = Entry(width=22, bg=ENTRY_BG)
entry_password.grid(row=4, column=1, sticky=W, columnspan=2)


# buttons
button_search = Button(width=14, bg=BUTTON_BG, text="Search", font=("Inter", 6, "bold"), command=find_password)
button_search.grid(row=2, column=1, columnspan=2, sticky=E)

button_generate_pw = Button(width=14, bg=BUTTON_BG, text="Generate Password", font=("Inter", 6, "bold"), command=password_gen)
button_generate_pw.grid(row=4, column=1, columnspan=2, sticky=E)

button_add = Button(width=30, bg=BUTTON_BG, text="Add", font=("Inter", 9, "bold"), command=save_data)
button_add.grid(row=5, column=1, columnspan=3, sticky=W)

button_show_data = Button(width=15, bg=BUTTON_BG, text="Show Websites", font=("Inter", 8, "bold"), command=show_data)
button_show_data.grid(row=0, column=0, sticky=NW)

window.mainloop()
