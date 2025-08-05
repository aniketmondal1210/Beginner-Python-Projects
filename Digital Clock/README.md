# 🕒 Digital Clock (Tkinter)

This is a simple **Digital Clock** GUI application built using **Python's Tkinter** library. It displays the current time (with AM/PM) and the date, updating every second.

## 📸 Screenshot

![Digital Clock Example](https://via.placeholder.com/600x200.png?text=Digital+Clock+GUI)

## 🛠️ Features

- Displays current time in **HH:MM:SS AM/PM** format
- Shows the current date below the time
- Updates every second
- Built with a clean and minimal **Tkinter GUI**

## 📋 Requirements

- Python 3.x

> No external libraries required — uses only Python's built-in `tkinter` and `time` modules.

## 🚀 How to Run

1. Clone this repository or copy the script.
2. Save it as `digital_clock.py`.
3. Run the script using:

```bash
python digital_clock.py
```

## 🧾 Code Overview

```python
import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(root, font=('calibri', 50, 'bold'), background='white', foreground='black')
label.pack(anchor='center')

time()
root.mainloop()
```

## 📦 License

This project is licensed under the MIT License.

## 👤 Author

- [Your Name](https://github.com/yourusername)
