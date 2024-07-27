import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Label for password length input
        ttk.Label(self.root, text="Enter the length of the password:").grid(row=0, column=0, padx=10, pady=10)

        # Entry widget for length
        self.length_entry = ttk.Entry(self.root, width=20)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        # Button to generate password
        self.generate_button = ttk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Label to display the password
        self.result_label = ttk.Label(self.root, text="", wraplength=300)
        self.result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        # Get the length from the entry widget
        length = self.length_entry.get()

        try:
            length = int(length)
            if length <= 0:
                raise ValueError("Length must be positive")

            # Generate random password
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))

            # Display the password
            self.result_label.config(text=f"Generated Password: {password}")

        except ValueError:
            self.result_label.config(text="Please enter a valid positive integer.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
