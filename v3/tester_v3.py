import pygame
import random
import time
import math

# Initialize Pygame
pygame.init()

# Define constants for grid dimensions
GRID_WIDTH = 14
GRID_HEIGHT = 12
BLOCK_SIZE = 100
SCREEN_WIDTH = GRID_WIDTH * BLOCK_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * BLOCK_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (195, 195, 195)
BROWN = (155, 103, 60)
FONT_COLOR = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Grid System")

# Load font
pygame.font.init()
font = pygame.font.SysFont(None, 40)

class World_Grid:
    def __init__(self, screen):
        self.screen = screen
        self.images = {}  # Dictionary to store images and their coordinates
        self.intersections = {}  # Dictionary to store intersection blocks and their movement options

    def add_image(self, image, coord):
        """Add an image to a specific grid block (1-indexed coordinates)."""
        self.images[coord] = image

    def add_intersection(self, coord, directions):
        """Define an intersection block and its possible movement directions."""
        self.intersections[coord] = directions

    def check_intersection(self, coord):
        """Check if the current block is an intersection and return possible directions."""
        if coord in self.intersections:
            return self.intersections[coord]
        return None

    def draw_grid(self):
        """Draw a grid with blocks of 100x100 pixels and display images."""
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                # Draw a filled rectangle (no outline)
                rect = pygame.Rect(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)

                # Check if there is an image at this grid coordinate (1-indexed)
                if (col + 1, row + 1) in self.images:
                    image = self.images[(col + 1, row + 1)]
                    self.screen.blit(image, (col * BLOCK_SIZE, row * BLOCK_SIZE))

                # Label the block with coordinates (1-indexed)
                coord_text = f"{col+1},{row+1}"
                text_surf = font.render(coord_text, True, FONT_COLOR)

                # Position the text at the center of each block
                text_rect = text_surf.get_rect(center=(col * BLOCK_SIZE + BLOCK_SIZE // 2,
                                                       row * BLOCK_SIZE + BLOCK_SIZE // 2))
                self.screen.blit(text_surf, text_rect)  # Draw the text



class Car:
    def __init__(self, x, y, speed, direction):
        
        if direction == (-1, 0):  # Moving left
            self.car_image = pygame.image.load('v2/pictures_v2/car_left.png')
            # self.car_image = pygame.transform.scale(self.car_image, (45, 18))
        elif direction == (1, 0):  # Moving right
            self.car_image = pygame.image.load('v2/pictures_v2/car_right.png')
        elif direction == (0, -1):  # Moving up
            self.car_image = pygame.image.load('v2/pictures_v2/car_up.png')
        elif direction == (0, 1):  # Moving down
            self.car_image = pygame.image.load('v2/pictures_v2/car_down.png')


        self.original_image = self.car_image  # Store the original image
        self.rect = pygame.Rect(x, y, 90, 36)  # The car's rectangle
        self.speed = speed
        self.direction = direction  # Direction as a vector, e.g., (-1, 0) for left
        self.has_turned = False
        self.rotation_angle = 0
        self.rotation_speed = 0

    def move_forward(self):     #Move the car forward in its current direction
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed

    def turn_left(self):        # Turn the car 90 degrees to the left based on the current direction
        if self.direction == (1, 0):  # Moving right
            self.rotate_car(90)  # Turn counterclockwise to move up
        elif self.direction == (-1, 0):  # Moving left
            self.rotate_car(90)  # Turn clockwise to move down
        elif self.direction == (0, -1):  # Moving up
            self.rotate_car(90)  # Turn counterclockwise to move left
        elif self.direction == (0, 1):  # Moving down
            self.rotate_car(90)  # Turn clockwise to move right

        # Update the direction based on the turn
        self.direction = (self.direction[1], -self.direction[0])


    def turn_right(self):       # Turn the car 90 degrees to the right based on the current direction."""
        
        if self.direction == (1, 0):  # Moving right
            self.rotate_car(-90)  # Turn clockwise to move down
        elif self.direction == (-1, 0):  # Moving left
            self.rotate_car(270)  # Turn counterclockwise to move up
        elif self.direction == (0, -1):  # Moving up
            self.rotate_car(-90)  # Turn clockwise to move right
        elif self.direction == (0, 1):  # Moving down
            self.rotate_car(270)  # Turn counterclockwise to move left

        # Update the direction based on the turn
        self.direction = (-self.direction[1], self.direction[0])

    def rotate_car(self, angle):        # Rotate the car by the specified angle
        
        self.rotation_speed = angle / 10
        for _ in range(27):
            print("hello")
            self.rect.x += 10
            self.rotation_angle += self.rotation_speed
        self.car_image = pygame.transform.rotate(self.car_image, self.rotation_angle)

    def update(self):
        # Get the current block the car is in
        current_block = self.get_current_block()  # Assuming you have a method to get the current block
        intersection_block = (4, 4)  # Define your intersection block here
        
        # Check if the car has passed the adjacent block and is at the intersection
        self.check_passed_adjacent_blocks(current_block, intersection_block)
    
    # def handle_intersection(self, world_grid):
    #     """Handle turning when the vehicle has passed an intersection."""
    #     # Calculate the grid coordinates (1-indexed)
    #     grid_x = self.rect.x // BLOCK_SIZE + 1
    #     grid_y = self.rect.y // BLOCK_SIZE + 1
    #     current_block = (grid_x, grid_y)

    #     # We want to trigger turning after leaving block (5,4)
    #     if current_block == (4, 4) and not self.has_turned:
    #     # if current_block == (5, 4) or (grid_x == 5 and grid_y == 3):
    #     # if (grid_x, grid_y) == (5, 4) and self.direction == (-1, 0):  # Check if car is leaving block (5,4) from the right
    
    #         if not self.has_turned:
    #             # Check if the vehicle has fully passed the block based on direction
    #             if self._has_passed_block():
    #                 possible_directions = world_grid.check_intersection(current_block)
                    
    #                 if "right" in possible_directions:
    #                     self.turn_right()  # Perform the turn
    #                     self.has_turned = True  # Mark that the car has turned

    def check_passed_adjacent_blocks(self, current_block, intersection_block):
        """
        Check if the vehicle has passed the adjacent block based on its direction and touches the intersection block.
        """
        # Current block values
        block_x_start = current_block[0] * BLOCK_SIZE
        block_x_end = block_x_start + BLOCK_SIZE
        
        # Intersection block values (in your case, it's (4,4))
        intersection_x_start = intersection_block[0] * BLOCK_SIZE
        intersection_x_end = intersection_x_start + BLOCK_SIZE

        # Moving left, check if we passed (5,4) and reach the intersection (4,4)
        if self.direction == (-1, 0):  # Moving left
            # Check if the car has passed the adjacent block (5,4)
            if current_block == (5, 4) and not self.has_turned:
                if self.rect.right < block_x_start:  # Passed block (5,4)
                    print("Vehicle has passed block (5,4) moving left.")
                    self.has_turned = True

            # Now check if the car is in the intersection block (4,4)
            # if current_block == (4, 4) and self.has_turned:
            if self.rect.x < intersection_x_end + 50  and self.has_turned:
                print("Vehicle is in intersection block (4,4), triggering turn.")
                self.turn_right()  # Trigger the turn here
                # return True
        
        # Handle other directions similarly if needed


    def _has_passed_block(self):
        """Return True if the vehicle has passed beyond block (5,4) based on its direction."""
        # Define the boundaries for block (5,4)
        
        block_x_start = (5 - 1) * BLOCK_SIZE  # 400
        block_x_end = block_x_start + BLOCK_SIZE  # 500
        block_y_start = (4 - 1) * BLOCK_SIZE  # 300
        block_y_end = block_y_start + BLOCK_SIZE  # 400

        # print(f"Block (5,4) x-start: {block_x_start}, x-end: {block_x_end}")

        # Check if the vehicle has fully exited the block based on its direction
        if self.direction == (-1, 0):  # Moving left
            print(f"Vehicle position: ({self.rect.x}, {self.rect.y}), right: {self.rect.right}, block_x_start: {block_x_start}")
            # if self.rect.x < block_x_end:
            if self.rect.x < block_x_start:
                # print("Vehicle has passed block (5, 4) moving left.")
                return True
            else:
                print("Vehicle not passed.")
                return False
            
        elif self.direction == (1, 0):  # Moving right
            print(f"Vehicle position: ({self.rect.x}, {self.rect.y}), left: {self.rect.left}, block_x_end: {block_x_end}")
            if self.rect.left > block_x_end:
                print("Vehicle has passed block (5, 4) moving right.")
                return True

        elif self.direction == (0, -1):  # Moving up
            print(f"Vehicle position: ({self.rect.x}, {self.rect.y}), bottom: {self.rect.bottom}, block_y_start: {block_y_start}")
            if self.rect.bottom < block_y_start:
                print("Vehicle has passed block (5, 4) moving up.")
                return True

        elif self.direction == (0, 1):  # Moving down
            print(f"Vehicle position: ({self.rect.x}, {self.rect.y}), top: {self.rect.top}, block_y_end: {block_y_end}")
            if self.rect.top > block_y_end:
                print("Vehicle has passed block (5, 4) moving down.")
                return True

        return False



    def draw(self, screen):
        """Draw the rotated car image at its current position."""
        # Get the rotated car image and re-align its position
        rotated_car = self.car_image
        rotated_rect = rotated_car.get_rect(center=self.rect.center)

        
        # Draw the rectangle
        pygame.draw.rect(screen, (0, 0, 0), rotated_rect, 2)  # Red rectangle

        # Draw the rotated car image
        screen.blit(rotated_car, rotated_rect.topleft)

    
    

def load_and_add_images(world_grid):
    """Separate function to load and add multiple images to the grid."""
    picA = pygame.image.load("v3/pictures_v3/road_stop_200.png")
    picA = pygame.transform.scale(picA, (BLOCK_SIZE, BLOCK_SIZE))
    picA_rotated_90 = pygame.transform.rotate(picA, 90)
    picA_rotated_180 = pygame.transform.rotate(picA, 180)
    
    # picB = normal road
    picB = pygame.image.load("v3/pictures_v3/road_normal_200.png")
    picB = pygame.transform.scale(picB, (BLOCK_SIZE, BLOCK_SIZE))

    # picC = grass
    picC = pygame.image.load("v3/pictures_v3/grass_200.png")
    picC = pygame.transform.scale(picC, (BLOCK_SIZE, BLOCK_SIZE))

    # Add images to the grid
    world_grid.add_image(picA, (5, 4)) 
    world_grid.add_image(picA_rotated_180, (3, 5))  
    world_grid.add_image(picA_rotated_90, (4, 3))  
     
    
    coords_normal_road = [
        (4, 1), 
        (4, 2), 
        (1, 4), (2, 4), (3, 4), (4, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4), (12, 4), (13, 4), (14, 4),
        (1, 5), (2, 5), (4, 5), (5, 5), (6, 5), (7, 5),
    ]
    fill_blocks_with_image(world_grid, picB, coords_normal_road)

    coords_grass = [(6, 1), (7, 1), (7, 2), (7, 3), (8, 3), (9, 3), (10, 3)]
    fill_blocks_with_image(world_grid, picC, coords_grass)

    # Define an intersection at (5, 4) with a right turn
    world_grid.add_intersection((4, 4), ["right"])  # Car can turn right at (5, 4)



def fill_blocks_with_image(world_grid, image, coords):
    """Fill multiple blocks with the same image."""
    for coord in coords:
        world_grid.add_image(image, coord)


# Main loop
def main():
    clock = pygame.time.Clock()
    world_grid = World_Grid(screen)

    # Load and add images to the grid
    load_and_add_images(world_grid)

    # Create a car initially moving from right to left
    car = Car(SCREEN_WIDTH - 100, 350, 5, (-1, 0))

    # left to right
    # car = Car(100, 350, 5, (1, 0))

    # up to down
    # car = Car(450, 100, 5, (0, 1))


    # down to up
    # car = Car(450, SCREEN_HEIGHT - 100, 5, (0, -1))



    running = True

    while running:
        screen.fill(BROWN)
        world_grid.draw_grid()

        # Move the car forward and handle intersections
        car.move_forward()
        # car.handle_intersection(world_grid)
        car.check_passed_adjacent_blocks((5,4), (4,4) )
        car.draw(screen)

        # Draw the car
        # pygame.draw.rect(screen, BLACK, car.rect)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
