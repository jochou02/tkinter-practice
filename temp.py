import tkinter as tk

# Initialize Window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# Swap Method
def swap():
    if lbl_temp["text"] == "\N{DEGREE FAHRENHEIT}":
        lbl_temp["text"] = "\N{DEGREE CELSIUS}"
        lbl_result["text"] = "\N{DEGREE FAHRENHEIT}"
    else:
        lbl_temp["text"] = "\N{DEGREE FAHRENHEIT}"
        lbl_result["text"] = "\N{DEGREE CELSIUS}"

# Conversion Method
def convert():
    if lbl_temp["text"] == "\N{DEGREE FAHRENHEIT}":
        fahrenheit = ent_temp.get()
        celsius = (5 / 9) * (float(fahrenheit) - 32)
        lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    else:
        celsius = ent_temp.get()
        fahrenheit = float(celsius) * (9 / 5) + 32
        lbl_result["text"] = f"{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}"

# Initialize Frames for two rows
frm_row_one = tk.Frame(master=window)
frm_row_two = tk.Frame(master=window)

# Initialize Entry Frame with Fahrenheit
frm_entry = tk.Frame(master=frm_row_one)
ent_temp = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
ent_temp.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Conversion Arrow Button
btn_convert = tk.Button(master=frm_row_one, text="\N{RIGHTWARDS BLACK ARROW}", command=convert)

# Initialize result label to Celcius
lbl_result = tk.Label(master=frm_row_one, text="\N{DEGREE CELSIUS}")

# Swap Button
btn_swap = tk.Button(master=frm_row_two, text="SWAP CONVERSION", command=swap)

# Set up layout
frm_entry.grid(row=0, column=0, padx=10, pady=10)
btn_convert.grid(row=0, column=1)
lbl_result.grid(row=0, column=2, padx=10)
btn_swap.grid(row=0, column=0, sticky="ew", pady=10)
frm_row_one.grid(row=0, column=0)
frm_row_two.grid(row=1, column=0)

# Run the application
window.mainloop()