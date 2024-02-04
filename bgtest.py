import tkinter as tk
from tkinter import messagebox as mb
import mysql.connector as sql
from PIL import Image, ImageTk

def show_login():
    create_account_frame.pack_forget()
    login_frame.pack()

    # Get the dimensions of the Tkinter window
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    # Load and resize the image
    try:
        img = Image.open("/Users/bhardwaj/Documents/pictures for project/istockphoto-941302930-612x612.jpg")  # Update the image file path
    except IOError:
        mb.showinfo(title="Error", message="Failed to load the background image.")
        return

    resized_image = img.resize((window_width, window_height), Image.LANCZOS)
    image_tk = ImageTk.PhotoImage(resized_image)

    # Create or update the background label
    if hasattr(show_login, 'background_label'):
        show_login.background_label.configure(image=image_tk)
        show_login.background_label.image = image_tk
    else:
        show_login.background_label = tk.Label(login_frame, image=image_tk)
        show_login.background_label.image = image_tk
        show_login.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Update the position and size of entry widgets and buttons
    update_widgets_position_size(window_width, window_height)

def update_widgets_position_size(width, height):
    # Update the position and size of entry widgets and labels in the login frame
    login_username_entry.place(relx=0.5, rely=0.4, anchor="center")
    login_password_entry.place(relx=0.5, rely=0.5, anchor="center")
    login_button.place(relx=0.5, rely=0.6, anchor="center")
    createacc_button.place(relx=0.5, rely=0.7, anchor="center")

def on_resize(event):
    # Update the background image and widget positions and sizes when the window is resized
    show_login()

# Function to create account
def create_account():
    c_username = create_username_entry.get()
    c_password = create_password_entry.get()

    if c_username == "" or c_password == "":
        mb.showinfo(title="Fields are empty", message="Create a username and password for your account")
    else:
        con = sql.connect(host="localhost", user="root", password="0139612345", database="login_details")
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (username VARCHAR(255), password VARCHAR(255))")

        # Insert data into the table
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (c_username, c_password))

        con.commit()
        mb.showinfo(title="Created account status", message="Successful")
        con.close()

# Function for login
def login():
    e_username = login_username_entry.get()
    e_password = login_password_entry.get()

    if e_username == "" or e_password == "":
        mb.showinfo(title="Fields are empty", message="Create a username and password for your account")
    else:
        con = sql.connect(host="localhost", user="root", password="0139612345", database="login_details")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (e_username, e_password))
        data = cursor.fetchone()

        if data:
            mb.showinfo(title="Login successful", message="Welcome, " + e_username)
        else:
            mb.showinfo(title="Login unsuccessful", message="Username or Password are incorrect. If you are a new user, create a new account")

# Main Window
root = tk.Tk()
root.title("Welcome to flipzon")
root.geometry("800x700")

# Login frame
login_frame = tk.Frame(root)
login_label = tk.Label(login_frame, text="Provide your login details")
login_label.place(relx=0.5, rely=0.3, anchor="center")

login_username_label = tk.Label(login_frame, text="Username")
login_username_entry = tk.Entry(login_frame)
login_password_label = tk.Label(login_frame, text="Password")
login_password_entry = tk.Entry(login_frame, show="*")

login_button = tk.Button(login_frame, text="Login", command=login)
createacc_button = tk.Button(login_frame, text="New User? Create Your account", command=create_account)

# Initial widget positions and sizes
update_widgets_position_size(root.winfo_width(), root.winfo_height())

# Bind the on_resize function to the window resize event
root.bind("<Configure>", on_resize)

# Create your account frame
create_account_frame = tk.Frame(root)
create_label = tk.Label(create_account_frame, text="Create your account here")
create_label.pack()

create_username_label = tk.Label(create_account_frame, text="Username")
create_username_entry = tk.Entry(create_account_frame)
create_password_label = tk.Label(create_account_frame, text="Password")
create_password_entry = tk.Entry(create_account_frame, show="*")

create_button = tk.Button(create_account_frame, text="Create", command=create_account)
create_button.pack()

show_login()

root.mainloop()
