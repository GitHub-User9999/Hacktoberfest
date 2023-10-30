import tkinter as tk
from tkinter import PhotoImage
from itertools import cycle

root = tk.Tk()
root.title("Animated Profile Card")

# Create a canvas
canvas = tk.Canvas(root, width=300, height=400)
canvas.pack()

# Load profile images
images = [PhotoImage(file=f"image{i}.gif") for i in range(1, 6)]
image_cycle = cycle(images)

# Function to update the image
def update_image():
    img = next(image_cycle)
    canvas.create_image(150, 200, image=img)
    canvas.image = img
    root.after(1000, update_image)  # Change image every 1 second

# Initial image
initial_img = next(image_cycle)
canvas.create_image(150, 200, image=initial_img)
canvas.image = initial_img

# Start the animation
root.after(1000, update_image)

root.mainloop()
