import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error!!!")

root = tk.Tk()
root.title("Calculator")
root.configure(bg="gray")

entry = tk.Entry(root, width=20, borderwidth=8, font=10)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_num, col_num = 1, 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, bg="lightgreen", command=calculate).grid(row=row_num, column=col_num)
    elif button == 'C':
        tk.Button(root, text=button, padx=20, pady=20, bg="red", command=lambda: entry.delete(0, tk.END)).grid(row=row_num, column=col_num)
    elif button in ['+', '-', '*', '/']:
        tk.Button(root, text=button, padx=20, pady=20, bg="skyblue", command=lambda b=button: button_click(b)).grid(row=row_num, column=col_num)
    else:
        tk.Button(root, text=button, padx=20, pady=20, command=lambda b=button: button_click(b)).grid(row=row_num, column=col_num)

    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

root.mainloop()