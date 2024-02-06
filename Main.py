import tkinter as tk
from tkinter import messagebox as mb
import mysql.connector as sql
from mysql.connector import Error
from PIL import Image, ImageTk
from tkmacosx import Button
from tkinter import ttk
import os
import re

conn = sql.connect(
    host="localhost",
    user="root",
    password="0139612345",
    database="login_details"
)

create_userdetails_table = """
CREATE TABLE IF NOT EXISTS user_details (  
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL,
    phone VARCHAR(100) NOT NULL,
    address VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
)
"""

#executing the query
cursor = conn.cursor()
cursor.execute(create_userdetails_table)
conn.commit()
conn.close()



class flipzon:

    def __init__(self,root):
        self.root = root
        self.root.title("Welcome to flipzon")
        self.root.geometry("1040x900")
        self.root.configure(bg="white")
        self.root.attributes('-alpha', 1)
        #self.image_tk = None

        img = Image.open("/Users/bhardwaj/Documents/pictures for project/PhotoGrid_Plus_1707021941021.png")
        resized_image = img.resize((1035, 850), Image.LANCZOS)
        image_tk = ImageTk.PhotoImage(resized_image)

        self.background_label = tk.Label(root, image=image_tk)
        self.background_label.image = image_tk  # Keep a reference
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #self.login_frame.place(x=327,y=370,width=390)

        #cursor=conn.cursor()

        self.show_login()

    def show_login(self):
        for i in self.root.winfo_children():
            i.destroy()

        self.background_label = tk.Label(root)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.login_frame=tk.Frame(root, bg="white")
        #login_frame.place(x=0,y=0,relheight=1, relwidth=1)
        #login_frame.attributes('-alpha', 0.9)
        self.login_label = tk.Label(self.login_frame, text="Provide Your Login Details",bg="white",fg="black",font=("Calibri","20"))
        self.login_label.grid(row=0,column=2,columnspan=5,pady=10)
        self.login_username_label= tk.Label(self.login_frame, text="Username",bg="white",fg="black",font=("Calibri","15","bold"),pady=5)
        self.login_username_entry= tk.Entry(self.login_frame)
        self.login_password_label= tk.Label(self.login_frame, text="Password",bg="white",fg="black",font=("Calibri","15","bold"))
        self.login_password_entry= tk.Entry(self.login_frame)
        self.login_button = Button(self.login_frame, text="Login",bg="sky blue",fg="black",command=self.login,highlightbackground="grey",borderless=1)
        self.forgot_password_button = Button(self.login_frame, text="Forgot password?",bg="light green",fg="black",command=self.show_forgot_password_screen,highlightbackground="grey",borderless=1)
        self.createacc_button= Button(self.login_frame, text="New User? Create Your account",bg="light green",fg="black",command=self.show_create_account_screen,highlightbackground="grey",borderless=1)

        self.login_username_label.grid(row=1,column=1)
        self.login_username_entry.grid(row=1, column=2)
        self.login_password_label.grid(row=2,column=1)
        self.login_password_entry.grid(row=2,column=2)
        self.login_button.grid(row=3,column=2,pady="10")
        self.forgot_password_button.grid(row=4,column=2,padx=5)
        self.createacc_button.grid(row=7,column=2,columnspan=3,pady="10")
        #self.l_frame()
        #self.destroy_background_image()
        # self.create_account_frame.pack_forget()
        # self.forgot_password_frame.pack_forget()
        self.login_frame.place(x=327,y=230,width=390)
        self.update_background_image("/Users/bhardwaj/Documents/pictures for project/PhotoGrid_Plus_1707021941021.png")
        #self.login_frame.pack() 

    def show_create_account_screen(self):
        #self.destroy_background_image()
        for i in self.root.winfo_children():
            i.destroy()

        self.background_label = tk.Label(root)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.create_account_frame=tk.Frame(root,bg="black")
        self.create_label = tk.Label(self.create_account_frame, text="Create your account here",font=("Helvetica",20,"bold"),bg="black",fg="white")
        self.create_label.grid(row=0,column=1,padx=5,pady=10,sticky="w")
        self.create_firstname_label= tk.Label(self.create_account_frame, text="First Name",bg="black",fg="azure",font=("Calibri","15","bold"),pady="5")
        self.create_firstname_entry= tk.Entry(self.create_account_frame)
        self.create_lastname_label= tk.Label(self.create_account_frame, text="Last Name",bg="black",font=("Calibri","15","bold"),pady="5")
        self.create_lastname_entry= tk.Entry(self.create_account_frame)
        self.create_phone_label= tk.Label(self.create_account_frame, text="Phone",bg="black",font=("Calibri","15","bold"),pady="5")
        self.create_phone_entry= tk.Entry(self.create_account_frame)
        self.crreate_address_label= tk.Label(self.create_account_frame, text="Address",bg="black",font=("Calibri","15","bold"),pady="5")
        self.create_address_entry= tk.Entry(self.create_account_frame)
        self.create_email_label= tk.Label(self.create_account_frame, text="Email",bg="black",font=("Calibri","15","bold"),pady="5")
        self.create_email_entry= tk.Entry(self.create_account_frame)
        self.create_username_label= tk.Label(self.create_account_frame, text="username",bg="black",fg="azure",font=("Calibri","15","bold"),pady="5")
        self.create_username_entry= tk.Entry(self.create_account_frame)
        self.create_password_label= tk.Label(self.create_account_frame, text="password",bg="black",font=("Calibri","15","bold"),pady="5")
        self.create_password_entry= tk.Entry(self.create_account_frame)
        self.create_button = Button(self.create_account_frame, text="Create",bg="yellow",command=self.create_account,highlightbackground="black",borderless=1)
        self.create_back_login_button = Button(self.create_account_frame, text="Back to login",bg="yellow",command=self.show_login,highlightbackground="black",borderless=1)

        self.create_firstname_label.grid(row=1,column=0)
        self.create_firstname_entry.grid(row=1, column=1)
        self.create_lastname_label.grid(row=2,column=0)
        self.create_lastname_entry.grid(row=2,column=1)
        self.create_phone_label.grid(row=3,column=0)
        self.create_phone_entry.grid(row=3,column=1)
        self.crreate_address_label.grid(row=4,column=0)
        self.create_address_entry.grid(row=4,column=1)
        self.create_email_label.grid(row=5,column=0)
        self.create_email_entry.grid(row=5,column=1)
        self.create_username_label.grid(row=6,column=0)
        self.create_username_entry.grid(row=6, column=1)
        self.create_password_label.grid(row=7,column=0)
        self.create_password_entry.grid(row=7,column=1)
        self.create_button.grid(row=9,column=0,columnspan=2,pady="10")
        self.create_back_login_button.grid(row=10,column=0,columnspan=3)
        self.create_account_frame.place(x=230,y=160,height=550,width=550)
        # self.frame1=Frame(self.app,width=700,height=450,bg="white")
        # self.frame1.place(x=180,y=90)

        self.update_background_image("/Users/bhardwaj/Documents/pictures for project/PhotoGrid_Plus_1707024804464.png")

    def show_forgot_password_screen(self):
        #self.destroy_background_image()
        #self.create_account_frame.pack_forget()

        for i in self.root.winfo_children():
            i.destroy()
        
        self.background_label = tk.Label(root)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.forgot_password_frame=tk.Frame(root,bg="gray1")
        self.forgot_label = tk.Label(self.forgot_password_frame, text="Forgot password",bg="black",font=("Calibri","20","bold"))
        self.forgot_label.grid(row=0,column=0,columnspan=5,pady=10)
        self.flogin_username_label= tk.Label(self.forgot_password_frame, text="username",bg="black",fg="azure",font=("Calibri","15","bold"),pady="5")
        self.flogin_username_entry= tk.Entry(self.forgot_password_frame)
        self.flogin_password_label= tk.Label(self.forgot_password_frame, text="new password",bg="black",font=("Calibri","15","bold"),pady="5")
        self.flogin_password_entry= tk.Entry(self.forgot_password_frame)
        self.flogin_confirm_password_label= tk.Label(self.forgot_password_frame, text="confirm password",bg="black",font=("Calibri","15","bold"),pady="5")
        self.flogin_confirm_password_entry= tk.Entry(self.forgot_password_frame)
        self.flogin_button = Button(self.forgot_password_frame, text="Update",bg="cyan",command=self.forgot_password,highlightbackground="grey",borderless=1)
        self.flogin_back_login_button = Button(self.forgot_password_frame, text="Back to login",bg="cyan",command=self.show_login,highlightbackground="grey",borderless=1)

        self.flogin_username_label.grid(row=1,column=0)
        self.flogin_username_entry.grid(row=1, column=1)
        self.flogin_password_label.grid(row=2,column=0)
        self.flogin_password_entry.grid(row=2,column=1)
        self.flogin_confirm_password_label.grid(row=3,column=0)
        self.flogin_confirm_password_entry.grid(row=3,column=1)
        self.flogin_button.grid(row=5,column=0,columnspan=2,pady="10")
        self.flogin_back_login_button.grid(row=6,column=0,columnspan=3)
        self.forgot_password_frame.place(x=327,y=280,width=390)
        self.update_background_image("/Users/bhardwaj/Downloads/_0f134ab2-ff1b-491d-94e7-a7b0e40ac860.jpeg")

