import tkinter as tk

def button_click(number):
    current = entry_box.get()

root = tk.Tk()
root.title("Calculator")

entry_box = tk.Entry(root, width=40, state="disabled")
entry_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20,
                       command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
