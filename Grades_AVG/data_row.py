import tkinter
from tkinter import messagebox
TITLE_FONTS = ("Times New Roman", 12, "bold")
BUTTON_FONTS = ("Times New Roman", 8, "bold")
BG = "#116D6E"
ENTRY_COLOR = "#DFD3C3"
BUTTON_COLOR = "#85586F"


class DataRow:
    def __init__(self, win):
        self.win = win
        self.grade_ratio = 0
        self.sum_credits = 0
        self.index = 1
        self.row = 1

        self.entry_name = tkinter.Entry(width=8)
        self.entry_credit = tkinter.Entry(width=8)
        self.entry_grade = tkinter.Entry(width=8)

        self.button_add = tkinter.Button(width=5, text="Add", command=self.collect_data)
        self.button_print = tkinter.Button(width=7, text="Calculate", command=self.print_data)
        self.button_new = tkinter.Button(text="New", width=5, height=1, command=lambda: self.clear(new_win=self.win))

        self.add_data_row()


    def add_data_row(self):
        label_index = tkinter.Label(text=str(self.index))
        label_index.grid(row=self.row, column=0)
        label_index.config(bg=BG, font=BUTTON_FONTS)

        self.entry_name = tkinter.Entry(width=8)
        self.entry_name.grid(row=self.row, column=1)
        self.entry_name.config(background=ENTRY_COLOR)
        self.entry_name.insert(0, f"Subject_{self.index}")
        self.entry_name.select_range(0, tkinter.END)
        self.entry_name.focus()

        self.entry_credit = tkinter.Entry(width=8)
        self.entry_credit.grid(row=self.row, column=2)
        self.entry_credit.config(background=ENTRY_COLOR)

        self.entry_grade = tkinter.Entry(width=8)
        self.entry_grade.grid(row=self.row, column=3)
        self.entry_grade.config(background=ENTRY_COLOR)

        self.button_add.grid(row=self.row, column=4)
        self.button_add.config(background=BUTTON_COLOR, font=BUTTON_FONTS)
        self.button_print.grid(row=self.row, column=5)
        self.button_print.config(background=BUTTON_COLOR, font=BUTTON_FONTS)
        self.button_new.grid(row=0, column=4)
        self.button_new.config(background=BUTTON_COLOR, font=BUTTON_FONTS)
        self.row += 1
        self.index += 1



    def collect_data(self):
        try:
            grade = int(str(self.entry_grade.get()))
            credit = int(str(self.entry_credit.get()))
        except ValueError:
            messagebox.showinfo(title="Input Error", message="Give a valid number!")

        self.grade_ratio += grade * credit
        self.sum_credits += credit
        self.add_data_row()

    def print_data(self):
        try:
            grade = int(str(self.entry_grade.get()))
            credit = int(str(self.entry_credit.get()))
        except ValueError:
            messagebox.showinfo(title="Input Error", message="Give a valid number!")

        self.grade_ratio += grade * credit
        self.sum_credits += credit

        avg = self.grade_ratio / self.sum_credits
        line = f"Average: {round(avg, 2)}"
        messagebox.showinfo(title="Your Average", message=line)

    def clear(self, new_win):
        new_win.destroy()
        new_win = tkinter.Tk()

        new_win.title("Calculate your Grade-Point-Average")
        new_win.config(width=600, height=500, padx=20, pady=20, background=BG)

        # Labels
        label_title_ix = tkinter.Label(text="Name:", font=TITLE_FONTS, width=8, bg=BG)
        label_title_ix.grid(row=0, column=1)

        label_title_credit = tkinter.Label(text="Credits:", font=TITLE_FONTS, width=8, bg=BG)
        label_title_credit.grid(row=0, column=2)

        label_title_grade = tkinter.Label(text="Grade:", font=TITLE_FONTS, width=8, bg=BG)
        label_title_grade.grid(row=0, column=3)

        line = DataRow(win=new_win)
