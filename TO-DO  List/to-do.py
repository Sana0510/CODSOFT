import tkinter as tk
from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("TO-DO GUI-APP")

appicon=PhotoImage(file="C:/Users/DELL/Downloads/download.png")
root.iconphoto(False,appicon)

img= PhotoImage(file='C:/Users/DELL/Downloads/gradient 2.png', master= root)
img_label= Label(root,image=img)
img_label.place(x=0, y=0)

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)

def update_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        updated_task = task_entry.get()
        if updated_task:
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, updated_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task.")

def mark_as_doing():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.itemconfig(selected_task_index, {'bg': 'light blue'})

def mark_as_completed():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.itemconfig(selected_task_index, {'bg':'light green'})


# Create and configure widgets
task_entry = tk.Entry(root, width=30)
add_button = tk.Button(root, text="Add Task", command=add_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
update_button = tk.Button(root, text="Update Task", command=update_task)
doing_button = tk.Button(root, text="Mark as Doing", command=mark_as_doing)
completed_button = tk.Button(root, text="Mark as Completed", command=mark_as_completed)
task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)

# Place widgets on the screen
task_entry.grid(row=0, column=0, padx=10, pady=10)
add_button.grid(row=0, column=1, padx=10, pady=10)
delete_button.grid(row=1, column=0, padx=10, pady=10)
update_button.grid(row=1, column=1, padx=10, pady=10)
doing_button.grid(row=2, column=0, padx=10, pady=10)
completed_button.grid(row=2, column=1, padx=10, pady=10)
task_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
