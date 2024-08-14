import pygame
import random
import threading
import time

# Initialize Pygame
pygame.init()

# Global variables
exit_threads = False
current_light = 'green'
canvas_width = 800
randomspeedlow = 5
randomspeedhigh = 10

# Define rectangles and speeds
rects = [
    {"rect": pygame.Rect(800, 50, 100, 50), "speed": random.randint(randomspeedlow, randomspeedhigh)},
    {"rect": pygame.Rect(800, 150, 100, 50), "speed": random.randint(randomspeedlow, randomspeedhigh)},
    {"rect": pygame.Rect(800, 250, 100, 50), "speed": random.randint(randomspeedlow, randomspeedhigh)}
]

def move_rect(index):
    global exit_threads
    while not exit_threads:
        rect = rects[index]["rect"]
        speed = rects[index]["speed"]
        if current_light != 'red' or rect.x < canvas_width * 0.585 or rect.x > canvas_width * 0.6:
            rect.x -= speed
            if rect.x < -300:
                randomappear = random.randint(1, 10)
                randomwaittime = random.randint(1, 5)
                time.sleep(randomwaittime)
                if randomappear > 5:
                    rect.x = canvas_width
            for other_rect in rects:
                if other_rect["rect"] != rect:
                    distance = abs(rect.x - other_rect["rect"].x)
                    if distance <= 95:
                        rects[index]["speed"] = 0
                    elif distance > 100:
                        rects[index]["speed"] = random.randint(randomspeedlow, randomspeedhigh)
        else:
            rects[index]["speed"] = 0
        pygame.time.delay(1000 // 10)  # 10 FPS

# Create and start threads for each rectangle
threads = []
for i in range(len(rects)):
    thread = threading.Thread(target=move_rect, args=(i,))
    threads.append(thread)
    thread.start()

# Ensure that threads are joined before exiting
for thread in threads:
    thread.join()

# Quit Pygame
pygame.quit()
