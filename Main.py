import tkinter as tk
from tkinter import messagebox as mb
import mysql.connector as sql
from mysql.connector import Error
from PIL import Image, ImageTk
from tkmacosx import Button
#from tkinter import ttk
import os
import re

flipzondb = sql.connect(
    host="localhost",
    user="root",
    password="0139612345",
    database="login_details"
)

create_userdetails_table = """
CREATE TABLE IF NOT EXISTS user_details (  
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
)
"""

#executing the query
cursor = flipzondb.cursor()
cursor.execute(create_userdetails_table)


class flipzon:

    def __init__(self,root):
        self.root = root
        self.root.title("Welcome to flipzon")
        self.root.geometry("1040x900")
        self.root.configure(bg="white")
        self.root.attributes('-alpha', 1)
        #self.image_tk = None

        img = Image.open("/Users/bhardwaj/Documents/pictures for project/_defd105c-4bb3-46e3-826a-562cc387d98e.jpeg")
        resized_image = img.resize((1035, 850), Image.LANCZOS)
        image_tk = ImageTk.PhotoImage(resized_image)

        self.background_label = tk.Label(root, image=image_tk)
        self.background_label.image = image_tk  # Keep a reference
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #self.login_frame.place(x=327,y=370,width=390)

    def show_login(self):
        #self.destroy_background_image()
        self.create_account_frame.pack_forget()
        self.forgot_password_frame.pack_forget()
        self.login_frame.place(x=327,y=370,width=390)
        self.update_background_image("/Users/bhardwaj/Documents/pictures for project/_defd105c-4bb3-46e3-826a-562cc387d98e.jpeg")
        #self.login_frame.pack() 

    def show_create_account_screen(self):
        #self.destroy_background_image()
        self.login_frame.place_forget()
        self.forgot_password_frame.pack_forget()
        self.create_account_frame.pack()
        self.update_background_image("/Users/bhardwaj/Documents/pictures for project/force-majeure-du8AbwM5z2g-unsplash.jpg")

    def show_forgot_password_screen(self):
        #self.destroy_background_image()
        self.login_frame.place_forget()
        self.create_account_frame.pack_forget()
        self.forgot_password_frame.pack()
        self.update_background_image("/Users/bhardwaj/Documents/pictures for project/eileen-pan-5d5DSRQ5dUc-unsplash.jpg")

#Function to create account
    def create_account(self):
        c_username=self.create_username_entry.get()
        c_password=self.create_password_entry.get()

        if c_username == "" or c_password == "" :
            mb.showinfo(title = "Fields are empty",message="create a username and password for your account" )
        else:
            #con = sql.connect(host="localhost", user="root", password="0139612345", database="login_details")
            cursor=flipzondb.cursor()
            #cursor.execute("CREATE TABLE IF NOT EXISTS users (username VARCHAR(255), password VARCHAR(255))")

            # Insert data into the table
            cursor.execute("INSERT INTO user_details (username, password) VALUES (%s, %s)", (c_username, c_password))

        
            flipzondb.commit()
            mb.showinfo(title="created account status",message="successful")
            flipzondb.close()

