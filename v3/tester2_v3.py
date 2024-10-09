import pygame
import math

# Initialize Pygame
pygame.init()

# Set up some constants
BLOCK_SIZE = 100
ROTATION_SPEED = 9  # degrees per frame

class Car:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
        self.direction = (1, 0)  # initial direction
        self.rotation_angle = 0
        self.car_image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.car_image.fill((255, 0, 0))  # red color

    def turn_right(self):
        # Calculate the new direction based on the turn
        new_direction = (-self.direction[1], self.direction[0])

        # Animate the rotation of the car
        for _ in range(10):  # 10 frames to complete the turn
            # Rotate the car by a small angle
            self.rotate_car(-ROTATION_SPEED)  # ROTATION_SPEED degrees per frame

            # Update the car's image to match the new rotation
            self.car_image = pygame.transform.rotate(self.car_image, self.rotation_angle)

            # Update the game state (e.g., redraw the screen)
            screen = pygame.display.set_mode((800, 600))
            screen.fill((0, 0, 0))  # black background
            screen.blit(self.car_image, (self.rect.x, self.rect.y))
            pygame.display.flip()

            # Cap the frame rate to 60 FPS
            pygame.time.Clock().tick(60)

        # Update the car's direction
        self.direction = new_direction

    def rotate_car(self, angle):
        self.rotation_angle += angle
        self.car_image = pygame.transform.rotate(self.car_image, self.rotation_angle)

# Create a car object
car = Car(100, 100)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                car.turn_right()

    # Update the game state (e.g., redraw the screen)
    screen = pygame.display.set_mode((800, 600))
    screen.fill((0, 0, 0))  # black background
    screen.blit(car.car_image, (car.rect.x, car.rect.y))
    pygame.display.flip()

    # Cap the frame rate to 60 FPS
    pygame.time.Clock().tick(60)

pygame.quit()