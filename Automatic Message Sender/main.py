import pyautogui
import time

message = 3
while (message > 0):
    time.sleep(4)  # Wait for 4 seconds before typing
    pyautogui.typewrite("It's magic, It's magic!") # It's magic, It's magic! - change your message accordingly
    time.sleep(2)  # Wait for 2 seconds before pressing enter
    pyautogui.press('enter')
    message -= 1
