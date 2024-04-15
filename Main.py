import shutil
import tkinter as tk
from tkinter import messagebox as mb
import mysql.connector as sql
from mysql.connector import Error
from PIL import Image, ImageTk
from tkmacosx import Button
from tkinter import ttk
from tkinter import filedialog
import os
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from fpdf import FPDF
import webbrowser
import xlsxwriter


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
    role VARCHAR(100) default 'user' NOT NULL,
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



class walkwise:

    def __init__(self,root):
        self.root = root
        self.root.title("Welcome to Walkwise")
        self.root.geometry("1300x700")
        self.root.configure(bg="white")
        self.root.attributes('-alpha', 1)
        #self.image_tk = None

        img = Image.open("/Users/bhardwaj/Downloads/loginpage.jpg")
        resized_image = img.resize((1035, 850), Image.LANCZOS)
        image_tk = ImageTk.PhotoImage(resized_image)

        self.background_label = tk.Label(root, image=image_tk)
        self.background_label.image = image_tk  # Keep a reference
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #self.login_frame.place(x=327,y=370,width=390)

        #cursor=conn.cursor()

        self.show_login()

        self.cart_items = []

    def show_login(self):
        for i in self.root.winfo_children():
            i.destroy()

        self.background_label = tk.Label(root)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.login_frame=tk.Frame(root, bg="#020c11")
        #place login frame on right side of the screen
        self.login_frame.place(x=800,y=150,width=400)
        
#         #adding login text on the top
#         self.login_label = tk.Label(self.login_frame, text="Login", font=("calibri", 20, "bold"), bg="white", fg="black")
#         self.login_label.place(x=850, y=200)
        
#         #adding username label
#         self.username_label = tk.Label(self.login_frame, text="_", font=("calibri", 18, "bold"), bg="black", fg="WHITE") 
#         self.username_label.place(x=760, y=270)
#         #adding password label
#         self.password_label = tk.Label(self.login_frame, text="_____", font=("calibri", 18, "bold"), bg="black", fg="WHITE")
#         self.password_label.place(x=760, y=340)
        
#         #adding password entry
#         self.password_entry = tk.Entry(self.login_frame,font=("calibri", 18), bg="black", width=28, bd=0,fg="white", relief="ridge",insertbackground="white")
#         self.password_entry.place(x=765, y=325)
#         self.password_entry.insert(0, "Password")
#         self.password_entry.bind('<FocusIn>', self.removepasswordtext)
#         self.password_entry.bind('<FocusOut>', self.removepasswordtext)
    
#         #adding username entry
#         self.username_entry = tk.Entry(self.login_frame,font=("calibri", 18), bg="black", width= 28, bd=0,fg="white", relief="ridge",insertbackground="white")
#         self.username_entry.place(x=765, y=260)
#         self.username_entry.insert(0, "Email")
#         #self.username_entry.bind("<Key>", self.removeusernametext)
#         self.username_entry.bind('<FocusIn>', self.removeusernametext)
#         self.username_entry.bind('<FocusOut>', self.removeusernametext)
        
#         #adding show password icon
#         show_icon_image = Image.open("/Users/bhardwaj/Downloads/WhatsApp Image 2024-03-26 at 12.46.45 AM (1).jpeg")
#         show_icon_resized = show_icon_image.resize((30, 30), Image.Resampling.LANCZOS)  
#         self.show_icon = ImageTk.PhotoImage(show_icon_resized)

#         # Open and resize the hide icon
#         hide_icon_image = Image.open("/Users/bhardwaj/Downloads/WhatsApp Image 2024-03-26 at 12.46.45 AM.jpeg")
#         hide_icon_resized = hide_icon_image.resize((30, 30), Image.Resampling.LANCZOS)  
#         self.hide_icon = ImageTk.PhotoImage(hide_icon_resized)


#         # Create a button to toggle password visibility
#         self.toggle_button = tk.Button(self.login_frame, image=self.show_icon, command=self.toggle_password_visibility, borderwidth=0,highlightthickness=0, bg="black", activebackground="black")
#         self.toggle_button.place(x=1050, y=330)
        
        
#         #adding login button
#         self.login_button = Button(self.login_frame, text="Login", font=("calibri",18,"bold"), bg="black", fg="white", bd=0, cursor="hand2",activebackground="black",activeforeground="grey", command=self.login)
#         self.login_button.place(x=800, y=400)
#         #adding signup button
#         self.signup_button = Button(self.login_frame, text="Sign Up", font=("calibri",18,"bold"), bg="black", fg="white", bd=0, cursor="hand2",activebackground="black",activeforeground="grey",command=self.show_create_account_screen)
#         self.signup_button.place(x=950, y=400)
#         #adding forgot password button
#         self.login_forgot_password_button = Button(self.login_frame, text="Forgot Password?", font=("calibri",10,"bold"), bg="black", fg="light blue", bd=0, cursor="hand2",activebackground="black",activeforeground="grey")
#         self.login_forgot_password_button.place(x=960, y=380)
#         self.login_forgot_password_button.config(command=self.show_create_account_screen)

        
        self.update_background_image("/Users/bhardwaj/Downloads/loginpage.jpg")
