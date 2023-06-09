import tkinter
import data_row

BG_COLOR = "#116D6E"
TITLE_FONTS = ("Times New Roman", 12, "bold")


# Window
tk = tkinter.Tk()
tk.title("Calculate your Grade-Point-Average")
tk.config(width=600, height=500, padx=20, pady=20, background=BG_COLOR)

# Labels
label_title_name = tkinter.Label(text="Name:", font=TITLE_FONTS, width=8)
label_title_name.grid(row=0, column=1)
label_title_name.config(bg=BG_COLOR)

label_title_credit = tkinter.Label(text="Credits:", font=TITLE_FONTS, width=8)
label_title_credit.grid(row=0, column=2)
label_title_credit.config(bg=BG_COLOR)

label_title_grade = tkinter.Label(text="Grade:", font=TITLE_FONTS, width=8)
label_title_grade.grid(row=0, column=3)
label_title_grade.config(bg=BG_COLOR)

# Brain
line = data_row.DataRow(win=tk)

tk.mainloop()
