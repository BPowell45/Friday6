import tkinter as tk


root = tk.Tk()
root.title("Sign Up")

name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
password_entry = tk.Entry(root)
password_entry.grid(row=2, column=1, padx=10, pady=5)

sign_up_button = tk.Button(root, text="Sign Up Now")
sign_up_button.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()