# #method for show and hide password icon
#     def toggle_password_visibility(self):
#         if self.password_visible:
#             # Hide the password and update the button icon
#             self.password_entry.config(show="*")
#             self.toggle_button.config(image=self.show_icon)
#             self.password_visible = False
#         else:
#             # Show the password and update the button icon
#             self.password_entry.config(show="")
#             self.toggle_button.config(image=self.hide_icon)
#             self.password_visible = True
    
#     #creating entry lable inside the username entry
#     def removeusernametext(self, event):
#         if self.username_entry.get() == "Email":
#             self.username_entry.delete(0, "end")
#             self.username_entry.config(fg="white")
#         elif self.username_entry.get() == "":
#             self.username_entry.insert(0, "Email")
#             self.username_entry.config(fg="white") 
#     def removepasswordtext(self, event):
#         if self.password_entry.get() == "Password":
#             self.password_entry.delete(0, "end")
#             self.password_entry.config(fg="white")
#             self.password_entry.config(show="*")
#         elif self.password_entry.get() == "":
#             self.password_entry.insert(0, "Password")
#             self.password_entry.config(show="")
#             self.password_entry.config(fg="white")
        # login_frame.place(x=0,y=0,relheight=1, relwidth=1)
        # login_frame.attributes('-alpha', 0.9)
        self.login_label = tk.Label(self.login_frame, text="Login",bg="#020c11",fg="white",font=("Calibri","70"))
        self.login_label.grid(row=0,column=2,padx=5,pady=10,sticky="w")
        self.login_username_label= tk.Label(self.login_frame, text="Username",bg="#020c11",fg="white",font=("Calibri","25","bold"),pady=5)
        self.login_username_entry= tk.Entry(self.login_frame,font=("Calibri","15"))    
        self.login_password_label= tk.Label(self.login_frame, text="Password",bg="#020c11",fg="white",font=("Calibri","25","bold"))
        self.login_password_entry= tk.Entry(self.login_frame,show="*",font=("Calibri","15"))
        self.login_button = Button(self.login_frame, text="Login",bg="#020c11",fg="white",command=self.login,highlightbackground="grey",borderless=1,font=("Calibri","20"))
        self.forgot_password_button = Button(self.login_frame, text="Forgot password?",bg="#020c11",fg="white",command=self.show_forgot_password_screen,highlightbackground="grey",borderless=1,font=("Calibri","15"))
        self.createacc_button= Button(self.login_frame, text="New User? Create Your account",bg="#020c11",fg="white",command=self.show_create_account_screen,highlightbackground="grey",borderless=1,font=("Calibri","15"))

        self.login_username_label.grid(row=1,column=1)
        self.login_username_entry.grid(row=1, column=2)
        self.login_password_label.grid(row=2,column=1)
        self.login_password_entry.grid(row=2,column=2)
        self.login_button.grid(row=3,column=2,pady="10")
        self.forgot_password_button.grid(row=4,column=2,padx=5)
        # self.createacc_button.place(x=10, y=170, width=200, height=30)

        self.createacc_button.grid(row=7,column=2,columnspan=3,pady="10")
        #self.l_frame()
        #self.destroy_background_image()
        # self.create_account_frame.pack_forget()
        # self.forgot_password_frame.pack_forget()
        
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

        self.update_background_image("/Users/bhardwaj/Downloads/WhatsApp Image 2024-03-28 at 10.39.25 PM.jpeg")

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
        self.flogin_password_entry= tk.Entry(self.forgot_password_frame,show="*")
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
        self.update_background_image("/Users/bhardwaj/Downloads/WhatsApp Image 2024-03-28 at 10.33.10 PM.jpeg")

