# 🖼️ Tkinter Image Slideshow

A simple **Python Tkinter** GUI application that displays a slideshow of images with smooth transitions ✨.  
It loads images from a specified folder, resizes them, and cycles through them at a set interval ⏳.

## 🚀 Features
- 🖼️ Display multiple images in a Tkinter window  
- 📏 Resize images to a fixed resolution (1080x1080 by default)  
- ⚡ Smooth non-blocking slideshow using `root.after()`  
- ⚙️ Easily configurable image list and slideshow interval  

## 📦 Requirements
Make sure you have Python installed along with the required dependencies:

```bash
pip install pillow
```

🛠 How It Works

    📂 Load Images – Reads image paths from a list.

    📏 Resize – Adjusts each image to the set resolution using Pillow.

    🔄 Cycle – Uses itertools.cycle to loop through images infinitely.

    🕒 Slideshow – Changes images every few seconds without freezing the UI.

🎨 Customization

    ✂ Image Size – Adjust width & height in the script

    🕑 Interval – Change delay time (in milliseconds) for switching images

    📂 Image Paths – Add or remove file paths for different images

## 📷 Example Output

When you run the script, you'll see a Tkinter window with a "Start Slideshow" ▶ button. Clicking it will start cycling through your chosen images.

## 👨‍💻 Author: Aniket Mondal

## 📜 License: MIT
