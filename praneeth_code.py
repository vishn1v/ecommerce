from tkinter import *

from PIL import Image, ImageTk
import os
import ast

# Creating a window
app = Tk()
app.title("Login Page")
app.geometry("1024x650")
app.configure(bg="white")

font1 = ("Times", 20, "bold")
font2 = ("Times", 15, "bold")
font3 = ("Times", 10, "bold")
font4 = ("Times", 10, "bold", "underline")

img = ImageTk.PhotoImage(Image.open("intro.jpg"))
Label(app, image=img).place(x=0, y=0)

#button = Button(app, text="")
#button.place(x=500, y=500)

frame = Frame(app, width= 250, height=190, bg="white")  
frame.place(x=435, y=400)

heading = Label(frame,text="Login", font=font1,bg="white")
heading.place(x=90, y=10)

#creating the labels and entry widgets for username and password
# for username
def on_click(event):
    username.delete(0, END)
def on_nonclick(event):
    if username.get() == "":
        username.insert(0, "Username")

username = Entry(frame,width=25,fg="black",bg="#fff",font='Times 12')
username.place(x=30, y=50)
username.insert(0, "Username")
username.bind("<FocusIn>", on_click)
username.bind("<FocusOut>", on_nonclick)

Frame(frame, width=250, height=190, bg="white").place(x=435, y=400)
#for password
def on_click(event):
    password.delete(0, END)
def on_nonclick(event):
    if password.get() == "":
        password.insert(0, "Password")

password = Entry(frame,width=25,fg="black",bg="#fff",font='Times 12')
password.place(x=30, y=90)
password.insert(0, "Password")
password.bind("<FocusIn>", on_click)
password.bind("<FocusOut>", on_nonclick)

Frame(frame, width=250, height=190, bg="white").place(x=495, y=490)



app.mainloop()