import tkinter as tk
from PIL import Image, ImageTk

def print_coordinates(event):
    x, y = event.x, event.y
    coordinates_label.config(text=f"Coordinates: x={x}, y={y}")

root = tk.Tk()
root.attributes('-fullscreen', True)  # Maximize the window

# Load the image with Pillow
image = Image.open("atten_img.jpg")
# Resize the image to fit the window
image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
background_image = ImageTk.PhotoImage(image)

# Create a canvas
canvas = tk.Canvas(root, bg="white", width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack(expand=True, fill="both")  # Expand canvas to fill the available space

# Set the background image
canvas.create_image(0, 0, anchor="nw", image=background_image)

# Bind a mouse click event to the canvas
canvas.bind("<Button-1>", print_coordinates)

# Label to display coordinates
coordinates_label = tk.Label(root, text="Coordinates: ", font=("Helvetica", 12))
coordinates_label.pack(side="bottom", pady=10)

root.mainloop()
