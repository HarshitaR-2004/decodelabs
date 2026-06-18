import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_scale.get()

    chars = string.ascii_letters

    if include_numbers.get():
        chars += string.digits

    if include_symbols.get():
        chars += "!@#$%^&*()_+-=[]{}"

    password = ''.join(random.choice(chars) for _ in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("450x500")
root.resizable(False, False)

# Title
title = tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 22, "bold")
)
title.pack(pady=20)

# Password Length
length_label = tk.Label(
    root,
    text="Password Length:",
    font=("Arial", 14)
)
length_label.pack()

length_scale = tk.Scale(
    root,
    from_=4,
    to=30,
    orient=tk.HORIZONTAL,
    length=300
)
length_scale.set(12)
length_scale.pack(pady=10)

# Checkboxes
include_symbols = tk.BooleanVar(value=True)
include_numbers = tk.BooleanVar(value=True)

symbol_check = tk.Checkbutton(
    root,
    text="Include Symbols",
    variable=include_symbols,
    font=("Arial", 12)
)
symbol_check.pack(pady=5)

number_check = tk.Checkbutton(
    root,
    text="Include Numbers",
    variable=include_numbers,
    font=("Arial", 12)
)
number_check.pack(pady=5)

# Generate Button
generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 14, "bold"),
    width=20,
    height=2
)
generate_btn.pack(pady=30)

# Result Label
result_label = tk.Label(
    root,
    text="Generated Password:",
    font=("Arial", 14)
)
result_label.pack()

# Password Box
password_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 14),
    justify="center"
)
password_entry.pack(pady=10)

# Copy Button
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied!")

copy_btn = tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    bg="#2196F3",
    fg="white",
    font=("Arial", 12)
)
copy_btn.pack(pady=10)

root.mainloop()
