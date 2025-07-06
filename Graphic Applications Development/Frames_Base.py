import tkinter as tk


window = tk.Tk()
square = 400
window.geometry(f"{square}x{square}+{window.winfo_screenwidth()//2}+{window.winfo_screenheight()//2}")

colors = [ "red",   "blue",  "yellow",  ]

color_frames = []

for bg_color in colors:
    frame = tk.Frame(window, bg=bg_color)
    frame.tkraise
    frame.grid(column=0, row=0, sticky="nesw")
    color_frames.append(frame)

window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)


button_frame = tk.Frame(window)
button_frame.grid(row=1, column=0)

def switch_next_frame():
    global color_frames
    next_frame = color_frames.pop(0)
    next_frame.tkraise()
    color_frames.append(next_frame)

def switch_prev_frame():
    global color_frames
    next_frame = color_frames.pop()
    next_frame.lower()
    color_frames.insert(0, next_frame)

next_button = tk.Button(button_frame, text="Next Frame", command=switch_next_frame)
next_button.grid(row=0, column=1)

prev_button = tk.Button(button_frame, text = "Prev Frame", command=switch_prev_frame)
prev_button.grid(row=0, column=0)


window.mainloop()