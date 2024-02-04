import tkinter as tk

def login():
    # Implement your login logic here
    print("Login button clicked")

window = tk.Tk()
window.title("Login page")
window.geometry("400x200")

label = tk.Label(window, text="Provide your login details")
label.pack()

frame = tk.Frame(window)
frame.pack()

username_label = tk.Label(frame, text="Username")
username_entry = tk.Entry(frame)
password_label = tk.Label(frame, text="Password")
password_entry = tk.Entry(frame, show="*")  # Use show="*" to hide password
login_button = tk.Button(frame, text="Login", command=login)

username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
login_button.grid(row=2, column=0, columnspan=2)

window.mainloop()
