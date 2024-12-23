import datetime #Library already present
import time #Library already present
import pygame

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

alarm_time = input("Enter alarm time (HH:MM): ")  # 24 Hours format
print("Yayy! Your alarm is set!")
set_alarm(alarm_time)
