import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")
        master.geometry("400x300")
        master.configure(bg="#f0f0f0")

        self.length_label = tk.Label(master, text="Password Length:", bg="#f0f0f0")
        self.length_label.pack(fill=tk.BOTH, padx=10, pady=5)

        self.length_var = tk.IntVar(value=12)
        self.length_entry = tk.Entry(master, textvariable=self.length_var)
        self.length_entry.pack(fill=tk.BOTH, padx=10, pady=5)

        self.complexity_label = tk.Label(master, text="Password Complexity:", bg="#f0f0f0")
        self.complexity_label.pack(fill=tk.BOTH, padx=10, pady=5)

        self.complexity_var = tk.StringVar(value="Medium")
        self.complexity_menu = tk.OptionMenu(master, self.complexity_var, "Low", "Medium", "High")
        self.complexity_menu.pack(fill=tk.BOTH, padx=10, pady=5)

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password, bg="#4CAF50", fg="white")
        self.generate_button.pack(fill=tk.BOTH, padx=10, pady=10)

        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard, bg="#008CBA", fg="white")
        self.copy_button.pack(fill=tk.BOTH, padx=10, pady=5)

        self.password_label = tk.Label(master, text="", font=("Helvetica", 14), wraplength=300, bg="#f0f0f0")
        self.password_label.pack(fill=tk.BOTH, padx=10, pady=5)

    def generate_password(self):
        length = self.length_var.get()
        complexity = self.complexity_var.get()

        if complexity == "Low":
            characters = string.ascii_letters + string.digits
        elif complexity == "Medium":
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_label.config(text=password)

    def copy_to_clipboard(self):
        password = self.password_label.cget("text")
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Password Generator", "Password copied to clipboard!")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
