import pygame
import sys


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


white = (255, 255, 255)

#========== left turn
car_image = pygame.image.load('pictures/car_down.png')
car_width, car_height = car_image.get_size()


#========== right turn
# car_image = pygame.image.load('small_car_up_to_down_wheel_right.png')
# car_width, car_height = car_image.get_size()


x = screen_width * 0.5
y = 0
rotation_angle = 0


y_speed = 5
x_speed = 5
rotation_speed = 2  # Rotation speed in degrees per frame


running = True
moving_down = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    screen.fill(white)
    
    if moving_down:
        y += y_speed
        if y >= 100:
            moving_down = False
    else:
        
        #========== left turn
        if rotation_angle < 90:
            rotation_angle += rotation_speed
        x += x_speed
        if y < screen_height * 0.5:
            y += y_speed
        if x >= screen_width - car_width:
            x = screen_width - car_width


        #========== right turn
        # if rotation_angle > -90:
        #     rotation_angle -= rotation_speed
        # x -= x_speed
        # if y < screen_height * 0.5:
        #     y += y_speed
        # if x >= screen_width - car_width:
        #     x = screen_width - car_width







    # Rotate the car image
    rotated_car = pygame.transform.rotate(car_image, rotation_angle)
    
    # Get the new rect for the rotated car image
    rotated_rect = rotated_car.get_rect(center=(x, y))
    
    # Draw the rotated car image
    screen.blit(rotated_car, rotated_rect.topleft)
    
    # Update the screen
    pygame.display.flip()
    
    # Frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
