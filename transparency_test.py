import tkinter as tk

root = tk.Tk()
root.title("Transparent Frame")

# Not all systems support transparent windows with Tkinter
try:
    # Set the transparency level (0.0 to 1.0)
    root.attributes('-alpha', 0.5)
except tk.TclError:
    print("Transparency not supported on this system.")

frame = tk.Frame(root, width=300, height=200, bg="blue")
frame.pack(padx=10, pady=10)

root.mainloop()
