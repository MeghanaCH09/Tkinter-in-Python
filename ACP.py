import tkinter as tk
import random

def generate_password(length):
    """Generate a random password of specified length."""
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    punctuation = '!@#$%^&*()-_=+}{[];:,.<>?'

    characters = lowercase + uppercase + digits + punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def on_generate():
    """Handle the button click to generate a new password."""
    try:
        length = int(length_entry.get()) 
        if length < 1:
            raise ValueError("Length must be at least 1")
        password = generate_password(length) 
        password_entry.delete(0, tk.END) 
        password_entry.insert(0, password)
    except ValueError:
        password_entry.delete(0, tk.END) 
        password_entry.insert(0, "Invalid input") 

root = tk.Tk()
root.title("Random Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.pack(pady=20)

password_label = tk.Label(root, text="Generated Password:")
password_label.pack(pady=10)

password_entry = tk.Entry(root)
password_entry.pack(pady=5)

root.mainloop()
