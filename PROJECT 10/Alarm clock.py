import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("DIGITAL CLOCK")

def time():
    string = strftime("%H : %M : %S \n %d-%m-%Y")  # Hours, Minutes, Seconds + Date
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(root, font=("calibri", 50, 'bold'), background="yellow", foreground="black")
label.pack(anchor='center')

time()
root.mainloop()
