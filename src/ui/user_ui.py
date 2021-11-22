from ast import copy_location
import tkinter as tk



def user_screen():
    root = tk.Tk()
    
    label = tk.Label(text="Login Screen")
    label.grid(row=0, column=1)

    email_label = tk.Label(text="Email")
    email_label.grid(row=1, column=0)

    email_entry = tk.Entry()
    email_entry.grid(row=1, column=1)

    password_label = tk.Label(text="Password")
    password_label.grid(row=2, column=0)

    password_entry = tk.Entry()
    password_entry.grid(row=2, column=1)

    button_label = tk.Button(text="Login")
    button_label.grid(row=3, column=1)



    a = email_entry.cget
    print(a)
    root.mainloop()