#Function to create account
    def create_account(self):
        c_firstname=self.create_firstname_entry.get()
        c_lastname=self.create_lastname_entry.get()
        c_phone=self.create_phone_entry.get()
        c_address=self.create_address_entry.get()
        c_email=self.create_email_entry.get()
        c_username=self.create_username_entry.get()
        c_password=self.create_password_entry.get()

        if c_username == "" or c_password == "" :
            mb.showinfo(title = "Fields are empty",message="create a username and password for your account" )
        else:
            con = sql.connect(host="localhost", user="root", password="0139612345", database="login_details")
            cursor=con.cursor()
            #cursor.execute("CREATE TABLE IF NOT EXISTS users (username VARCHAR(255), password VARCHAR(255))")

            # Insert data into the table
            cursor.execute("INSERT INTO user_details (firstname, lastname, phone, address, email, username, password) VALUES (%s, %s, %s, %s, %s, %s,%s)", (c_firstname,c_lastname,c_phone,c_address,c_email,c_username, c_password))

        
            con.commit()
            mb.showinfo(title="created account status",message="successful")
            con.close()

#Function for login
    def login(self):
        #self.destroy_background_image()
        e_username=self.login_username_entry.get()
        e_password=self.login_password_entry.get()

        #con = sql.connect(host="localhost", user="root", password="0139612345", database="login_details")
        

        if e_username == "" or e_password == "":
            mb.showinfo(title = "Fields are empty",message="create a username and password for your account" )
        else:
            con = sql.connect(host="localhost", user="root", password="0139612345", database="login_details")
            cursor=con.cursor()
            cursor.execute("SELECT * FROM user_details WHERE username = %s AND password = %s", (e_username, e_password))
            data = cursor.fetchone()

            if data:
                mb.showinfo(title="Login successful", message="Welcome, " + e_username)
                self.catalog()
            else:
                mb.showinfo(title = "Login Usuccessful",message="Username or Password are incorrect. If you are new user create a new account" )
    
    #function to update password
    def forgot_password(self):
        con = sql.connect(host="localhost", user="root", password="0139612345", database="login_details")
        cursor=con.cursor()
        f_username= self.flogin_username_entry.get()
        
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
                    #cursor = con.cursor()
                    cursor.execute("UPDATE user_details SET password=%s WHERE username=%s", (f_password, f_username))
                    con.commit()
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

    #function to create a caatalog of products using notebook
    def catalog(self):
        for i in self.root.winfo_children():
            i.destroy()

        self.notebook = ttk.Notebook(self.root)
        
        self.frame1 = tk.Frame(self.notebook)
        self.frame2 = tk.Frame(self.notebook)
        self.frame3 = tk.Frame(self.notebook)

        self.notebook.add(self.frame1, text="Men Shoes")
        self.notebook.add(self.frame2, text="Women Shoes")
        self.notebook.add(self.frame3, text="Kids Shoes")
        self.notebook.pack(expand=True, fill="both")

        #frame1
        # self.img1 = Image.open("/Users/bhardwaj/Documents/pictures for project/mike-petrucci-c9FQyqIECds-unsplash.jpg")
        # self.resized_image1 = self.img1.resize((1035, 850), Image.LANCZOS)
        # self.image_tk1 = ImageTk.PhotoImage(self.resized_image1)
        # self.background_label1 = tk.Label(self.frame1, image=self.image_tk1)
        # self.background_label1.image = self.image_tk1
        # self.background_label1.place(x=0, y=0, relwidth=1, relheight=1)
        # self.title1 = tk.Label(self.frame1, text="MEN SHOES", font=("Helvetica", 20, "bold"), bg="black", fg="white")
        # self.title1.place(x=450, y=10)

        self.Canvas= tk.Canvas(self.frame1, bg="black", height=850, width=1035)
        self.Canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.Shoes1img = Image.open("/Users/bhardwaj/Documents/pictures for project/men_shoes1.jpeg")
        self.Shoes1img = self.Shoes1img.resize((200, 200), Image.LANCZOS)
        self.Shoes1img = ImageTk.PhotoImage(self.Shoes1img)
        self.Shoes1 = tk.Label(self.Canvas, image=self.Shoes1img, bg="black")
        self.Shoes1.image = self.Shoes1img
        self.Shoes1.place(x=50, y=50)
        self.Shoes1title = tk.Label(self.Canvas, text="Shoes 1", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes1title.place(x=50, y=250)
        self.Shoes1price = tk.Label(self.Canvas, text="Price: $50", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes1price.place(x=50, y=280)
        #dropdown menu for size
        self.Shoes1size = ttk.Combobox(self.Canvas, values=[7, 8, 9, 10, 11, 12], state="readonly")
        self.Shoes1size.place(x=50, y=310)
        self.Shoes1size.set("Select Size")

        self.Shoes1button = Button(self.Canvas, text="Add to Cart", bg="yellow", fg="black", highlightbackground="black", borderless=1)
        self.Shoes1button.place(x=50, y=350)

        self.Shoes2img = Image.open("/Users/bhardwaj/Documents/pictures for project/men_shoes3.jpeg")
        self.Shoes2img = self.Shoes2img.resize((200, 200), Image.LANCZOS)
        self.Shoes2img = ImageTk.PhotoImage(self.Shoes2img)
        self.Shoes2 = tk.Label(self.Canvas, image=self.Shoes2img, bg="black")
        self.Shoes2.image = self.Shoes2img
        self.Shoes2.place(x=300, y=50)
        self.Shoes2title = tk.Label(self.Canvas, text="Shoes 2", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes2title.place(x=300, y=250)
        self.Shoes2price = tk.Label(self.Canvas, text="Price: $60", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes2price.place(x=300, y=280)
        #dropdown menu for size
        self.Shoes2size = ttk.Combobox(self.Canvas, values=[7, 8, 9, 10, 11, 12], state="readonly")
        self.Shoes2size.place(x=300, y=310)
        self.Shoes2size.set("Select Size")
        self.Shoes2button = Button(self.Canvas, text="Add to Cart", bg="yellow", fg="black", highlightbackground="black", borderless=1)
        self.Shoes2button.place(x=300, y=350)

        self.Shoes3img = Image.open("/Users/bhardwaj/Documents/pictures for project/jordans.jpeg")
        self.Shoes3img = self.Shoes3img.resize((200, 200), Image.LANCZOS)
        self.Shoes3img = ImageTk.PhotoImage(self.Shoes3img)
        self.Shoes3 = tk.Label(self.Canvas, image=self.Shoes3img, bg="black")
        self.Shoes3.image = self.Shoes3img
        self.Shoes3.place(x=550, y=50)
        self.Shoes3title = tk.Label(self.Canvas, text="Shoes 3", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes3title.place(x=550, y=250)
        self.Shoes3price = tk.Label(self.Canvas, text="Price: $100", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes3price.place(x=550, y=280)
        #dropdown menu for size
        self.Shoes3size = ttk.Combobox(self.Canvas, values=[7, 8, 9, 10, 11, 12], state="readonly")
        self.Shoes3size.place(x=550, y=310)
        self.Shoes3size.set("Select Size")
        self.Shoes3button = Button(self.Canvas, text="Add to Cart", bg="yellow", fg="black", highlightbackground="black", borderless=1)
        self.Shoes3button.place(x=550, y=350)

        self.Shoes4img = Image.open("/Users/bhardwaj/Documents/pictures for project/footballshoes.jpeg")
        self.Shoes4img = self.Shoes4img.resize((200, 200), Image.LANCZOS)
        self.Shoes4img = ImageTk.PhotoImage(self.Shoes4img)
        self.Shoes4 = tk.Label(self.Canvas, image=self.Shoes4img, bg="black")
        self.Shoes4.image = self.Shoes4img
        self.Shoes4.place(x=800, y=50)
        self.Shoes4title = tk.Label(self.Canvas, text="Shoes 4", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes4title.place(x=800, y=250)
        self.Shoes4price = tk.Label(self.Canvas, text="Price: $80", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes4price.place(x=800, y=280)
        #dropdown menu for size
        self.Shoes4size = ttk.Combobox(self.Canvas, values=[7, 8, 9, 10, 11, 12], state="readonly")
        self.Shoes4size.place(x=800, y=310)
        self.Shoes4size.set("Select Size")
        self.Shoes4button = Button(self.Canvas, text="Add to Cart", bg="yellow", fg="black", highlightbackground="black", borderless=1)
        self.Shoes4button.place(x=800, y=350)

        

        #frame2
        # self.img2 = Image.open("/Users/bhardwaj/Documents/pictures for project/women_shoes.png")
        # self.resized_image2 = self.img2.resize((1035, 850), Image.LANCZOS)
        # self.image_tk2 = ImageTk.PhotoImage(self.resized_image2)
        # self.background_label2 = tk.Label(self.frame2, image=self.image_tk2)
        # self.background_label2.image = self.image_tk2
        # self.background_label2.place(x=0, y=0, relwidth=1, relheight=1)
        # self.title2 = tk.Label(self.frame2, text="WOMEN SHOES", font=("Helvetica", 20, "bold"), bg="black", fg="white")
        # self.title2.place(x=450, y=10)

        self.Canvas2= tk.Canvas(self.frame2, bg="black", height=850, width=1035)
        self.Canvas2.place(x=0, y=0, relwidth=1, relheight=1)
        self.Shoes5img = Image.open("/Users/bhardwaj/Documents/pictures for project/women_shoes1.webp")
        self.Shoes5img = self.Shoes5img.resize((200, 200), Image.LANCZOS)
        self.Shoes5img = ImageTk.PhotoImage(self.Shoes5img)
        self.Shoes5 = tk.Label(self.Canvas2, image=self.Shoes5img, bg="black")
        self.Shoes5.image = self.Shoes5img
        self.Shoes5.place(x=50, y=50)
        self.Shoes5title = tk.Label(self.Canvas2, text="Shoes 5", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes5title.place(x=50, y=250)
        self.Shoes5price = tk.Label(self.Canvas2, text="Price: $50", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes5price.place(x=50, y=280)
        #dropdown menu for size
        self.Shoes5size = ttk.Combobox(self.Canvas2, values=[7, 8, 9, 10, 11, 12], state="readonly")
        self.Shoes5size.place(x=50, y=310)
        self.Shoes5size.set("Select Size")
        self.Shoes5button = Button(self.Canvas2, text="Add to Cart", bg="yellow", fg="black", highlightbackground="black", borderless=1)
        self.Shoes5button.place(x=50, y=350)

        self.Shoes6img = Image.open("/Users/bhardwaj/Documents/pictures for project/women_shoes3.jpeg")
        self.Shoes6img = self.Shoes6img.resize((200, 200), Image.LANCZOS)
        self.Shoes6img = ImageTk.PhotoImage(self.Shoes6img)
        self.Shoes6 = tk.Label(self.Canvas2, image=self.Shoes6img, bg="black")
        self.Shoes6.image = self.Shoes6img
        self.Shoes6.place(x=300, y=50)
        self.Shoes6title = tk.Label(self.Canvas2, text="Shoes 6", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes6title.place(x=300, y=250)
        self.Shoes6price = tk.Label(self.Canvas2, text="Price: $60", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes6price.place(x=300, y=280)
        #dropdown menu for size
        self.Shoes6size = ttk.Combobox(self.Canvas2, values=[7, 8, 9, 10, 11, 12], state="readonly")
        self.Shoes6size.place(x=300, y=310)
        self.Shoes6size.set("Select Size")
        self.Shoes6button = Button(self.Canvas2, text="Add to Cart", bg="yellow", fg="black", highlightbackground="black", borderless=1)
        self.Shoes6button.place(x=300, y=350)

        self.Shoes7img = Image.open("/Users/bhardwaj/Documents/pictures for project/women_shoes2.webp")
        self.Shoes7img = self.Shoes7img.resize((200, 200), Image.LANCZOS)
        self.Shoes7img = ImageTk.PhotoImage(self.Shoes7img)
        self.Shoes7 = tk.Label(self.Canvas2, image=self.Shoes7img, bg="black")
        self.Shoes7.image = self.Shoes7img
        self.Shoes7.place(x=550, y=50)
        self.Shoes7title = tk.Label(self.Canvas2, text="Shoes 7", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes7title.place(x=550, y=250)
        self.Shoes7price = tk.Label(self.Canvas2, text="Price: $100", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes7price.place(x=550, y=280)
        #dropdown menu for size
        self.Shoes7size = ttk.Combobox(self.Canvas2, values=[7, 8, 9, 10, 11, 12], state="readonly")
        self.Shoes7size.place(x=550, y=310)
        self.Shoes7size.set("Select Size")
        self.Shoes7button = Button(self.Canvas2, text="Add to Cart", bg="yellow", fg="black", highlightbackground="black", borderless=1)
        self.Shoes7button.place(x=550, y=350)

        self.Shoes8img = Image.open("/Users/bhardwaj/Documents/pictures for project/womenshoes5.webp")
        self.Shoes8img = self.Shoes8img.resize((200, 200), Image.LANCZOS)
        self.Shoes8img = ImageTk.PhotoImage(self.Shoes8img)
        self.Shoes8 = tk.Label(self.Canvas2, image=self.Shoes8img, bg="black")
        self.Shoes8.image = self.Shoes8img
        self.Shoes8.place(x=800, y=50)
        self.Shoes8title = tk.Label(self.Canvas2, text="Shoes 8", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes8title.place(x=800, y=250)
        self.Shoes8price = tk.Label(self.Canvas2, text="Price: $80", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes8price.place(x=800, y=280)
        #dropdown menu for size
        self.Shoes8size = ttk.Combobox(self.Canvas2, values=[7, 8, 9, 10, 11, 12], state="readonly")
        self.Shoes8size.place(x=800, y=310)
        self.Shoes8size.set("Select Size")
        self.Shoes8button = Button(self.Canvas2, text="Add to Cart", bg="yellow", fg="black", highlightbackground="black", borderless=1)
        self.Shoes8button.place(x=800, y=350)




        #frame3
        # self.img3 = Image.open("/Users/bhardwaj/Documents/pictures for project/kids_shoes.png")
        # self.resized_image3 = self.img3.resize((1035, 850), Image.LANCZOS)
        # self.image_tk3 = ImageTk.PhotoImage(self.resized_image3)
        # self.background_label3 = tk.Label(self.frame3, image=self.image_tk3)
        # self.background_label3.image = self.image_tk3
        # self.background_label3.place(x=0, y=0, relwidth=1, relheight=1)
        # self.title3 = tk.Label(self.frame3, text="KIDS SHOES", font=("Helvetica", 20, "bold"), bg="black", fg="white")
        # self.title3.place(x=450, y=10)

        self.Canvas3= tk.Canvas(self.frame3, bg="black", height=850, width=1035)
        self.Canvas3.place(x=0, y=0, relwidth=1, relheight=1)
        self.Shoes9img = Image.open("/Users/bhardwaj/Documents/pictures for project/kids_shoes.jpg")
        self.Shoes9img = self.Shoes9img.resize((200, 200), Image.LANCZOS)
        self.Shoes9img = ImageTk.PhotoImage(self.Shoes9img)
        self.Shoes9 = tk.Label(self.Canvas3, image=self.Shoes9img, bg="black")
        self.Shoes9.image = self.Shoes9img
        self.Shoes9.place(x=50, y=50)
        self.Shoes9title = tk.Label(self.Canvas3, text="Shoes 9", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes9title.place(x=50, y=250)
        self.Shoes9price = tk.Label(self.Canvas3, text="Price: $50", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes9price.place(x=50, y=280)
        #dropdown menu for size
        self.Shoes9size = ttk.Combobox(self.Canvas3, values=[7, 8, 9, 10, 11, 12], state="readonly")
        self.Shoes9size.place(x=50, y=310)
        self.Shoes9size.set("Select Size")
        self.Shoes9button = Button(self.Canvas3, text="Add to Cart", bg="yellow", fg="black", highlightbackground="black", borderless=1)
        self.Shoes9button.place(x=50, y=350)

        self.Shoes10img = Image.open("/Users/bhardwaj/Documents/pictures for project/kidsshoes2.webp")
        self.Shoes10img = self.Shoes10img.resize((200, 200), Image.LANCZOS)
        self.Shoes10img = ImageTk.PhotoImage(self.Shoes10img)
        self.Shoes10 = tk.Label(self.Canvas3, image=self.Shoes10img, bg="black")
        self.Shoes10.image = self.Shoes10img
        self.Shoes10.place(x=300, y=50)
        self.Shoes10title = tk.Label(self.Canvas3, text="Shoes 10", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes10title.place(x=300, y=250)
        self.Shoes10price = tk.Label(self.Canvas3, text="Price: $60", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes10price.place(x=300, y=280)
        #dropdown menu for size
        self.Shoes10size = ttk.Combobox(self.Canvas3, values=[7, 8, 9, 10, 11, 12], state="readonly")
        self.Shoes10size.place(x=300, y=310)
        self.Shoes10size.set("Select Size")
        self.Shoes10button = Button(self.Canvas3, text="Add to Cart", bg="yellow", fg="black", highlightbackground="black", borderless=1)
        self.Shoes10button.place(x=300, y=350)

        self.Shoes11img = Image.open("/Users/bhardwaj/Documents/pictures for project/kids_shoes3.webp")
        self.Shoes11img = self.Shoes11img.resize((200, 200), Image.LANCZOS)
        self.Shoes11img = ImageTk.PhotoImage(self.Shoes11img)
        self.Shoes11 = tk.Label(self.Canvas3, image=self.Shoes11img, bg="black")
        self.Shoes11.image = self.Shoes11img
        self.Shoes11.place(x=550, y=50)
        self.Shoes11title = tk.Label(self.Canvas3, text="Shoes 11", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes11title.place(x=550, y=250)
        self.Shoes11price = tk.Label(self.Canvas3, text="Price: $100", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        self.Shoes11price.place(x=550, y=280)
        #dropdown menu for size
        self.Shoes11size = ttk.Combobox(self.Canvas3, values=[7, 8, 9, 10, 11, 12], state="readonly")
        self.Shoes11size.place(x=550, y=310)
        self.Shoes11size.set("Select Size")
        self.Shoes11button = Button(self.Canvas3, text="Add to Cart", bg="yellow", fg="black", highlightbackground="black", borderless=1)
        self.Shoes11button.place(x=550, y=350)

    #function for cart
    def cart(self):
        pass




        


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

if __name__ == "__main__":
    root = tk.Tk()
    app = flipzon(root)
    
    # app.l_frame()
    # app.c_frame()
    # app.f_frame()
    # app.show_login()
    root.mainloop()

