import datetime
import time
import pygame
import tkinter as tk
from threading import Thread

def set_alarm(alarm_time):
    while True:
        if datetime.datetime.now().strftime("%H:%M") == alarm_time:  # 24 Hours format
            print("Wake Up! Nowwww!")
            pygame.mixer.init()
            pygame.mixer.music.load("alarm.mp3")
            pygame.mixer.music.play()
            time.sleep(60)
            break
        time.sleep(30)

def start_alarm():
    alarm_time = alarm_entry.get()  # Get the alarm time from the entry field
    print("Yayy! Your alarm is set!")
    alarm_thread = Thread(target=set_alarm, args=(alarm_time,))
    alarm_thread.start()

def update_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")  # Display with seconds
    time_label.config(text=f"Current Time: {current_time}")
    root.after(1000, update_time)

# Create GUI
root = tk.Tk()
root.title("Alarm Clock")

# Display current time
time_label = tk.Label(root, text="", font=("Helvetica", 24), fg="blue")
time_label.pack(pady=20)

# Alarm time input
alarm_label = tk.Label(root, text="Set Alarm Time (HH:MM):", font=("Helvetica", 16))
alarm_label.pack(pady=5)
alarm_entry = tk.Entry(root, font=("Helvetica", 16), justify="center")
alarm_entry.pack(pady=5)

# Set alarm button
set_alarm_button = tk.Button(root, text="Set Alarm", font=("Helvetica", 16), command=start_alarm)
set_alarm_button.pack(pady=20)

# Update live time
update_time()

# Run the GUI event loop
root.mainloop()
