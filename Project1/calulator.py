import tkinter as tk
from tkinter import messagebox

# Function to update the display when buttons are clicked
def button_click(item):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + item)

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)

# Function to perform arithmetic operations
def calculate():
    try:
        expression = display.get()
        result = eval(expression)  # Using eval is okay here for simplicity in this context
        display.delete(0, tk.END)
        display.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        clear_display()

# Function to handle the exit button
def on_exit():
    if messagebox.askokcancel("Exit", "Do you want to quit?"):
        root.destroy()

# Main Tkinter window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display numbers and results
display = tk.Entry(root, width=60, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons with corresponding functions
buttons = [
    ("7", lambda: button_click('7')),
    ("8", lambda: button_click('8')),
    ("9", lambda: button_click('9')),
    ("/", lambda: button_click('/')),
    ("4", lambda: button_click('4')),
    ("5", lambda: button_click('5')),
    ("6", lambda: button_click('6')),
    ("*", lambda: button_click('*')),
    ("1", lambda: button_click('1')),
    ("2", lambda: button_click('2')),
    ("3", lambda: button_click('3')),
    ("-", lambda: button_click('-')),
    ("0", lambda: button_click('0')),
    (".", lambda: button_click('.')),
    ("=", calculate),
    ("+", lambda: button_click('+')),
    ("C", clear_display),
    ("Exit", on_exit)
]

# Place buttons in the grid
row_index = 1
col_index = 0
for (text, command) in buttons:
    tk.Button(root, text=text, padx=50, pady=20, command=command).grid(row=row_index, column=col_index)
    col_index += 1
    if col_index > 3:
        col_index = 0
        row_index += 1

# Start the GUI main loop
root.mainloop()