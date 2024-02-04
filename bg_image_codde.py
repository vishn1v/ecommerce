'''original_image = Image.open("/Users/bhardwaj/Documents/pictures for project/force-majeure-du8AbwM5z2g-unsplash.jpg")  
    #ackground_photo = ImageTk.PhotoImage(background_image)

    #background_label = tk.Label(login_frame, image=background_photo)
    #background_label.photo= background_photo
    #background_label.place(x=0,y=0, relwidth=1, relheight=1)
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    # Resize the image to match the window dimensions
    resized_image = original_image.resize((1540,800), Image.LANCZOS)

    # Convert the resized image to PhotoImage
    background_photo = ImageTk.PhotoImage(original_image)

    # Create a label with the resized image
    background_label = tk.Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0) '''



original_image = Image.open("/Users/bhardwaj/Documents/pictures for project/force-majeure-du8AbwM5z2g-unsplash.jpg")

    # Get the dimensions of the Tkinter window
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    # Resize the image to match the window dimensions using LANCZOS filter
   #resized_image = original_image.resize((600, 400), Image.LANCZOS)

    # Convert the resized image to PhotoImage
    background_photo = ImageTk.PhotoImage(original_image)

    # Create a Canvas widget to display the image
    canvas = tk.Canvas(login_frame, width=window_width, height=window_height)
    canvas.grid(row=0, column=0, sticky="nsew")

    # Display the image on the Canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)

'''def on_resize(event):
    # Update the background image when the window is resized
    show_login()'''

'''img = ImageTk.PhotoImage(Image.open("/Users/bhardwaj/Documents/pictures for project/force-majeure-du8AbwM5z2g-unsplash.jpg"))
tk.Label(root, image=img).place(x=0, y=0)'''

'''root.bind("<Configure>", on_resize)'''
