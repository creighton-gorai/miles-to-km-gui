from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
# window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
equals_label = Label(text="is equal to", font=("Arial", 12, "bold"))
conversion_label = Label(text=0, font=("Arial", 12, "bold"))
km_label = Label(text="Km", font=("Arial", 12, "bold"))

miles_label.grid(column=2, row=0)
equals_label.grid(column=0, row=1)
conversion_label.grid(column=1, row=1)
km_label.grid(column=2, row=1)


user_input = Entry(width=5)
user_input.grid(column=1, row=0)


def calculate():
    result = int(user_input.get()) * 1.609344
    conversion_label.config(text=str(int(result)))


calc_button = Button(text="Click Me", command=calculate)
calc_button.grid(column=1, row=2)














window.mainloop()
