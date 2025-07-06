import tkinter as tk
from tkinter import messagebox

window = tk.Tk()


def saluta():
    nume = input.get()
    messagebox.showinfo(title="Greeting",message=f"Hello, {nume}!")


label = tk.Label(window, text="Enter name")
label.pack()

input = tk.Entry(window)
input.pack()

button = tk.Button(window, text="Greet", command=saluta)
button.pack()


window.mainloop()
