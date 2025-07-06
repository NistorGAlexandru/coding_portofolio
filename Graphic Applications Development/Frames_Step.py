import tkinter as tk


window = tk.Tk()
square = 400
window.geometry(f"{square}x{square}+{window.winfo_screenwidth()//2}+{window.winfo_screenheight()//2}")

colors = [ "red",   "blue",  "yellow"]
STEP = len(colors) - 1

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
    global STEP 
    STEP += 1
    if STEP > len(colors) - 1:
        STEP = 0

    color_frames[STEP].tkraise()

def switch_prev_frame():
    global STEP 
    STEP -= 1
    if STEP < 0:
        STEP = len(colors) - 1
    color_frames[STEP].tkraise()

next_button = tk.Button(button_frame, text="Next Frame", command=switch_next_frame)
next_button.grid(row=0, column=1)

prev_button = tk.Button(button_frame, text = "Prev Frame", command=switch_prev_frame)
prev_button.grid(row=0, column=0)


window.mainloop()