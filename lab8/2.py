import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Colors
colorRED = (255, 0, 0)
colorWHITE = (255, 255, 255)
colorGREEN = (0, 255, 0)
colorDARKGREEN = (0, 128, 0)
colorBLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling the game's frame rate
clock = pygame.time.Clock()

# Game variables
SNAKE_SIZE = 20
SNAKE_SPEED = 5
FOOD_SIZE = 20
score = 0
level = 1
snake_body = [(WIDTH // 2, HEIGHT // 2)]  # Snake's initial position
food_position = (0, 0)  # Food's initial position

# Function to generate random position for food
def generate_food_position():
    x = random.randint(0, (WIDTH - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE
    y = random.randint(0, (HEIGHT - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE
    return x, y

# Function to draw the snake
def draw_snake():
    for i, segment in enumerate(snake_body):
        color = colorDARKGREEN if i == 0 else colorGREEN  # Snake's head is dark green
        pygame.draw.rect(screen, color, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

# Function to draw the food
def draw_food():
    pygame.draw.rect(screen, colorRED, (food_position[0], food_position[1], FOOD_SIZE, FOOD_SIZE))

# Function to handle events
def handle_events():
    global snake_body, direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            elif event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"

# Function to check for border collision
def check_border_collision():
    return (snake_body[0][0] < 0 or snake_body[0][0] >= WIDTH or
            snake_body[0][1] < 0 or snake_body[0][1] >= HEIGHT)

# Function to check if snake collides with itself
def check_self_collision():
    return snake_body[0] in snake_body[1:]

# Main game loop
direction = "right"
food_position = generate_food_position()

while True:
    screen.fill(colorBLACK)  # Background is black

    handle_events()

    # Move the snake
    if direction == "up":
        new_head = (snake_body[0][0], snake_body[0][1] - SNAKE_SIZE)
    elif direction == "down":
        new_head = (snake_body[0][0], snake_body[0][1] + SNAKE_SIZE)
    elif direction == "left":
        new_head = (snake_body[0][0] - SNAKE_SIZE, snake_body[0][1])
    elif direction == "right":
        new_head = (snake_body[0][0] + SNAKE_SIZE, snake_body[0][1])

    snake_body = [new_head] + snake_body  # Add new head
    snake_body = snake_body[:score + 1]  # Trim tail if not growing

    # Check for collision with food
    if snake_body[0] == food_position:
        score += 1
        if score % 3 == 0:  # Increase level every 3 foods
            level += 1
            SNAKE_SPEED += 1  # Increase speed with level
        food_position = generate_food_position()

    # Check for collision with borders or self
    if check_border_collision() or check_self_collision():
        # Reset game variables
        score = 0
        level = 1
        snake_body = [(WIDTH // 2, HEIGHT // 2)]
        SNAKE_SPEED = 5
        direction = "right"
        food_position = generate_food_position()

    # Draw snake and food
    draw_snake()
    draw_food()

    # Display score and level
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}  Level: {level}", True, colorWHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(SNAKE_SPEED)
