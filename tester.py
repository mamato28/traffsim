import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Rect dimensions
rect_width = 30
rect_height = 90

# Initial position and rotation
x = screen_width * 0.5
y = 0
rotation_angle = 0

# Define the movement speeds
y_speed = 5
x_speed = 5
rotation_speed = 2  # Rotation speed in degrees per frame

# Main loop
running = True
moving_down = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill(white)
    
    if moving_down:
        y += y_speed
        if y >= 100:
            moving_down = False
    else:
        # Gradually increase the rotation angle to 90 degrees
        if rotation_angle < 90:
            rotation_angle += rotation_speed
        x += x_speed
        if y < screen_height * 0.5:
            y += y_speed
        if x >= screen_width - rect_width:
            x = screen_width - rect_width

    # Create a surface to draw the rectangle
    rect_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
    rect_surface.fill(black)
    
    # Rotate the surface
    rotated_surface = pygame.transform.rotate(rect_surface, rotation_angle)
    
    # Get the new rect for the rotated surface
    rotated_rect = rotated_surface.get_rect(center=(x, y))
    
    # Draw the rotated rectangle
    screen.blit(rotated_surface, rotated_rect.topleft)
    
    # Update the screen
    pygame.display.flip()
    
    # Frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
