import pygame
import sys
import random

pygame.init()

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

white = (255, 255, 255)
grey = (196, 196, 196)

bg_image = pygame.image.load('pictures/bg_4_25.png')
bg_image = pygame.transform.scale(bg_image, (screen_width, screen_height))


class Car:
    def __init__(self, image_path):
        self.car_image = pygame.image.load(image_path)
        self.car_width, self.car_height = self.car_image.get_size()
        self.x = screen_width * 0.5
        self.y = 0
        self.rotation_angle = 0
        # self.y_speed = 5
        self.y_speed = random.randint(5,10)
        # self.x_speed = random.randint(5,10)
        self.x_speed = 3
        self.rotation_speed = 4.5  # Rotation speed in degrees per frame
        self.moving_down = True

    def move_down(self):
        if self.moving_down:
            self.y_speed += random.uniform(-1, 1)
            self.y_speed = max(1, min(10, self.y_speed))  # clamp the y_speed to the range [1, 10]
   
            self.y += self.y_speed

            # print('y: '+ self.y + 'y_speed: ' + self.y_speed)
            # print(f" y: {self.y} + " + f" y_speed: {self.y_speed}")

            if self.y >= screen_height * 0.5:
                self.moving_down = False

    def turn_right(self):
        # self.x_speed += random.uniform(-1, 1)
        # self.x_speed = max(1, min(10, self.x_speed))  # clamp the y_speed to the range [1, 10]
   
        if self.rotation_angle > -90:
            self.rotation_angle -= self.rotation_speed
        
        if self.x > screen_width*0.4 :
            self.x -= self.x_speed
        else :
            self.x_speed += random.uniform(-1, 1)
            self.x_speed = max(1, min(10, self.x_speed))
            self.x -= self.x_speed
            
        # print(self.x_speed)
        if self.y < screen_height * 0.5:
            self.y += self.y_speed

        


    def turn_left(self):
        if self.rotation_angle < 90:
            self.rotation_angle += self.rotation_speed
        self.x += self.x_speed
        # print(self.x_speed)
        if self.y < screen_height * 0.5:
            self.y += self.y_speed
        

    
        

    def draw(self, screen):
        # Rotate the car image
        rotated_car = pygame.transform.rotate(self.car_image, self.rotation_angle)
        # Get the new rect for the rotated car image
        rotated_rect = rotated_car.get_rect(center=(self.x, self.y))
        # Draw the rotated car image
        screen.blit(rotated_car, rotated_rect.topleft)


car = Car('pictures/car_down.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_image,(0,0))



    car.move_down()

    if not car.moving_down:
        # car.turn_left()
        car.turn_right()
    
    car.draw(screen)
    


    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()

