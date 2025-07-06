import tkinter as tk


win = tk.Tk()

win.title("Prima mea aplicatie")

width = 300
height = 300
x = 0
y = 0
win.geometry(f"{width}x{height}+{x}+{y}")
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

### DREAPTA JOS
win.geometry(f"{width}x{height}+{screen_width-width}+{screen_height-height}")

### STANGA JOS
win.geometry(f"{width}x{height}+{0}+{screen_height-height}")

### MIJLOC
win.geometry(f"{width}x{height}+{(screen_width-width)//2}+{(screen_height-height)//2}")

win.mainloop()



