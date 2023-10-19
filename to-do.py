#Task 1: To-do List
#This program will help you to list-out tasks by use of various buttons. You can "add", "delete", or "edit" tasks.
#In addition, you can change theme of the interface for better use. "Dark" and "Light" themes are available.

import tkinter as tk
from tkinter import messagebox

# Creating and setting up the display window
window = tk.Tk()
window.title("Task 1: To-do List")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = int(screen_width * 0.17)
window_height = int(screen_height * 0.43)
window.geometry(f"{window_width}x{window_height}")
window.config(bg = "white")

tasks = []  #List that will store entered tasks

def add_tasks():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END,task)
        entry.delete(0,tk.END)
    else:
        messagebox.showwarning("Warning!!!","Please enter a task!!")

def delete_tasks():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
        tasks.pop(selected_task)
    except IndexError:
        messagebox.showwarning("Warning!!!","Please select a task to delete!")

def edit_task():
    try:
        selected_task = listbox.curselection()[0]
        new_task = entry.get()
        if new_task:
            tasks[selected_task] = new_task
            listbox.delete(selected_task)
            listbox.insert(selected_task,new_task)
            entry.delete(0,tk.END)
        else:
            messagebox.showwarning("Warning!!","Please enter a new task!")
    except IndexError:
        messagebox.showwarning("Warning!","Please select a task to edit!!")

#theme changing block
def change_theme():
    current_theme = window.cget("bg")
    #dark theme
    if current_theme == "white":  
        new_theme = "#2D2D32" #darkgrey 
        window.configure(bg=new_theme)
        listbox.configure(bg="#616166", fg="white", selectbackground="#FF6C3F",selectforeground="white") 
        label1.configure(bg="#2D2D32", fg="white") 
        label2.configure(bg="#2D2D32", fg="white") 
        entry.configure(bg="#616166", fg="white") 
        change_theme_button.configure(bg="#7514EF", fg="white") 
    #light theme
    else: 
        new_theme = "white" 
        window.configure(bg=new_theme)
        listbox.configure(bg="#EEDCFF", fg="#241239", selectbackground="#42B8EB",selectforeground="white") 
        label1.configure(bg="white", fg="#241239") 
        label2.configure(bg="white", fg="#241239") 
        entry.configure(bg="#EEDCFF", fg="#241239") 
        change_theme_button.configure(bg="#7514EF", fg="white")

#button to change theme
change_theme_button = tk.Button(window, text=" Change Theme ", command=change_theme,bg="#7514EF", fg="white", font=("Comic Sans MS", 10, "bold","roman"))
change_theme_button.pack(side=tk.TOP, padx=5, pady= 5)

#Listing entered tasks
label1 = tk.Label(window, text=" List of tasks entered: ", font = ("Times", 12, "normal","bold"),bg="white", fg="#241239")
label1.pack(pady=5)
listbox = tk.Listbox(window, selectmode=tk.SINGLE, border=1, justify="center", font = ("Comic Sans MS",10, "normal"),bg="#EEDCFF", fg="#241239", selectbackground="#42B8EB",selectforeground="white")
listbox.pack(pady=0, padx=30, fill=tk.X, expand=True)

#Entering tasks
label2 = tk.Label(window, text=" Type a task to add: " , font = ("Times", 12 , "normal","bold"),bg="white", fg="#241239")
label2.pack(pady=5)
entry = tk.Entry(window, font = ("Comic Sans MS",11), bg="#EEDCFF", fg="#241239")
entry.pack(pady=0, padx=10, fill=tk.X, expand=False)

#creating buttons
add_button = tk.Button(window, text="Add Task", command=add_tasks, bg="#0C951A",fg="white" , font = ("Comic Sans MS", 10, "roman")) 
delete_button = tk.Button(window, text="Delete Task", command=delete_tasks, bg="#BC093F",fg="white", font = ("Comic Sans MS", 10, "roman"))  #maroon bg
edit_button = tk.Button(window, text="Edit Task", command=edit_task, bg="#0F60B6",fg="white" , font = ("Comic Sans MS", 10, "roman"))  #blue
add_button.pack(side=tk.LEFT, padx=5 , pady=5)
delete_button.pack(side=tk.LEFT, padx=5, pady=5)
edit_button.pack(side=tk.LEFT, padx=5, pady=5)

window.mainloop()