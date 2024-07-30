import random
import tkinter as tk
from tkinter import simpledialog

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def copy_to_clipboard(password):
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update() 

def show_password(password):
    password_window = tk.Toplevel(root)
    password_window.title("Generated Password")
    password_window.configure(bg="#2E236C")

    tk.Label(password_window, text="Your Generated Password:", bg="#2E236C", fg="#C8ACD6").pack(pady=10)
    password_label = tk.Label(password_window, text=password, font=("Helvetica", 16, "bold"), bg="#2E236C", fg="#C8ACD6")
    password_label.pack(pady=10)

    copy_button = tk.Button(password_window, text="Copy to Clipboard", command=lambda: copy_to_clipboard(password))
    copy_button.pack(pady=10)

    close_button = tk.Button(password_window, text="Close", command=password_window.destroy)
    close_button.pack(pady=10)

def main():
    global root
    root = tk.Tk()
    root.withdraw() 

    length = simpledialog.askinteger("Input", "Enter the desired length of the password:", minvalue=1, maxvalue=100)
    
    if length:
        password = generate_password(length)
        show_password(password)

if __name__ == "__main__":
    main()
    tk.mainloop()
    
    
    