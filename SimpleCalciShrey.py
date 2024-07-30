import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result = add(num1, num2)
        elif operation == "Subtraction":
            result = subtract(num1, num2)
        elif operation == "Multiplication":
            result = multiply(num1, num2)
        elif operation == "Division":
            result = divide(num1, num2)
        else:
            messagebox.showerror("Error", "Invalid operation!")
            return

        label_result.config(text=f"The result is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="#2E236C")

label_num1 = tk.Label(root, text="Enter the first number:", bg="#2E236C", fg="#C8ACD6")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

label_num2 = tk.Label(root, text="Enter the second number:", bg="#2E236C", fg="#C8ACD6")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

label_operation = tk.Label(root, text="Choose an operation:", bg="#2E236C", fg="#C8ACD6")
label_operation.pack(pady=5)
operation_var = tk.StringVar(root)
operation_var.set("Addition")
dropdown_operation = tk.OptionMenu(root, operation_var, "Addition", "Subtraction", "Multiplication", "Division")
dropdown_operation.pack(pady=5)

button_calculate = tk.Button(root, text="Calculate", command=calculate, bg="#433D8B", fg="white")
button_calculate.pack(pady=10)

label_result = tk.Label(root, text="", bg="#2E236C", fg="#C8ACD6")
label_result.pack(pady=5)

root.mainloop()
