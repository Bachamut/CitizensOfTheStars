import pygame

import random

from settings import Settings

import game_functions as gf

FPS = 60
fpsClock = pygame.time.Clock()

# Initialize of pygame
pygame.init()

settings = Settings()

# Create a screen
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

# Title and icon
pygame.display.set_caption("CitizensOfTheStars")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Background
background = pygame.image.load("background.png")

speed_m = 3

# Player
playerImg = pygame.image.load("spaceship.png")

playerX = settings.screen_height * 0.61
playerY = settings.screen_width * 0.64
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

    gf.check_events()

    # Boundary of X axis movement for player
    if playerX < 0:
        playerX = 0
        playerX_vector = 0
    elif playerX > settings.screen_width - 64:
        playerX = settings.screen_width - 64
        playerX_vector = 0
    # Boundary of Y axis movement for player
    if playerY < 0:
        playerY = 0
        playerY_vector = 0
    elif playerY > settings.screen_height - 64:
        playerY = settings.screen_height - 64
        playerY_vector = 0


    # Boundary of X axis movement for enemy
    if enemyX < 0:
        enemyX = 0
        enemyX_vector = - enemyX_vector
    elif enemyX > settings.screen_width - 64:
        enemyX = settings.screen_width - 64
        enemyX_vector = - enemyX_vector
    # Boundary of Y axis movement for enemy
    if enemyY < 0:
        enemyY = 0
        enemyY_vector = 0
    elif enemyY > settings.screen_height - 64:
        enemyY = settings.screen_height - 64
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
