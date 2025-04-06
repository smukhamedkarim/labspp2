import pygame
import sys
import random
import time

pygame.init()

# const
WIDTH, HEIGHT = 400, 600
FPS = 60
PLAYER_SPEED = 5
ENEMY_SPEED = 5
COIN_SIZE = 30
SCORE = 0
COINS = 0

ASSETS = "/Users/symbatmuhamedkarim/Desktop/8lab/"

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# display settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Dodge Game")
clock = pygame.time.Clock()
font_small = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 60)

# sound 
crash_sound = pygame.mixer.Sound(ASSETS + "crash.wav")
background = pygame.image.load(ASSETS + "background.png")

# player
player_img = pygame.image.load(ASSETS + "Player.png")
player_rect = player_img.get_rect(center=(WIDTH // 2, HEIGHT - 80))

# enemy
enemy_img = pygame.image.load(ASSETS + "enemy.png")
enemy_rect = enemy_img.get_rect(center=(random.randint(40, WIDTH - 40), 0))

# coin
coin_img = pygame.image.load(ASSETS + "coin.jpg")
coin_img = pygame.transform.scale(coin_img, (COIN_SIZE, COIN_SIZE))
coin_rect = coin_img.get_rect(center=(random.randint(40, WIDTH - 40), random.randint(0, HEIGHT // 2)))

# speed
INCREASE_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INCREASE_SPEED, 1000)

# main 
running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == INCREASE_SPEED:
            ENEMY_SPEED += 0.5

    # control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += PLAYER_SPEED

    # enemy movement
    enemy_rect.y += int(ENEMY_SPEED)
    if enemy_rect.top > HEIGHT:
        SCORE += 1
        enemy_rect.center = (random.randint(40, WIDTH - 40), 0)

    # coin movement
    coin_rect.y += int(ENEMY_SPEED)
    if coin_rect.top > HEIGHT:
        coin_rect.center = (random.randint(40, WIDTH - 40), random.randint(0, HEIGHT // 2))

    # checking for collision
    if player_rect.colliderect(enemy_rect):
        crash_sound.play()
        screen.fill(RED)
        screen.blit(font_big.render("Game Over", True, BLACK), (50, 250))
        pygame.display.update()
        time.sleep(2)
        break

    if player_rect.colliderect(coin_rect):
        COINS += 1
        coin_rect.center = (random.randint(40, WIDTH - 40), random.randint(0, HEIGHT // 2))

    # rendering
    screen.blit(player_img, player_rect)
    screen.blit(enemy_img, enemy_rect)
    screen.blit(coin_img, coin_rect)
    screen.blit(font_small.render("Score: " + str(SCORE), True, BLACK), (10, 10))
    screen.blit(font_small.render("Coins: " + str(COINS), True, BLACK), (WIDTH - 100, 10))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()