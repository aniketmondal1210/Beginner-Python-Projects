import pygame
from time import sleep
import sys
import os

# Initialize pygame
pygame.init()

# Set up fullscreen window
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Scary Display")

# Initialize mixer
pygame.mixer.init()

# Helper to safely load files
def safe_load(path, loader, desc):
    if not os.path.exists(path):
        print(f"Error: {desc} file '{path}' not found.")
        pygame.quit()
        sys.exit(1)
    return loader(path)

# Play first music
safe_load("ratsasan.mp3", pygame.mixer.music.load, "Music")
pygame.mixer.music.play()
sleep(5)

# Play second music
safe_load("scary.mp3", pygame.mixer.music.load, "Music")
pygame.mixer.music.play()
sleep(1)

# Load and display image (scaled to fullscreen)
image = safe_load("scr.jpg", pygame.image.load, "Image")
window_width, window_height = window.get_size()
image = pygame.transform.scale(image, (window_width, window_height))
window.blit(image, (0, 0))
pygame.display.update()

# Event loop: display image for 3 seconds or until ESC/window close
start_ticks = pygame.time.get_ticks()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
    # Exit after 3 seconds
    if (pygame.time.get_ticks() - start_ticks) > 3000:
        pygame.quit()
        sys.exit()