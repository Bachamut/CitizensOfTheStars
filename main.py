import pygame
import random

# Initialize of pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("CitizensOfTheStars")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Background
background = pygame.image.load("background.png")

speed_m = 3

# Player
playerImg = pygame.image.load("spaceship.png")

playerX = 368
playerY = 510
playerX_vector = 0
playerY_vector = 0

# Enemy
enemyImg = pygame.image.load("ufo.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_vector = speed_m * 0.06
enemyY_vector = speed_m * 0.002

# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = playerY
bulletX_vector = speed_m * 0
bulletY_vector = speed_m * 0.15
bullet_state = "ready"

decoupled = True
active = False


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 24, y - 16))


# Game Loop
running = True

while running:
    # Screen background color (RBG)
    screen.fill((50, 80, 000))

    # Background image
    screen.blit(background, (- playerX / 40 - 368, - playerY / 40 - 100))

    # Checking pressed keys
    keys = pygame.key.get_pressed()

    # Player ship movement
    if keys[pygame.K_LEFT]:
        playerX_vector += speed_m * -0.0002
    if keys[pygame.K_RIGHT]:
        playerX_vector += speed_m * 0.0002
    if keys[pygame.K_UP]:
        playerY_vector += speed_m * -0.0002
    if keys[pygame.K_DOWN]:
        playerY_vector += speed_m * 0.0002

    # Stop mechanics
    if decoupled == active:
        if keys[pygame.K_LEFT] == False and playerX_vector <= 0:
            playerX_vector += speed_m * 0.00015
        if keys[pygame.K_RIGHT] == False and playerX_vector >= 0:
            playerX_vector -= speed_m * 0.00015
        if keys[pygame.K_UP] == False and playerY_vector <= 0:
            playerY_vector += speed_m * 0.00015
        if keys[pygame.K_DOWN] == False and playerY_vector >= 0:
            playerY_vector -= speed_m * 0.00015

    for event in pygame.event.get():
        # loop exit
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # fire_bullet mechanics
            if event.key == pygame.K_w:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
            # changing decouple status for stop mechanics
            if event.key == pygame.K_SPACE:
                active = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                active = False

    # Boundary of X axis movement for player
    if playerX < 0:
        playerX = 0
        playerX_vector = 0
    elif playerX > 736:
        playerX = 736
        playerX_vector = 0
    # Boundary of Y axis movement for player
    if playerY < 0:
        playerY = 0
        playerY_vector = 0
    elif playerY > 536:
        playerY = 536
        playerY_vector = 0

    # Boundary of X axis movement for enemy
    if enemyX < 0:
        enemyX = 0
        enemyX_vector = - enemyX_vector
    elif enemyX > 736:
        enemyX = 736
        enemyX_vector = - enemyX_vector
    # Boundary of Y axis movement for enemy
    if enemyY < 0:
        enemyY = 0
        enemyY_vector = 0
    elif enemyY > 536:
        enemyY = 536
        enemyY_vector = 0

    # Player position update
    playerX += playerX_vector
    playerY += playerY_vector
    player(playerX, playerY)

    # Enemy position update
    enemyX += enemyX_vector
    enemyY += enemyY_vector
    enemy(enemyX, enemyY)

    # Bullet movement
    if bulletY <= -16:
        bulletY = playerY
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_vector

    pygame.display.update()
