import tkinter as tk
from tkinter import messagebox as mb
import mysql.connector as sql

def show_login_frame():
    


def create():
    username=username_entry.get()
    password=password_entry.get()

    if username == "" or password == "" :
        mb.showinfo(title = "Fields are empty",message="crate a username and password for your account" )
    else:
        con = sql.connect(host="localhost", user="root", password="0139612345", database="login_details")
        cursor=con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (username VARCHAR(255), password VARCHAR(255))")

            # Insert data into the table
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))

        
        con.commit()
        mb.showinfo(title="created account status",message="successful")
        con.close()



window = tk.Tk()
window.title("create your account")
window.geometry("1540x800")

label = tk.Label(window, text="create your login details")
label.pack()

frame = tk.Frame()
frame.pack()

username_label= tk.Label(frame, text="username")
username_entry= tk.Entry(frame)
password_label= tk.Label(frame, text="password")
password_entry= tk.Entry(frame)
login_button = tk.Button(frame, text="Create",command=create)

username_label.grid(row=1,column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2,column=0)
password_entry.grid(row=2,column=1)
login_button.grid(row=3,column=0,columnspan=2)



window.mainloop()