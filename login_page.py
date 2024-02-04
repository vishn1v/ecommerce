import tkinter as tk
import mysql.connector

window = tk.Tk()
window.title("Login page")
window.geometry("1540x800")

label = tk.Label(window, text="provide your login details")
label.pack()

frame = tk.Frame()
frame.pack()


username_label= tk.Label(frame, text="username")
username_entry= tk.Entry(frame)
password_label= tk.Label(frame, text="password")
password_entry= tk.Entry(frame)
createacc_button=tk.Button(frame, text="Create Your account")
login_button = tk.Button(frame, text="Login")

username_label.grid(row=1,column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2,column=0)
password_entry.grid(row=2,column=1)
createacc_button.grid(row=4,column=0,columnspan=3)
login_button.grid(row=3,column=0,columnspan=2)



window.mainloop()