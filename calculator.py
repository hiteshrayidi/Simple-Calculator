import tkinter as tk
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
def clear():
    entry.delete(0, tk.END)
root = tk.Tk()
root.title("Calculator")
root.geometry("360x530")
root.resizable(False, False)
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]
row = 1
col = 0
for button in buttons:
    if button == "=":
        cmd = calculate
    else:
        cmd = lambda b=button: click(b)
    tk.Button(
        root,
        text=button,
        width=6,
        height=3,
        font=("Arial", 14),
        command=cmd
    ).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1
tk.Button(
    root,
    text="C",
    width=28,
    height=2,
    font=("Arial", 14),
    command=clear
).grid(row=5, column=0, columnspan=4, padx=5, pady=10)
root.mainloop()