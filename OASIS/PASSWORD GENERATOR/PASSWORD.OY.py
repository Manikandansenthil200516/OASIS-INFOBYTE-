import random, string
from tkinter import *
import pyperclip

# Initialize Window
root = Tk()
root.geometry("400x400")  # size of the window by default

# title of our window
root.title("Advanced Password Generator")

# Variables for password complexity options
uppercase = BooleanVar()
numbers = BooleanVar()
special_chars = BooleanVar()

# Function to generate password
def generate_password():
    all_characters = ""
    if uppercase.get() == True:
        all_characters += string.ascii_uppercase
    if numbers.get() == True:
        all_characters += string.digits
    if special_chars.get() == True:
        all_characters += string.punctuation

    if all_characters == "":
        all_characters = string.ascii_letters + string.digits

    password_length = int(length_entry.get())
    password = "".join(random.choice(all_characters) for i in range(password_length))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# Function to copy password to clipboard
def copy_password():
    pyperclip.copy(password_entry.get())

# GUI elements
Label(root, text="Password Length:", font="vouge 12 bold").pack(pady=10)
length_entry = Entry(root, width=10, font="vouge 16")
length_entry.pack(pady=5)

Label(root, text="Include:", font="Arial 12 bold").pack(pady=10)
Checkbutton(root, text="Uppercase", variable=uppercase, onvalue=True, offvalue=False).pack(pady=5)
Checkbutton(root, text="Numbers", variable=numbers, onvalue=True, offvalue=False).pack(pady=5)
Checkbutton(root, text="Special Characters", variable=special_chars, onvalue=True, offvalue=False).pack(pady=5)

Button(root, text="Generate Password", font="vouge 12 bold", command=generate_password).pack(pady=20)

Label(root, text="Generated Password:", font="vouge 12 bold").pack(pady=10)
password_entry = Entry(root, width=30, font="vouge 16")
password_entry.pack(pady=5)

Button(root, text="Copy to Clipboard", font="vouge 12 bold", command=copy_password).pack(pady=20)

root.mainloop()