#Function for login
    def login(self):
        #self.destroy_background_image()
        e_username=self.login_username_entry.get()
        e_password=self.login_password_entry.get()

        if e_username == "" or e_password == "":
            mb.showinfo(title = "Fields are empty",message="create a username and password for your account" )
        else:
            #con = sql.connect(host="localhost", user="root", password="0139612345", database="login_details")
            cursor=flipzondb.cursor()
            cursor.execute("SELECT * FROM user_details WHERE username = %s AND password = %s", (e_username, e_password))
            data = cursor.fetchone()

            if data:
                mb.showinfo(title="Login successful", message="Welcome, " + e_username)
            else:
                mb.showinfo(title = "Login Usuccessful",message="Username or Password are incorrect. If you are new user create a new account" )
    
    #function to update password
    def forgot_password(self):
        f_username= self.flogin_username_entry.get()
        cursor=flipzondb.cursor()
        #try:
        cursor.execute("SELECT * from user_details WHERE username=%s", (f_username,))
        data = cursor.fetchone()
        #except Error as e:
           # mb.showerror("Error", e)
        if data:
            f_password = self.flogin_password_entry.get()
            confirm_new_password = self.flogin_confirm_password_entry.get()
            if f_username and f_password and confirm_new_password:
                if f_password == confirm_new_password:
                    #try:
                    cursor = flipzondb.cursor()
                    cursor.execute("UPDATE user_details SET password=%s WHERE username=%s", (f_password, f_username))
                    flipzondb.commit()
                    mb.showinfo("Success", "Password updated successfully")
                    #self.login_page()
                #except Error as e:
                    #mb.showerror("Error", e)
                else:
                    mb.showerror("Error", "Password and Confirm Password do not match")
            else:
                mb.showerror("Error", "All fields are required")
        else:
            mb.showerror("Error", "Invalid Email")
                    
                     
    #                 con = sql.connect(host="localhost", user="root", password="0139612345", database="login_details")
    #                 #cursor=con.cursor()
    #                 cursor.execute('''
    #                     UPDATE users
    #                     SET password = %s
    #                     WHERE username = %s
    #                 ''', (f_password, f_username))
    #                 con.commit()
    #                 con.close()
    #                 mb.showinfo(title="Password updated",message="Password updated successfully")
    #                 cursor = pdsdb.cursor()
    #                 cursor.execute("UPDATE user_info SET password=%s WHERE email=%s", (new_password, email))
    #                 pdsdb.commit()
    #                 messagebox.showinfo("Success", "Password updated successfully")
    #                 self.login_page()
    #             except Error as e:
    #                 messagebox.showerror("Error", e)
    #         else:
    #             messagebox.showerror("Error", "Password and Confirm Password do not match")
    #     else:
    #         messagebox.showerror("Error", "All fields are required")
    # else:
    #     messagebox.showerror("Error", "Invalid Email")

    #     if f_username == "" or f_password == "":
    #         mb.showinfo(title = "Fields are empty",message="provide a username and password for your account" )
    #     else:
    #         con = sql.connect(host="localhost", user="root", password="0139612345", database="login_details")
    #         cursor=con.cursor()
    #         cursor.execute('''
    #             UPDATE users
    #             SET password = %s
    #             WHERE username = %s
    #         ''', (f_password, f_username))
    #         con.commit()
    #         con.close()
    #         mb.showinfo(title="Password updated",message="Password updated successfully")
        # con = sql.connect(host="localhost", user="root", password="0139612345", database="login_details")
        # cursor=con.cursor()
        # cursor.execute('''
        #     UPDATE users
        #     SET password = %s
        #     WHERE username = %s
        # ''', (f_password, f_username))
        # con.commit()
        # con.close()
        #return True  # Update successful
        


    def update_background_image(self,image_path):
        img = Image.open(image_path)
        resized_image = img.resize((1035, 850), Image.LANCZOS)
        image_tk = ImageTk.PhotoImage(resized_image)
        self.background_label.configure(image=image_tk)
        self.background_label.image = image_tk

    def destroy_background_image(self):
        if hasattr(self, 'background_label') and self.background_label.winfo_exists():
             self.background_label.destroy()


   # if username == "" or password == "" :
     #  mb.showinfo(title = "Fields are empty",message="create a username and password for your account" )
    #else:
      #   mb.showinfo(title = "create an account",message="create a username and password for your account" )

#Main Window
# '''root = tk.Tk()
# root.title("Welcome to flipzon")
# root.geometry("1540x800")
# root.configure(bg="white")
# root.attributes('-alpha', 1)

# img = Image.open("/Users/bhardwaj/Documents/pictures for project/_defd105c-4bb3-46e3-826a-562cc387d98e.jpeg")
# resized_image = img.resize((1530, 800), Image.LANCZOS)
# image_tk = ImageTk.PhotoImage(resized_image)
# background_label = tk.Label(root, image=image_tk)
# background_label.image = image_tk  # Keep a reference
# background_label.place(x=0, y=0, relwidth=1, relheight=1)'''

# '''img = ImageTk.PhotoImage(Image.open("/Users/bhardwaj/Documents/pictures for project/force-majeure-du8AbwM5z2g-unsplash.jpg"))
# tk.Label(root, image=img).place(relheight=1, relwidth=1)'''




