import pygame
import random
import sys

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
score = 0
level = 1
snake_body = [(WIDTH // 2, HEIGHT // 2)]  # Snake's initial position
food_position = (0, 0)  # Food's initial position

# Timer variables
food_timer = 10000  # Food timer in milliseconds (10 seconds)
last_food_time = pygame.time.get_ticks()

# Function to generate random position for food
def generate_food_position():
    x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
    y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
    return x, y

# Function to generate random food type
def generate_food_type():
    return random.choice(["tiny", "normal", "large"])

# Function to draw the snake
def draw_snake():
    for i, segment in enumerate(snake_body):
        color = colorDARKGREEN if i == 0 else colorGREEN  # Snake's head is dark green
        pygame.draw.rect(screen, color, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

# Function to draw the food
def draw_food(food_position, food_type):
    if food_type == "tiny":
        food_size = 10
    elif food_type == "large":
        food_size = 30
    else:
        food_size = 20
    pygame.draw.rect(screen, colorRED, (food_position[0], food_position[1], food_size, food_size))

# Function to draw the timer
def draw_timer(time_left):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Time left: {time_left} seconds", True, colorWHITE)
    screen.blit(text, (WIDTH - text.get_width() - 10, 10))

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

# Function to update food
def update_food():
    global food_position, last_food_time, food_timer
    current_time = pygame.time.get_ticks()
    if current_time - last_food_time >= food_timer:
        food_position = generate_food_position()
        last_food_time = current_time
        food_timer = 10000  # Reset food timer
    else:
        time_left = int((food_timer - (current_time - last_food_time)) / 1000) + 1
        draw_timer(time_left)

# Main game loop
direction = "right"
food_position = generate_food_position()
food_type = generate_food_type()

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
        food_type = generate_food_type()
        last_food_time = pygame.time.get_ticks()  # Reset food timer
        food_timer = 10000  # Reset food timer

    # Check for collision with borders or self
    if check_border_collision() or check_self_collision():
        # Reset game variables
        score = 0
        level = 1
        snake_body = [(WIDTH // 2, HEIGHT // 2)]
        SNAKE_SPEED = 5
        direction = "right"
        food_position = generate_food_position()
        food_type = generate_food_type()
        last_food_time = pygame.time.get_ticks()  # Reset food timer
        food_timer = 10000  # Reset food timer

    # Draw snake and food
    draw_snake()
    draw_food(food_position, food_type)
    update_food()

    # Display score and level
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}  Level: {level}", True, colorWHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(SNAKE_SPEED)
