import tkinter as tk
from tkinter import messagebox as mb
import mysql.connector as sql

def create():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        mb.showinfo(title="Fields are empty", message="Create a username and password for your account")
    else:
        try:
            con = sql.connect(host="localhost", user="root", password="0139612345", database="login_details")
            cursor = con.cursor()

            # Create the table if not exists
            cursor.execute("CREATE TABLE IF NOT EXISTS login_details (username VARCHAR(255), password VARCHAR(255))")

            # Insert data into the table
            cursor.execute("INSERT INTO login_details (username, password) VALUES (%s, %s)", (username, password))

            con.commit()
            mb.showinfo(title="Account Creation Status", message="Account created successfully")
        except sql.Error as e:
            mb.showerror(title="Connection Error", message=f"Error: {e}")
        finally:
            if con.is_connected():
                con.close()

window = tk.Tk()
window.title("Create Your Account")
window.geometry("400x200")

label = tk.Label(window, text="Create your login details")
label.pack()

frame = tk.Frame(window)
frame.pack()

username_label = tk.Label(frame, text="Username")
username_entry = tk.Entry(frame)
password_label = tk.Label(frame, text="Password")
password_entry = tk.Entry(frame, show="*")  # Use show="*" to hide password
create_button = tk.Button(frame, text="Create", command=create)

username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
create_button.grid(row=3, column=0, columnspan=2)

window.mainloop()
