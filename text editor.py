import tkinter as tk

# Initialize Window
window = tk.Tk()
window.title("Simple Text Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Initialize Widgets
txt_edit = tk.Text(master=window)
frm_buttons = tk.Frame(master=window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(master=frm_buttons, text="Open")
btn_save = tk.Button(master=frm_buttons, text="Save As...")

# Button layout
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
# Frame layout
frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

# Run the application
window.mainloop()