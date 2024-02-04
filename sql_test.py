import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector

class sample:
    def __init__(self,root):
        self.root=root
        self.root.title("testing")
        self.root.geometry("1540x800")

root=Tk()
ob=sample(root)
root.mainloop()