#Function to create account
    def create_account(self):
        c_firstname=self.create_firstname_entry.get()
        c_lastname=self.create_lastname_entry.get()
        c_phone=self.create_phone_entry.get()
        c_address=self.create_address_entry.get()
        c_email=self.create_email_entry.get()
        c_username=self.create_username_entry.get()
        c_password=self.create_password_entry.get()

        #email validation
        if not re.match(r"[^@]+@[^@]+\.[^@]+", c_email):
            mb.showinfo(title="Invalid Email", message="Please enter a valid email address")
        

        #password validation for length and special characters
        elif not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", c_password):
            mb.showinfo(title="Invalid Password", message="Password must contain at least 8 characters, one letter, one number and one special character")
        
            
        #phone number validation
        elif not re.match(r"[0-9]{10}", c_phone) and len(c_phone) != 10:
            mb.showinfo(title="Invalid Phone Number", message="Please enter a valid phone number")
        

        elif c_username == "" or c_password == "" :
            mb.showinfo(title = "Fields are empty",message="create a username and password for your account" )
        else:
            con = sql.connect(host="localhost", user="root", password="0139612345", database="login_details")
            cursor=con.cursor()
            #cursor.execute("CREATE TABLE IF NOT EXISTS users (username VARCHAR(255), password VARCHAR(255))")

            #check if username already exists
            cursor.execute("SELECT * FROM user_details WHERE username = %s", (c_username,))
            user = cursor.fetchone()
            if user:
                mb.showinfo(title="Username exists", message="Username already exists, please try another")
            else:

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
            self.user = cursor.fetchone()

            if self.user:
                # self.currentuser_username=e_username
                # self.currentuser_role=self.user[3]
                mb.showinfo(title="Login successful", message="Welcome, " + e_username)
                print(self.user[3])
                if self.user[3]=='admin':
                    self.adminpage()
                    #self.catalog()
                
                else:
                    self.catalog()
            
            else:
                mb.showinfo(title = "Login Usuccessful",message="Username or Password are incorrect. If you are new user create a new account" )
            con.commit()
            con.close()
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
                    if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", f_password):
                        mb.showinfo(title="Invalid Password", message="Password must contain at least 8 characters, one letter, one number and one special character")
                    else:
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
            mb.showerror("Error", "Invalid username")
                    
        con.close()


    def update_background_image(self,image_path):
        img = Image.open(image_path)
        resized_image = img.resize((1295, 695), Image.LANCZOS)
        image_tk = ImageTk.PhotoImage(resized_image)
        self.background_label.configure(image=image_tk)
        self.background_label.image = image_tk

    def destroy_background_image(self):
        if hasattr(self, 'background_label') and self.background_label.winfo_exists():
             self.background_label.destroy()

    def adminpage(self):
        for i in self.root.winfo_children():
            i.destroy()
            
        self.background_label = tk.Label(root)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.update_background_image("/Users/bhardwaj/Downloads/WhatsApp Image 2024-04-08 at 2.14.33 PM.jpeg")
        
        self.admin_frame=tk.Frame(root,bg="#232323")
        self.admin_label = tk.Label(self.admin_frame, text="Welcome to Admin Page",font=("Helvetica",20,"bold"),bg="#232323",fg="white")
        self.admin_label.grid(row=0,column=0,columnspan=5,pady=10,sticky="w")
        
        self.admin_shoe_name_label= tk.Label(self.admin_frame, text="Shoe Name",bg="#232323",fg="azure",font=("Calibri","15","bold"))
        self.admin_shoe_name_entry= tk.Entry(self.admin_frame)
        self.admin_shoe_price_label= tk.Label(self.admin_frame, text="Shoe Price",bg="#232323",font=("Calibri","15","bold"))
        self.admin_shoe_price_entry= tk.Entry(self.admin_frame)
        #dropdown menu for shoe type
        options = {'men','women','kids'}
        self.admin_shoe_type_option = tk.StringVar(self.admin_frame)
        self.admin_shoe_type_option.set('Select Shoe Type')
        self.admin_shoe_type_option_menu = tk.OptionMenu(self.admin_frame, self.admin_shoe_type_option, *options)
        self.admin_shoe_type_option_menu.config(width=15)
        self.admin_shoe_type_label= tk.Label(self.admin_frame, text="Shoe Type",bg="#232323",font=("Calibri","15","bold"))
        self.admin_shoe_type_option_menu.grid(row=3,column=1)

        # self.admin_shoe_type_label= tk.Label(self.admin_frame, text="Shoe Type",bg="black",font=("Calibri","15","bold"))
        # self.admin_shoe_type_entry= tk.Entry(self.admin_frame)
        self.admin_shoe_image_label= tk.Label(self.admin_frame, text="Shoe Image",bg="#232323",font=("Calibri","15","bold"))
        self.admin_shoe_image_button= Button(self.admin_frame, text="Upload Image",bg="yellow",command=self.upload_image,highlightbackground="black",borderless=1)
        self.admin_add_to_catalog_button = Button(self.admin_frame, text="Add to Catalog",bg="yellow",command=self.add_to_catalog,highlightbackground="black",borderless=1)
        self.admin_catalog_button = Button(self.admin_frame, text="Catalog",bg="yellow",command=self.catalog,highlightbackground="black",borderless=1)

        self.admin_shoe_name_label.grid(row=1,column=0)
        self.admin_shoe_name_entry.grid(row=1, column=1)
        self.admin_shoe_price_label.grid(row=2,column=0)
        self.admin_shoe_price_entry.grid(row=2,column=1)
        self.admin_shoe_type_label.grid(row=3,column=0)
        # self.admin_shoe_type_entry.grid(row=3,column=1)
        self.admin_shoe_image_label.grid(row=4,column=0)
        self.admin_shoe_image_button.grid(row=4,column=1)
        self.admin_add_to_catalog_button.grid(row=5,column=0,columnspan=2,pady="10")
        self.admin_catalog_button.grid(row=6,column=0,columnspan=2,pady="10")


        self.admin_frame.place(x=430,y=230,width=400,height=300)
        #self.admin_frame.pack()

    #upload image
    def upload_image(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("JPEG files", "*.jpeg"),("JPG files", "*.jpg"), ("PNG files", "*.png"),("all files", "*.*")))
        print(self.filename)

        #messagebox.showinfo("Success", "Image Uploaded")
        if self.filename:

            mb.showinfo("Success", "Image Uploaded")
            self.admin_shoe_image_button.config(text="Image Uploaded")
        else:
            mb.showinfo("Error", "No Image Selected")


        #update insert movie page image button admin_shoe_image_button
        #self.admin_shoe_image_button.config(text="Image Uploaded")

    #function to add to catalog
    def add_to_catalog(self):
        shoe_name=self.admin_shoe_name_entry.get()
        shoe_price=self.admin_shoe_price_entry.get()
        shoe_type=self.admin_shoe_type_option.get()
        shoe_image=self.filename    
        print(shoe_name, shoe_price,shoe_type, shoe_image)

        con = sql.connect(host="localhost", user="root", password="0139612345", database="login_details")
        cursor=con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS catalog (shoe_id INT AUTO_INCREMENT PRIMARY KEY, shoe_name VARCHAR(100) NOT NULL, shoe_price VARCHAR(100) NOT NULL,shoe_type VARCHAR(100) NOT NULL, shoe_image VARCHAR(100) NOT NULL)")
        cursor.execute("INSERT INTO catalog (shoe_name, shoe_price, shoe_type, shoe_image) VALUES (%s, %s, %s, %s)", (shoe_name, shoe_price, shoe_type, shoe_image))
        con.commit()
        con.close()
        mb.showinfo("Success", "Shoe added to catalog")

    #function to display a catalog of products using notebook
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
        
        #connect to the database
        con = sql.connect(host="localhost", user="root", password="0139612345", database="login_details")

        cursor=con.cursor()
        cursor.execute("SELECT * FROM catalog")
        shoes = cursor.fetchall()
        con.close()

        #print shoes based on type
        # for i, shoe in enumerate(shoes):
        #     shoe=list(shoe)
        #     shoe = {
        #             "shoe_id": shoe[0],
        #             "shoe_name": shoe[1],
        #             "shoe_price": shoe[2],
        #             "shoe_type": shoe[3],
        #             "shoe_image": shoe[4]
        #         }
        #     print(shoe)

        

        #print all the shoes in the catalog
        #iterate one by one from all shoes and display images
        for i, shoe in enumerate(shoes):
            #display shoe image as button
            shoe=list(shoe)
            shoe = {
                    "shoe_id": shoe[0],
                    "shoe_name": shoe[1],
                    "shoe_price": shoe[2],
                    "shoe_type": shoe[3],
                    "shoe_image": shoe[4]
                }
            if shoe["shoe_type"] == "men":

                image = Image.open(shoe["shoe_image"])
                image = image.resize((150, 200), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                row = i // 6  # integer division to get row number
                col = i % 6 # modulo operator to get column number

                catalog_shoe_button = tk.Button(self.frame1, image=photo, command=lambda shoe=shoe: self.show_shoe_details(shoe))
                catalog_shoe_button.image = photo
                catalog_shoe_button.grid(row=row, column=col, padx=5, pady=5)

            elif shoe["shoe_type"] == "women":
                image = Image.open(shoe["shoe_image"])
                image = image.resize((150, 200), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                row = i // 6  # integer division to get row number
                col = i % 6 # modulo operator to get column number

                catalog_shoe_button = tk.Button(self.frame2, image=photo, command=lambda shoe=shoe: self.show_shoe_details(shoe))
                catalog_shoe_button.image = photo
                catalog_shoe_button.grid(row=row, column=col, padx=5, pady=5)

            elif shoe["shoe_type"] == "kids":
                image = Image.open(shoe["shoe_image"])
                image = image.resize((150, 200), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                row = i // 6
                col = i % 6

                catalog_shoe_button = tk.Button(self.frame3, image=photo, command=lambda shoe=shoe: self.show_shoe_details(shoe))
                catalog_shoe_button.image = photo
                catalog_shoe_button.grid(row=row, column=col, padx=5, pady=5)

    #lopout button
        logout_button = tk.Button(self.root, text="logout", command=self.show_login)
        logout_button.place(x=10, y=10)
        

    
    #view cart icon
        cart_image = Image.open("/Users/bhardwaj/Documents/pictures for project/cart.png")
        cart_image = cart_image.resize((50, 50), Image.LANCZOS)
        cart_photo = ImageTk.PhotoImage(cart_image)
        cart_button = tk.Button(self.root, image=cart_photo, command=self.cart)
        cart_button.image = cart_photo
        cart_button.place(x=950, y=10)

        #report button if admin is logged in
        if self.user[3] == "admin":
            report_button = tk.Button(self.root, text="Report", command=self.report)
            report_button.place(x=1100, y=10)

    def report(self):
        con = sql.connect(host="localhost", user="root", password="0139612345", database="login_details")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM catalog")
        shoes = cursor.fetchall()
        con.close()

        # Create a new workbook and add a worksheet
        workbook = xlsxwriter.Workbook("catalog.xlsx")
        worksheet = workbook.add_worksheet()

        # Add a bold format to use to highlight cells
        bold = workbook.add_format({"bold": True})

        # Write some data headers
        worksheet.write("A1", "Shoe ID", bold)
        worksheet.write("B1", "Shoe Name", bold)
        worksheet.write("C1", "Shoe Price", bold)
        worksheet.write("D1", "Shoe Type", bold)
        worksheet.write("E1", "Shoe Image", bold)

        # Start from the first cell below the headers
        row = 1
        col = 0

        # Iterate over the data and write it out row by row
        for shoe in shoes:
            worksheet.write(row, col, shoe[0])
            worksheet.write(row, col + 1, shoe[1])
            worksheet.write(row, col + 2, shoe[2])
            worksheet.write(row, col + 3, shoe[3])
            worksheet.write(row, col + 4, shoe[4])
            row += 1
            
        workbook.close()
        mb.showinfo("Success", "Report generated successfully")

        #ask location to save the file and download the file
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            shutil.move("catalog.xlsx", file_path)
            mb.showinfo("Success", "Report downloaded successfully")
            


        

        



    def show_shoe_details(self, shoe):
        
        
        shoe_details_frame = tk.Frame(self.root, bg="black")
        shoe_details_frame.place(x=0, y=0, relwidth=1, relheight=1)
        # Load the background image
        # bg_image = Image.open("/Users/bhardwaj/Documents/pictures for project/JPEG image-4FFE-866D-43-0.jpeg")
        # bg_image = bg_image.resize((1035, 850), Image.LANCZOS)  # Adjust the size as needed
        # bg_photo = ImageTk.PhotoImage(bg_image)

        # # Create a label with the background image
        # bg_label = tk.Label(shoe_details_frame, image=bg_photo)
        # bg_label.image = bg_photo
        # bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # #display shoe deatils to the right of the image
        # shoe_name_label = tk.Label(shoe_details_frame, text=shoe["shoe_name"], font=("Helvetica", 20, "bold"), bg="black", fg="white")
        # shoe_name_label.place(x=10, y=10)
        # shoe_price_label = tk.Label(shoe_details_frame, text=shoe["shoe_price"], font=("Helvetica", 20, "bold"), bg="black", fg="white")
        # shoe_price_label.place(x=10, y=50)
        # shoe_type_label = tk.Label(shoe_details_frame, text=shoe["shoe_type"], font=("Helvetica", 20, "bold"), bg="black", fg="white")
        # shoe_type_label.place(x=10, y=90)
        #display the shoe image to the left of the details
        image = Image.open(shoe["shoe_image"])
        image = image.resize((350, 400), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        shoe_image_label = tk.Label(shoe_details_frame, image=photo)
        shoe_image_label.image = photo
        shoe_image_label.place(x=10, y=130)
        #shoe_image_label.pack(side=tk.LEFT, padx=20, pady=20)
        # add_to_cart_button = tk.Button(shoe_details_frame, text="Add to Cart", command=lambda: self.cart(shoe["shoe_name"], shoe["shoe_price"], shoe["shoe_type"], shoe["shoe_image"]))
        # add_to_cart_button.pack(pady=10)
        # back_button = tk.Button(shoe_details_frame, text="Back", command=shoe_details_frame.destroy)
        # back_button.pack(pady=10)
        shoe_name_label = tk.Label(shoe_details_frame, text=shoe["shoe_name"], font=("Calibri", 52, "bold","italic"), bg="black",fg="white")
        shoe_name_label.place(x=550, y=170)

        shoe_price_label = tk.Label(shoe_details_frame, text=shoe["shoe_price"], font=("Calibri", 30, "bold"), bg="black", fg="white")
        shoe_price_label.place(x=550, y=270)

        shoe_type_label = tk.Label(shoe_details_frame, text=shoe["shoe_type"], font=("Calibri", 20, "bold"), bg="black", fg="white")
        shoe_type_label.place(x=550, y=330)

        #dropdown for shoe size
        #arrange the options for the dropdown
        options = ['6','7','8','9','10','11','12']
        #Sort the options list as strings converted to integers
        options.sort(key=int)
        
        self.shoe_size_option = tk.StringVar(shoe_details_frame)
        self.shoe_size_option.set('Select Shoe Size')
        # self.shoe_size_combo = ttk.Combobox(shoe_details_frame, textvariable=self.shoe_size_option, values=options) 
        # self.shoe_size_combo.config(width=15)
        # self.shoe_size_combo.place(x=550, y=390)

        self.shoe_size_option_menu = tk.OptionMenu(shoe_details_frame, self.shoe_size_option, *options)
        self.shoe_size_option_menu.config(width=15)
        self.shoe_size_label= tk.Label(shoe_details_frame, text="Shoe Size", font=("Calibri","15","bold"), bg="gray", fg="white",highlightbackground="#f3e7c4")
        self.shoe_size_option_menu.place(x=550, y=390)

        #size chart hyperlink with underline
        size_chart_label = tk.Label(shoe_details_frame, text="Size Chart", font=("Calibri", 15, "underline","bold"), bg="black", fg="white",highlightbackground="#f3e7c4")
        size_chart_label.place(x=550, y=420)
        size_chart_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.shoecarnival.com/content/sizechart"))

        add_to_cart_button = Button(shoe_details_frame, text="Add to Cart",bg="gray",borderless=1, command=lambda: self.handle_add_to_cart(shoe["shoe_name"], shoe["shoe_price"], shoe["shoe_type"], shoe["shoe_image"]),highlightbackground="#f3e7c4")
        add_to_cart_button.place(x=550, y=470)

        back_button = Button(shoe_details_frame, text="Back",bg="gray", command=shoe_details_frame.destroy,highlightbackground="#f3e7c4",borderless=1)
        back_button.place(x=550, y=520)

        #continue shopping button
        # continue_shopping_button = Button(shoe_details_frame, text="Continue Shopping",bg="gray", command=self.catalog,highlightbackground="#f3e7c4",borderless=1)
        # continue_shopping_button.place(x=580, y=520)

        #view cart button
        view_cart_button = Button(shoe_details_frame, text="View Cart",bg="gray", command=self.cart,highlightbackground="#f3e7c4",borderless=1)
        view_cart_button.place(x=550, y=570)
        # view_cart_button = Button(shoe_details_frame, text="View Cart",bg="gray", command=self.cart ,highlightbackground="#f3e7c4",borderless=1)
        # view_cart_button.place(x=580, y=570)

        
        #self.update_background_image("/Users/bhardwaj/Documents/pictures for project/bg2.jpeg")



        #delete button if user is admin
        if self.user[3] == "admin":
            delete_button = tk.Button(shoe_details_frame, text="Delete", command=lambda: self.delete_product(shoe["shoe_name"]))
            delete_button.pack(pady=10)

    def handle_add_to_cart(self, shoe_name=None, shoe_price=None, shoe_type=None, shoe_image=None, shoe_size=None):

        shoe_size = self.shoe_size_option.get()
        if shoe_size == 'Select Shoe Size':
            mb.showerror("Error", "Please select a shoe size.")
        else:
            if shoe_name and shoe_price and shoe_type and shoe_image and shoe_size:
                item = {"name": shoe_name, "price": shoe_price, "type": shoe_type, "image_path": shoe_image, "size": shoe_size}
                self.cart_items.append(item)


            mb.showinfo("Success", "Added to cart")


    def cart(self, shoe_name=None, shoe_price=None, shoe_type=None, shoe_image=None):
        # shoe_size = self.shoe_size_option.get()
        # if shoe_size == 'Select Shoe Size':
        #     mb.showerror("Error", "Please select a shoe size.")
        # else:
            
        #     mb.showinfo("Success", "Added to cart")

        
    # Add selected item to the cart_items list
        # if shoe_name and shoe_price and shoe_type and shoe_image:
        #     item = {"name": shoe_name, "price": shoe_price, "type": shoe_type, "image_path": shoe_image}
        #     self.cart_items.append(item)

    # Create a new frame for the cart
        self.cart_frame = tk.Frame(self.root, bg="white")
        self.cart_frame.place(x=0, y=0, relwidth=1, relheight=1)
    
    #if cart is empty, display a message
        if not self.cart_items:
            label = tk.Label(self.cart_frame, text="Cart is empty", font=("Helvetica", 20, "bold"), bg="white", fg="black")
            label.pack(pady=10)
    

    # Display cart items in the cart frame
        for idx, item in enumerate(self.cart_items):
            if item:
                self.item_frame = tk.Frame(self.cart_frame, bg="white", bd=1, relief=tk.SOLID)
                self.item_frame.pack(fill=tk.BOTH, padx=10, pady=5)

                # Shoe image
                image = Image.open(item["image_path"])
                image = image.resize((100, 150), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                shoe_image_label = tk.Label(self.item_frame, image=photo, bg="white")
                shoe_image_label.image = photo
                shoe_image_label.pack(side=tk.LEFT, padx=10, pady=10)

                # Shoe details
                self.details_frame = tk.Frame(self.item_frame, bg="white")
                self.details_frame.pack(side=tk.LEFT, padx=10, pady=10)

                shoe_name_label = tk.Label(self.details_frame, text=item["name"], font=("Helvetica", 16, "bold"), bg="white", fg="black")
                shoe_name_label.pack(anchor=tk.W)

                price_label = tk.Label(self.details_frame, text=f"Price: {item['price']}", font=("Helvetica", 14), bg="white", fg="black")
                price_label.pack(anchor=tk.W)

                type_label = tk.Label(self.details_frame, text=f"type: {item['type']}", font=("Helvetica", 14), bg="white", fg="black")
                type_label.pack(anchor=tk.W)

                #size details
                size_label = tk.Label(self.details_frame, text=f"Size: {self.shoe_size_option.get()}", font=("Helvetica", 14), bg="white", fg="black")
                size_label.pack(anchor=tk.W)

                # Remove from cart button
                remove_from_cart_button = tk.Button(self.item_frame, text="Remove from Cart", command=lambda shoe=item["name"]: self.remove_from_cart(shoe))
                remove_from_cart_button.pack(side=tk.RIGHT, padx=10, pady=10)


    # Continue shopping button
        continue_shopping_button = tk.Button(self.cart_frame, text="Continue Shopping", command=self.catalog)
        continue_shopping_button.pack(pady=10)

    # Order button
        order_button = tk.Button(self.cart_frame, text="Place Order", command=self.place_order)
        order_button.pack(pady=10)

    def remove_from_cart(self, shoe_name):
        #print self.cart_items
        print(self.cart_items, shoe_name)
        # Remove the item from the cart_items list
        for item in self.cart_items:
            if item["name"] == shoe_name:
                self.cart_items.remove(item)
                break

        # If the cart is empty, display a message
        if not self.cart_items:
            self.cart_frame.destroy()
            mb.showinfo("Success", "Cart is empty")
        

        else:
            self.cart_frame.destroy()
        
            self.cart()

        # # Destroy the item frame
        # self.item_frame.destroy()
        
        #after removing the item, display the updated cart
       


        
        





                          










     
    #order page function
    def place_order(self):
        #print the cart items in a new window
        order_frame = tk.Frame(self.root, bg="white")
        order_frame.place(x=0, y=0, relwidth=1, relheight=1)
        #display the cart items in the order frame
        for idx, item in enumerate(self.cart_items):
            if item:
                self.item_frame = tk.Frame(order_frame, bg="white", bd=1, relief=tk.SOLID)
                self.item_frame.pack(fill=tk.BOTH, padx=10, pady=5)

                # Shoe image
                image = Image.open(item["image_path"])
                image = image.resize((100, 150), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                shoe_image_label = tk.Label(self.item_frame, image=photo, bg="white")
                shoe_image_label.image = photo
                shoe_image_label.pack(side=tk.LEFT, padx=10, pady=10)

                # Shoe details
                self.details_frame = tk.Frame(self.item_frame, bg="white")
                self.details_frame.pack(side=tk.LEFT, padx=10, pady=10)

                shoe_name_label = tk.Label(self.details_frame, text=item["name"], font=("Helvetica", 16, "bold"), bg="white", fg="black")
                shoe_name_label.pack(anchor=tk.W)

                price_label = tk.Label(self.details_frame, text=f"Price: {item['price']}", font=("Helvetica", 14), bg="white", fg="black")
                price_label.pack(anchor=tk.W)

                type_label = tk.Label(self.details_frame, text=f"type: {item['type']}", font=("Helvetica", 14), bg="white", fg="black")
                type_label.pack(anchor=tk.W)

                #size details
                size_label = tk.Label(self.details_frame, text=f"Size: {item['size']}", font=("Helvetica", 14), bg="white", fg="black")
                size_label.pack(anchor=tk.W)

        # confirm Order button
        c_email = self.user[6]
        print(c_email)
        order_button = tk.Button(order_frame, text="Confirm order", command=lambda: self.place_order_to_db(c_email))
        order_button.pack(pady=10)

    #function to place order and generate a invoice
    def place_order_to_db(self,c_email):

        

        #connect to the database
        con = sql.connect(host = "localhost", user = "root", password = "0139612345", database = "login_details")
        cursor = con.cursor()
        #create a table for orders
        cursor.execute("CREATE TABLE IF NOT EXISTS orders (order_id INT AUTO_INCREMENT PRIMARY KEY, shoe_name VARCHAR(100) NOT NULL, shoe_price VARCHAR(100) NOT NULL,shoe_type VARCHAR(100) NOT NULL, shoe_image VARCHAR(100) NOT NULL, shoe_size VARCHAR(100) NOT NULL)")
        #insert the cart items into the orders table
        for item in self.cart_items:
            cursor.execute("INSERT INTO orders (shoe_name, shoe_price, shoe_type, shoe_image,shoe_size) VALUES (%s, %s, %s, %s, %s)", (item["name"], item["price"], item["type"], item["image_path"], item["size"]))
        con.commit()
        con.close()
        #generate an invoice
        self.generate_invoice(c_email)
        #clear the cart items
        self.cart_items = []
        #display a message
        mb.showinfo("Success", "Order placed successfully")
        #destroy the cart frame
        self.cart_frame.destroy()
        #display the catalog
        self.catalog()

    #function to generate an invoice
    def generate_invoice(self, user_email):
    # Create a PDF invoice
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", style="B", size=24)
        pdf.set_text_color(0, 0, 255)  # Blue color
        pdf.cell(200, 10, "Invoice", ln=True, align='C')
        pdf.set_font("Arial", size=12)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(200, 10, f"User Email: {user_email}", ln=True)
        for idx, item in enumerate(self.cart_items):
            pdf.cell(200, 10, f"Item {idx + 1}: {item['name']}, Price: {item['price']}", ln=True)
        pdf.output("invoice.pdf")

        # Email the invoice
        from_email = "bharadwajkumar99@gmail.com"
        password = "wdrftjlybbgzmjbi"
        to_email = user_email

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = "Invoice for your order"

        body = "Please find attached the invoice for your order."
        msg.attach(MIMEText(body, 'plain'))

        filename = "invoice.pdf"
        attachment = open(filename, "rb")

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()

        print("Invoice sent successfully")

        #download the invoice
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

    # Save the PDF invoice
        if file_path:
            pdf.output(file_path)
            print("Invoice saved successfully")
        else:
            print("Invoice not saved")

        #invoice saved and sent to your  your email successfully 
        #display email id of the user in the message
        mb.showinfo("Success", f"Invoice saved and sent to {user_email} successfully")
            


    

    

    
        
    #function to delete a product from the catalog
    def delete_product(self, shoe_name):
        con = sql.connect(host="localhost", user="root", password="0139612345", database="login_details")
        cursor=con.cursor()
        cursor.execute("DELETE FROM catalog WHERE shoe_name = %s", (shoe_name,))
        con.commit()
        con.close()
        mb.showinfo("Success", "Shoe deleted from catalog")
        #clear the catalog and display the updated catalog
        self.catalog()








        

if __name__ == "__main__":
    root = tk.Tk()
    app = walkwise(root)
    
    # app.l_frame()
    # app.c_frame()
    # app.f_frame()
    # app.show_login()
    root.mainloop()

