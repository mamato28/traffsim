import pygame
import threading
import sys
import random

# Initialize Pygame
pygame.init()


# Set up some constants
WIDTH, HEIGHT = 1200, 600
RECT_WIDTH, RECT_HEIGHT = 90, 36
SPEED = 2

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the rectangle
rect_x, rect_y = WIDTH, HEIGHT // 2

randomcolorR = random.randint(0,255)
randomcolorG = random.randint(0,255)
randomcolorB = random.randint(0,255)

rect_color = (randomcolorR, randomcolorG, randomcolorB)

# Flag to control the thread
running = True

# Function to move the rectangle
def move_rect():
    global rect_x, running
    
    # while running or count < 3:
    #     rect_x -= SPEED
    #     if rect_x < -RECT_WIDTH:
    #         running = False  # Set the flag to False when the rectangle goes beyond the left boundary
            
    #     pygame.time.delay(16)  # 16ms = 60fps
        


thread = threading.Thread(target=move_rect)
thread.daemon = True  # So the thread dies when the main program dies
thread.start()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT))
    pygame.display.flip()