import pygame
import random
import sys
import time

# Initialize pygame
pygame.init()

# Set the dimensions of the screen
WIDTH = 400
HEIGHT = 600

# Create the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define colors
colorRED = (255, 0, 0)
colorWHITE = (255, 255, 255)

# Load background image
BACKGROUND = pygame.image.load("./files/AnimatedStreet.png")

# Initialize clock
clock = pygame.time.Clock()

# Create custom event to increase speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Define Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./files/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 55)

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect[0] > 0:
            self.rect.move_ip(-5, 0)
        if pressed[pygame.K_RIGHT] and self.rect[0] + self.rect[2] < WIDTH:
            self.rect.move_ip(5, 0)

# Define Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./files/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect[2] // 2, WIDTH - self.rect[2] // 2), 35)

    def move(self):
        if self.rect[1] + self.rect[3] < HEIGHT:
            self.rect.move_ip(0, SPEED)
        else:
            self.rect.center = (random.randint(self.rect[2] // 2, WIDTH - self.rect[2] // 2), 35)

# Define Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./files/Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect[2] // 2, WIDTH - self.rect[2] // 2), random.randint(-HEIGHT, HEIGHT // 2))

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > HEIGHT:
            self.reset_position()

    def reset_position(self):
        self.rect.center = (random.randint(self.rect[2] // 2, WIDTH - self.rect[2] // 2), random.randint(-HEIGHT, HEIGHT // 2))

# Set initial speed and collected coins
SPEED = 5
collected_coins = 0

# Create sprite groups
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# Create player and enemy instances
P1 = Player()
E1 = Enemy()

enemies.add(E1)
all_sprites.add(P1, E1)

# Set game state to not done
done = False

# Set frames per second
FPS = 60

# Variable to control coin spawning
coin_spawn_timer = 0

# Function to add a new coin to the game
def add_coin():
    new_coin = Coin()
    coins.add(new_coin)
    all_sprites.add(new_coin)

# Add the first coin to start the game
add_coin()

# Game loop
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == INC_SPEED:
            SPEED += 1

    # Render background image
    screen.blit(BACKGROUND, (0, 0))

    # Move all sprites
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    # Check collision with enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        screen.fill(colorRED)
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, colorWHITE)
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
        pygame.display.flip()
        time.sleep(1)
        pygame.quit()
        sys.exit()

    # Collision detection with coins
    collisions = pygame.sprite.spritecollide(P1, coins, True)
    if collisions:
        collected_coins += len(collisions)
        # Add a new coin
        add_coin()

    # Display collected coins count in the top right corner
    font = pygame.font.Font(None, 24)
    text = font.render(f"Coins: {collected_coins}", True, colorWHITE)
    screen.blit(text, (WIDTH - text.get_width() - 10, 10))

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)
