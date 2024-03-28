import pygame

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Set up the screen
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Moving Ball")

# Set up the ball
ball_color = (255, 0, 0)
ball_radius = 25
ball_position = [400, 400]

# Draw the ball on the screen
def draw_ball():
    pygame.draw.circle(screen, ball_color, ball_position, ball_radius)

# Move the ball in response to keyboard input
def handle_keys():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_position[1] -= 20
        if ball_position[1] < ball_radius:
            ball_position[1] = ball_radius
    if keys[pygame.K_DOWN]:
        ball_position[1] += 20
        if ball_position[1] > 800 - ball_radius:
            ball_position[1] = 800 - ball_radius
    if keys[pygame.K_LEFT]:
        ball_position[0] -= 20
        if ball_position[0] < ball_radius:
            ball_position[0] = ball_radius
    if keys[pygame.K_RIGHT]:
        ball_position[0] += 20
        if ball_position[0] > 800 - ball_radius:
            ball_position[0] = 800 - ball_radius

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle keyboard input
    handle_keys()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the ball
    draw_ball()

    # Update the screen
    pygame.display.flip()
    clock.tick(24)

# Quit Pygame
pygame.quit()
