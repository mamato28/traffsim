import pygame
import random
import time

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
        self.rotation_angle += angle
        self.car_image = pygame.transform.rotate(self.car_image, self.rotation_angle)


    def handle_intersection(self, world_grid):      # Handle turning when the car reaches an intersection
        grid_x = self.rect.x // BLOCK_SIZE + 1
        grid_y = self.rect.y // BLOCK_SIZE + 1
        current_block = (grid_x, grid_y)

        if current_block == (5, 4) and not self.has_turned:
            possible_directions = world_grid.check_intersection(current_block)
            
            if "right" in possible_directions:
                # self.turn_left()
                self.turn_right()  # Turn the car right (upward movement)
                self.has_turned = True  # Ensure the car only turns once at this intersection

    def draw(self, screen):
        """Draw the rotated car image at its current position."""
        # Get the rotated car image and re-align its position
        rotated_car = self.car_image
        rotated_rect = rotated_car.get_rect(center=self.rect.center)

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
    world_grid.add_intersection((5, 4), ["right"])  # Car can turn right at (5, 4)



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
        car.handle_intersection(world_grid)
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
