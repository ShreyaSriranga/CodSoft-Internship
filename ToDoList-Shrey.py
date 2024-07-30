import tkinter as tk 
from tkinter import ttk, messagebox

def newtask():
    task = myentry.get()
    if task != "":
        lb.insert(tk.END, task)
        myentry.delete(0, "end")
    else:
        messagebox.showwarning("Error!!", "Enter a Task!")

def delete():
    lb.delete(tk.ANCHOR)

ws = tk.Tk()
ws.geometry("500x450+500+200")
ws.title("ToDo List")
ws.config(bg="#ffb6c1")
ws.resizable(width=False, height=False)

frame = tk.Frame(ws)
frame.pack(pady=10)

lb = tk.Listbox(
    frame, 
    width=25, 
    height=8, 
    font=('Times', 18), 
    bd=0, 
    fg='#d87093', 
    highlightthickness=0, 
    selectbackground='#ff69b4', 
    activestyle="none"
)
lb.pack(side=tk.LEFT, fill=tk.BOTH)

task = ['Study', 'Sleep', 'Run', 'Music', 'Dance Practice']
for item in task:
    lb.insert(tk.END, item)

scb = tk.Scrollbar(frame)
scb.pack(side=tk.RIGHT, fill=tk.BOTH)

lb.config(yscrollcommand=scb.set)
scb.config(command=lb.yview)

myentry = tk.Entry(ws, font=('Times', 24))
myentry.pack(pady=20)

button_frame = tk.Frame(ws)
button_frame.pack(pady=20)

addtaskbtn = tk.Button(
    button_frame, 
    text='Add Task', 
    font=('Times', 14), 
    bg='#ff69b4', 
    padx=29, 
    pady=10, 
    command=newtask
)
addtaskbtn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

deltaskbtn = tk.Button(
    button_frame, 
    text='Delete Task', 
    font=('Times', 14), 
    bg='#db7093', 
    padx=29, 
    pady=10, 
    command=delete
)
deltaskbtn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

ws.mainloop()