#Login frame
    def l_frame(self):
        self.login_frame=tk.Frame(root, bg="grey")
        #login_frame.place(x=0,y=0,relheight=1, relwidth=1)
        #login_frame.attributes('-alpha', 0.9)
        self.login_label = tk.Label(self.login_frame, text="provide your login details",bg="grey",font=("Calibri","20","bold"))
        self.login_label.grid(row=0,column=0,columnspan=5,pady=10)
        self.login_username_label= tk.Label(self.login_frame, text="username",bg="grey",fg="azure",font=("Calibri","15","bold"),pady=5)
        self.login_username_entry= tk.Entry(self.login_frame)
        self.login_password_label= tk.Label(self.login_frame, text="password",bg="grey",font=("Calibri","15","bold"))
        self.login_password_entry= tk.Entry(self.login_frame)
        self.login_button = Button(self.login_frame, text="Login",bg="#FFFF00",fg="black",command=self.login,highlightbackground="grey",borderless=1)
        self.forgot_password_button = Button(self.login_frame, text="Forgot password?",bg="gold",fg="black",command=self.show_forgot_password_screen,highlightbackground="grey",borderless=1)
        self.createacc_button=tk.Button(self.login_frame, text="New User? Create Your account",bg="yellow",fg="black",command=self.show_create_account_screen,highlightbackground="grey")

        self.login_username_label.grid(row=1,column=0)
        self.login_username_entry.grid(row=1, column=1)
        self.login_password_label.grid(row=2,column=0)
        self.login_password_entry.grid(row=2,column=1)
        self.login_button.grid(row=3,column=0,columnspan=2,pady="10")
        self.forgot_password_button.grid(row=4,column=0,columnspan=3)
        self.createacc_button.grid(row=6,column=0,columnspan=3)

    #Create your account frame
    def c_frame(self):
        self.create_account_frame=tk.Frame(root,bg="grey")
        self.create_label = tk.Label(self.create_account_frame, text="create your account here",bg="grey",font=("Calibri","20","bold"))
        self.create_label.grid(row=0,column=0,columnspan=5,pady=10)
        self.create_username_label= tk.Label(self.create_account_frame, text="username",bg="grey",fg="azure",font=("Calibri","15","bold"),pady="5")
        self.create_username_entry= tk.Entry(self.create_account_frame)
        self.create_password_label= tk.Label(self.create_account_frame, text="password",bg="grey",font=("Calibri","15","bold"),pady="5")
        self.create_password_entry= tk.Entry(self.create_account_frame)
        self.create_button = tk.Button(self.create_account_frame, text="Create",bg="yellow",command=self.create_account,highlightbackground="grey")
        self.create_back_login_button = tk.Button(self.create_account_frame, text="Back to login",bg="gold",command=self.show_login,highlightbackground="grey")

        self.create_username_label.grid(row=1,column=0)
        self.create_username_entry.grid(row=1, column=1)
        self.create_password_label.grid(row=2,column=0)
        self.create_password_entry.grid(row=2,column=1)
        self.create_button.grid(row=3,column=0,columnspan=2,pady="10")
        self.create_back_login_button.grid(row=4,column=0,columnspan=3)
    
    #Forgot password frame
    def f_frame(self):
        self.forgot_password_frame=tk.Frame(root,bg="grey")
        self.forgot_label = tk.Label(self.forgot_password_frame, text="Forgot password",bg="grey",font=("Calibri","20","bold"))
        self.forgot_label.grid(row=0,column=0,columnspan=5,pady=10)
        self.flogin_username_label= tk.Label(self.forgot_password_frame, text="username",bg="grey",fg="azure",font=("Calibri","15","bold"),pady="5")
        self.flogin_username_entry= tk.Entry(self.forgot_password_frame)
        self.flogin_password_label= tk.Label(self.forgot_password_frame, text="new password",bg="grey",font=("Calibri","15","bold"),pady="5")
        self.flogin_password_entry= tk.Entry(self.forgot_password_frame)
        self.flogin_confirm_password_label= tk.Label(self.forgot_password_frame, text="confirm password",bg="grey",font=("Calibri","15","bold"),pady="5")
        self.flogin_confirm_password_entry= tk.Entry(self.forgot_password_frame)
        self.flogin_button = tk.Button(self.forgot_password_frame, text="Update",bg="yellow",command=self.forgot_password,highlightbackground="grey")
        self.flogin_back_login_button = tk.Button(self.forgot_password_frame, text="Back to login",bg="gold",command=self.show_login,highlightbackground="grey")

        self.flogin_username_label.grid(row=1,column=0)
        self.flogin_username_entry.grid(row=1, column=1)
        self.flogin_password_label.grid(row=2,column=0)
        self.flogin_password_entry.grid(row=2,column=1)
        self.flogin_confirm_password_label.grid(row=3,column=0)
        self.flogin_confirm_password_entry.grid(row=3,column=1)
        self.flogin_button.grid(row=5,column=0,columnspan=2,pady="10")
        self.flogin_back_login_button.grid(row=6,column=0,columnspan=3)

if __name__ == "__main__":
    root = tk.Tk()
    app = flipzon(root)
    
    app.l_frame()
    app.c_frame()
    app.f_frame()
    app.show_login()
    root.mainloop()

