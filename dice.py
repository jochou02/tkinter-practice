import tkinter as tk
import random

window = tk.Tk()

def gen_int():
    lbl_value["text"] = str(random.randint(1, 6))

window.columnconfigure(0, minsize=150)
window.rowconfigure([0,1], minsize=50)

btn_roll = tk.Button(master=window, text="Roll", command=gen_int)
btn_roll.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text='')
lbl_value.grid(row=1, column=0, sticky="nsew")

window.mainloop()