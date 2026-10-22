
import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            result_label.config(
                text="Password length must be at least 4!",
                fg="red"
            )
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(
            random.SystemRandom().choice(characters)
            for _ in range(length)
        )

        result_entry.config(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
        result_entry.config(state="readonly")

        result_label.config(
            text="Password generated successfully!",
            fg="#90EE90"
        )

    except ValueError:
        result_label.config(
            text="Please enter a valid password length!",
            fg="red"
        )

def copy_password():
    password = result_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        result_label.config(text="Password copied!", fg="#90EE90")

root = tk.Tk()
root.title("Password Generator")
root.geometry("450x400")
root.resizable(False, False)
root.configure(bg="#202020")

title = tk.Label(
    root,
    text="PASSWORD GENERATOR",
    font=("Segoe UI", 19, "bold"),
    bg="#202020",
    fg="white"
)
title.pack(pady=20)

length_label = tk.Label(
    root,
    text="Enter Password Length:",
    font=("Segoe UI", 12),
    bg="#202020",
    fg="white"
)
length_label.pack()

length_entry = tk.Entry(
    root,
    font=("Segoe UI", 13),
    justify="center",
    width=15
)
length_entry.insert(0, "12")
length_entry.pack(pady=10)

generate_button = tk.Button(
    root,
    text="Generate Password",
    font=("Segoe UI", 12, "bold"),
    bg="#16865C",
    fg="white",
    command=generate_password
)
generate_button.pack(pady=10)

result_entry = tk.Entry(
    root,
    font=("Consolas", 12),
    width=35,
    justify="center",
    state="readonly"
)
result_entry.pack(pady=10)

copy_button = tk.Button(
    root,
    text="Copy Password",
    font=("Segoe UI", 11),
    bg="#444444",
    fg="white",
    command=copy_password
)
copy_button.pack(pady=5)

result_label = tk.Label(
    root,
    text="Choose a length and generate your password.",
    font=("Segoe UI", 9),
    bg="#202020",
    fg="white",
    wraplength=400
)
result_label.pack(pady=10)

root.mainloop()
