import tkinter as tk

root = tk.Tk()
root.title("Login")

username_label = tk.Label(root, text="Username:")
username_label.place(x=20, y=30)

username_entry = tk.Entry(root)
username_entry.place(x=80, y=30)

password_label = tk.Label(root, text="Password:")
password_label.place(x=20, y=60)

password_entry = tk.Entry(root)
password_entry.place(x=80, y=60)

login_button = tk.Button(root, text="Login")
login_button.place(x=80, y=100)

root.mainloop()
