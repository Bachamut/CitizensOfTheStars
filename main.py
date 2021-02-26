import pygame

# initialize of pygame
pygame.init()

# create a screen
screen = pygame.display.set_mode((800, 600))
# title and icon
pygame.display.set_caption("CitizensOfTheStars")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("spaceship.png")

playerX = 368
playerY = 510

playerX_vector = 0
playerY_vector = 0

decoupled = True
active = False


def player(x, y):
    screen.blit(playerImg, (x, y))


# Game Loop
running = True


while running:
    # screen background color (RBG)
    screen.fill((50, 80, 000))

    # checking pressed keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerX_vector += -0.0002
    if keys[pygame.K_RIGHT]:
        playerX_vector += 0.0002
    if keys[pygame.K_UP]:
        playerY_vector += -0.0002
    if keys[pygame.K_DOWN]:
        playerY_vector += 0.0002
    if decoupled == active:
        if keys[pygame.K_LEFT] == False and playerX_vector <= 0:
            playerX_vector += 0.0001
        if keys[pygame.K_RIGHT] == False and playerX_vector >= 0:
            playerX_vector -= 0.0001
        if keys[pygame.K_UP] == False and playerY_vector <= 0:
            playerY_vector += 0.0001
        if keys[pygame.K_DOWN] == False and playerY_vector >= 0:
            playerY_vector -= 0.0001

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                active = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                active = False

        # check which key was pressed
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         playerX_vector += -0.02
        #     if event.key == pygame.K_RIGHT:
        #         playerX_vector += 0.02
            # if event.key == pygame.K_UP:
            #     playerY_change = -0.1
            # if event.key == pygame.K_DOWN:
            #     playerY_change = 0.1

        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT:
        #         if playerX_vector < 0:
        #             playerX_vector += 0.084
        #         else:
        #             playerX_vector = 0

            # if event.key == pygame.K_RIGHT:
            #     playerX_change = 0
            # if event.key == pygame.K_UP:
            #     playerY_change = 0
            # if event.key == pygame.K_DOWN:
            #     playerY_change = 0

    # Bounderies of X axis movement
    if playerX < 0:
        playerX = 0
        playerX_vector = 0
    elif playerX > 736:
        playerX = 736
        playerX_vector = 0
    # Boundries of Y axis movement
    if playerY < 0:
        playerY = 0
        playerY_vector = 0
    elif playerY > 536:
        playerY = 536
        playerY_vector = 0

    playerX += playerX_vector
    playerY += playerY_vector
    player(playerX, playerY)
    pygame.display.update()
