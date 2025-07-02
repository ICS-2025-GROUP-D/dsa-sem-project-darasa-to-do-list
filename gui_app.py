import tkinter as tk
from tkinter import messagebox,simpledialog
from data_structures import task_db, stack_undo, arrays_util
from PIL import Image,ImageTk

undo = stack_undo.UndoStack() 
task_id_map= []

# Color Theme
BG_COLOR = "#1e1e2f"
BTN_BG = "#2dd4bf"       # Turquoise
BTN_FG = "#ffffff"
ENTRY_BG = "#2c2c3a"
LISTBOX_BG = "#2a2a36"
TEXT_COLOR = "#f1f5f9"
FONT = ("Segoe UI", 11)


def refresh_tasks():
    task_listbox.delete(0, tk.END)
    tasks = arrays_util.sort_tasks(task_db.get_tasks())

    global task_id_map
    task_id_map = []  # Reset the map

    for i, task in enumerate(tasks, start=1):
        task_listbox.insert(tk.END, f"{i}. {task['description']} [{task['status']}]")
        task_id_map.append(task['id'])  # Store the real ID


def add_task():
    desc = entry.get()
    if desc:
        task_db.add_task(desc)
        undo.push({"action":"add","desc": desc})
        refresh_tasks()
        entry.delete(0,tk.END)

def delete_selected():
    try:
        index = task_listbox.curselection()[0]
        task_id = task_id_map[index]
        task_db.delete_task(task_id)
        undo.push({"action":"delete","id": task_id})
        refresh_tasks()
    except:
        messagebox.showerror("Error", "Please select a task to delete.")

def edit_selected():
    try:
        index = task_listbox.curselection()[0]
        task_id = task_id_map[index]
        new_desc = simpledialog.askstring("Edit Task","Enter new description:")
        if new_desc:
            task_db.update_task(task_id,new_desc)
            refresh_tasks()
    except:
        messagebox.showerror("Error", "Please selct a task to edit.")

def toggle_status():
    try:
        index = task_listbox.curselection()[0]
        task_id = task_id_map[index]
        task_db.toggle_status(task_id)
        refresh_tasks()

    except:
        messagebox.showerror("Error", "Please select a task to toggle status.")


def undo_last():
    action = undo.pop()
    if not action:
        messagebox.showinfo("Undo", "No actions to undo.")
        return
    if action ["action"]== "add":
        tasks= task_db.get_tasks()
        for t in tasks:
            if t['description']== action["desc"]:
                task_db.delete_task(t['id'])
                break
            elif action["action"]== "delete":
                task_db.add_task("[Restored]"+ str(action["id"]))
            refresh_tasks()

# 🖼 App Window Setup
app = tk.Tk()
app.title(" Darasa Todo")
app.geometry("600x600")
app.configure(bg=BG_COLOR)

#Load and resize image
img_raw = Image.open("logo_white.png")
img_raw = img_raw.resize((80, 80))  # Change size as needed
logo_img = ImageTk.PhotoImage(img_raw)


# Load and show log
logo_label = tk.Label(app, image=logo_img, bg=BG_COLOR)
logo_label.pack(pady=(15,5))

# Title
title_label = tk.Label(app, text=" Darasa To-Do List", font=("Segoe UI", 14, "bold"), bg=BG_COLOR, fg=TEXT_COLOR)
title_label.pack(pady=10)

# Entry Box
entry = tk.Entry(app, width=38, font=FONT, bg=ENTRY_BG, fg=TEXT_COLOR, insertbackground=TEXT_COLOR, relief=tk.FLAT)
entry.pack(pady=5)


# Buttons
btn_frame = tk.Frame(app, bg=BG_COLOR)
btn_frame.pack(pady=5)

def styled_btn(text, command):
    return tk.Button(
        btn_frame,
        text=text,
        command=command,
        bg=BTN_BG,
        fg=BTN_FG,
        font=FONT,
        padx=10,
        pady=3,
        bd=0,
        relief=tk.FLAT,
        activebackground="#22c1b4",
        activeforeground=BTN_FG
    )

styled_btn("Add", add_task).pack(side=tk.LEFT, padx=4)
styled_btn("Delete", delete_selected).pack(side=tk.LEFT, padx=4)
styled_btn("Edit", edit_selected).pack(side=tk.LEFT, padx=4)
styled_btn("Toggle", toggle_status).pack(side=tk.LEFT, padx=4)
styled_btn("Undo", undo_last).pack(side=tk.LEFT, padx=4)

# Task List
task_listbox = tk.Listbox(
    app,
    width=60,
    height=15,
    font=("Segoe UI", 10),
    bg=LISTBOX_BG,
    fg=TEXT_COLOR,
    selectbackground="#3fdad1",
    highlightthickness=0,
    relief=tk.FLAT
)

task_listbox.pack(pady=10)

refresh_tasks()
app.mainloop()