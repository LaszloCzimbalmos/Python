import math
from tkinter import *
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #

BTN_BG = "#FFBF9B"
DARK_PINK = "#D14D72"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- QUOTES ------------------------------- #

data = pandas.read_csv("quotes.csv")
pandas.DataFrame(data)
quotes_index = 0
quotes = [quote["quote"] for index, quote in data.iterrows() if len(quote["quote"])<41]
random.shuffle(quotes)


def change_quote():
    global quotes_index
    label_quote.config(text=quotes[quotes_index])
    quotes_index += 1
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global timer, mark, reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_check_mark.config(text="")
    label_quote.config(text="You can do it!")
    mark = "✓"
    random.shuffle(quotes)
    quotes_index = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_time_sec = WORK_MIN * 60
    break_time_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(fg=RED, text="Break")
        check_mark()

    elif reps % 2 == 0:
        count_down(break_time_sec)
        label_timer.config(fg=PINK, text="Break")
        check_mark()

    else:
        count_down(work_time_sec)
        label_timer.config(fg=GREEN, text="Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    mins = math.floor(count / 60)
    seconds = count % 60

    if count % 15 == 0:
        change_quote()

    if seconds <= 9:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{mins}:{seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)

    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

mark = "✓"
def check_mark():
    global mark
    label_check_mark.config(text=mark)
    mark += "✓"


# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW, width=500, height=600)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Buttons
start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), borderwidth=1, bg=BTN_BG, command=start_timer, border=2)
start_button.grid(row=3, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), borderwidth=1, bg=BTN_BG, command=reset_timer, border=2)
reset_button.grid(row=3, column=3)

# Labels
label_timer = Label(text="Timer", font=(FONT_NAME, 40, "bold"))
label_timer.config(fg=GREEN, bg=YELLOW, highlightthickness=0)
label_timer.grid(row=0, column=1)

label_check_mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
label_check_mark.grid(row=4, column=1)

label_quote = Label(window, text="You can do it!", bg=YELLOW, fg=DARK_PINK, font=(FONT_NAME, 15, "bold"),
                    wraplength=350, width=30, height=2)

label_quote.grid(row=5, column=1)


window.mainloop()
