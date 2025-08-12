from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow")

# List of image file paths
image_files = [
    r"X:\pqr\abc\mno\xyz\def\image1.jpg",
    r"X:\pqr\abc\mno\xyz\def\image2.jpg",
    r"X:\pqr\abc\mno\xyz\def\image3.jpg",
    r"X:\pqr\abc\mno\xyz\def\image4.jpg",
    r"X:\pqr\abc\mno\xyz\def\image5.jpg"
]

# Resize images
image_size = (1080, 1080)
images = [
    Image.open(image_file).resize(image_size, Image.Resampling.LANCZOS)
    for image_file in image_files
]
photo_images = cycle(ImageTk.PhotoImage(image) for image in images)

label = tk.Label(root)
label.pack()

def update_image():
    label.config(image=next(photo_images))
    root.after(3000, update_image)  # Change every 3 seconds

def start_slideshow():
    update_image()

play_button = tk.Button(root, text="Start Slideshow", command=start_slideshow)
play_button.pack()

root.mainloop()
