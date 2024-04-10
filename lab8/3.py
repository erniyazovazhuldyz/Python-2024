import pygame

# Initialize pygame
pygame.init()

# Set up the screen dimensions
WIDTH = 800
HEIGHT = 600

# Create the screen surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Create a base layer to draw shapes on
base_layer = pygame.Surface((WIDTH, HEIGHT))

# Define colors
colorRed = (255, 0, 0)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Variable to track if left mouse button is pressed
LMBpressed = False
# Default thickness of the drawing tool
Thickness = 5
# Default shape to draw
shape = 'rectangle'

# Coordinates of previous and current mouse positions
prevX = 0
prevY = 0
currX = 0
currY = 0

# Function to calculate rectangle dimensions
def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

# Function to draw different shapes based on the selected shape
def draw_shape(start_pos, end_pos):
    if shape == 'rectangle':
        pygame.draw.rect(screen, colorRed, calculate_rect(start_pos[0], start_pos[1], end_pos[0], end_pos[1]), Thickness)
    elif shape == 'circle':
        radius = max(abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1])) // 2
        center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
        pygame.draw.circle(screen, colorRed, center, radius, Thickness)
    elif shape == 'eraser':
        pygame.draw.circle(screen, colorWHITE, end_pos, Thickness)

# Main game loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Left mouse button pressed
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]
                # Clear base layer and draw shape
                base_layer.fill(colorWHITE)
                draw_shape((prevX, prevY), (currX, currY))
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # Left mouse button released
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            # Draw final shape on screen and update base layer
            draw_shape((prevX, prevY), (currX, currY))
            base_layer.blit(screen, (0, 0))
        if event.type == pygame.KEYDOWN:
            # Key pressed
            if event.key == pygame.K_EQUALS:
                # Increase thickness
                Thickness += 1
            elif event.key == pygame.K_MINUS:
                # Decrease thickness
                Thickness -= 1
            elif event.key == pygame.K_r:
                # Draw rectangle
                shape = 'rectangle'
            elif event.key == pygame.K_c:
                # Draw circle
                shape = 'circle'
            elif event.key == pygame.K_e:
                # Eraser
                shape = 'eraser'
            elif event.key == pygame.K_1:
                # Red color
                colorRed = (255, 0, 0)
            elif event.key == pygame.K_2:
                # Green color
                colorRed = (0, 255, 0)
            elif event.key == pygame.K_3:
                # Blue color
                colorRed = (0, 0, 255)
            elif event.key == pygame.K_4:
                # White color
                colorRed = (255, 0, 255)

    # Update the screen
    screen.blit(base_layer, (0, 0))
    pygame.display.flip()
    clock.tick(60)

# Quit pygame
pygame.quit()
