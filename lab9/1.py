import pygame
import random
import sys
import time

pygame.init()

# Screen dimensions
WIDTH = 400
HEIGHT = 600

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define colors
colorRED = (255, 0, 0)
colorWHITE = (255, 255, 255)

# Load background image
BACKGROUND = pygame.image.load("./files/AnimatedStreet.png")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Event for increasing speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # Increase speed event every 1000 milliseconds (1 second)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load player image and set initial position
        self.image = pygame.image.load("./files/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 55)  # Starting position for the player

    # Move player based on keyboard input
    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.left > 0:  # Move left if within screen boundaries
            self.rect.move_ip(-5, 0)
        if pressed[pygame.K_RIGHT] and self.rect.right < WIDTH:  # Move right if within screen boundaries
            self.rect.move_ip(5, 0)

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load enemy image and set initial position
        self.image = pygame.image.load("./files/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect.width // 2, WIDTH - self.rect.width // 2), 35)  # Randomize starting position
        self.speed = 5  # Initial speed

    # Move enemy downwards
    def move(self):
        if self.rect.bottom < HEIGHT:  # Move if within screen boundaries
            self.rect.move_ip(0, self.speed)
        else:  # Reset position if enemy reaches bottom of the screen
            self.rect.center = (random.randint(self.rect.width // 2, WIDTH - self.rect.width // 2), 35)

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load coin image and set initial position
        self.image = pygame.image.load("./files/Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect.width // 2, WIDTH - self.rect.width // 2), random.randint(-HEIGHT, HEIGHT // 2))  # Randomize starting position
        self.size = random.choice(["normal", "big", "small"])  # Random size for the coin
        if self.size == "big":
            self.image = pygame.transform.scale(self.image, (self.rect.width * 2, self.rect.height * 2))  # Double size if big
        elif self.size == "small":
            self.image = pygame.transform.scale(self.image, (self.rect.width // 2, self.rect.height // 2))  # Half size if small

    # Move coin downwards
    def move(self):
        self.rect.move_ip(0, SPEED)  # Move coin down the screen
        if self.rect.top > HEIGHT:  # Reset position if coin goes off the screen
            self.reset_position()

    # Reset coin's position
    def reset_position(self):
        self.rect.center = (random.randint(self.rect.width // 2, WIDTH - self.rect.width // 2), random.randint(-HEIGHT, HEIGHT // 2))  # Randomize starting position

# Initial game settings
SPEED = 5  # Initial speed
collected_coins = 0  # Initial collected coins count
enemy_speed_increase_threshold = 5  # Number of coins to collect before increasing enemy speed
enemy_speed_increase_amount = 2  # Amount to increase enemy speed

# Sprite groups
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# Create player and enemy instances
P1 = Player()
E1 = Enemy()

# Add player and enemy instances to respective sprite groups
enemies.add(E1)
all_sprites.add(P1, E1)

done = False  # Flag to control game loop

FPS = 60  # Frames per second

# Function to add a new coin to the game
def add_coin():
    new_coin = Coin()
    coins.add(new_coin)
    all_sprites.add(new_coin)

# Add the first coin to start the game
add_coin()

# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit event
            done = True
        if event.type == INC_SPEED:  # Increase speed event
            SPEED += 1
            if collected_coins >= enemy_speed_increase_threshold:
                E1.speed += enemy_speed_increase_amount
                enemy_speed_increase_threshold += 5  # Increase the threshold for the next speed increase

    screen.blit(BACKGROUND, (0, 0))  # Draw background image

    for entity in all_sprites:  # Move and draw all sprites
        entity.move()  # Move sprite
        screen.blit(entity.image, entity.rect)  # Draw sprite

    # Collision detection with enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        screen.fill(colorRED)  # Fill screen with red color (indicating game over)
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, colorWHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))  # Display "Game Over" text
        pygame
