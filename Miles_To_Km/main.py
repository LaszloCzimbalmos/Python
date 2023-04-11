from tkinter import *
mile = 0


def mile_to_km():
    km = float(mile.get()) * 1.609
    output.config(text=f" {km}  Km")


window = Tk()
window.config(width=250, height=200, padx=20, pady=20)
window.title("Convert Miles to Kilometers")


label1 = Label(text="Convert: ")
label1.place(x=0, y=10)

label2 = Label(text="Miles")
label2.place(x=175, y=10)

label3 = Label(text="is equal to: ")
label3.place(x=50, y=40)

output = Label(text=f" {0}  Km")
output.place(x=140, y=40)

mile = Entry(width=20)
mile.place(x=50, y=10)

cv_button = Button(text="Convert", command=mile_to_km)
cv_button.place(x=50, y=70)


window.mainloop()