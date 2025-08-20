import tkinter as tk
from tkinter import messagebox
import os
# Dummy database (dictionary for demo)
users = {}

# Register function
def register():
    username = reg_user.get()
    password = reg_pass.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required")
    elif username in users:
        messagebox.showerror("Error", "User already exists")
    else:
        users[username] = password
        messagebox.showinfo("Success", "Registration successful! You can login now.")
        reg_user.set("")
        reg_pass.set("")

# Login function
def login():
    username = login_user.get()
    password = login_pass.get()

    if username in users and users[username] == password:
        messagebox.showinfo("Success", f"Welcome {username}!")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

root = tk.Tk()
root.title("Login & Register Page")
root.geometry("400x300")
root.config(bg="white")

# ================= Register Frame =================
reg_frame = tk.LabelFrame(root, text="Register", font=("Arial", 12, "bold"), bg="white")
reg_frame.place(x=20, y=20, width=170, height=200)

reg_user = tk.StringVar()
reg_pass = tk.StringVar()

tk.Label(reg_frame, text="Username:", bg="white").pack(pady=5)
tk.Entry(reg_frame, textvariable=reg_user).pack(pady=5)
tk.Label(reg_frame, text="Password:", bg="white").pack(pady=5)
tk.Entry(reg_frame, textvariable=reg_pass, show="*").pack(pady=5)
tk.Button(reg_frame, text="Register", command=register, bg="lightgreen").pack(pady=10)

# ================= Login Frame =================
login_frame = tk.LabelFrame(root, text="Login", font=("Arial", 12, "bold"), bg="white")
login_frame.place(x=210, y=20, width=170, height=200)

login_user = tk.StringVar()
login_pass = tk.StringVar()

tk.Label(login_frame, text="Username:", bg="white").pack(pady=5)
tk.Entry(login_frame, textvariable=login_user).pack(pady=5)
tk.Label(login_frame, text="Password:", bg="white").pack(pady=5)
tk.Entry(login_frame, textvariable=login_pass, show="*").pack(pady=5)
tk.Button(login_frame, text="Login", command=login, bg="lightblue").pack(pady=10)

root.mainloop()
