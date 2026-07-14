import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = length_entry.get()

    if not length.isdigit():
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    length = int(length)

    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than 0.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# Create Window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x250")

# Heading
title = tk.Label(window, text="Password Generator", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Password Length
length_label = tk.Label(window, text="Enter Password Length:")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

# Generate Button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Display Password
password_label = tk.Label(window, text="Generated Password:")
password_label.pack()

password_entry = tk.Entry(window, width=40)
password_entry.pack()

# Run the application
window.mainloop()