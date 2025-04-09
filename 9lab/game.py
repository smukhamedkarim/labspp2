import pygame
import sys
import random
import time

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 400, 600
FPS = 60
PLAYER_SPEED = 5
ENEMY_SPEED = 5
COIN_SIZE = 30
SCORE = 0
COINS = 0
COINS_FOR_SPEEDUP = 5  # Количество монет, после которых враг ускоряется

ASSETS = "/Users/symbatmuhamedkarim/Desktop/8lab/"

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Dodge Game")
clock = pygame.time.Clock()
font_small = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 60)

# Звук столкновения
crash_sound = pygame.mixer.Sound(ASSETS + "crash.wav")

# Фон
background = pygame.image.load(ASSETS + "background.png")

# Игрок
player_img = pygame.image.load(ASSETS + "Player.png")
player_rect = player_img.get_rect(center=(WIDTH // 2, HEIGHT - 80))

# Враг
enemy_img = pygame.image.load(ASSETS + "enemy.png")
enemy_rect = enemy_img.get_rect(center=(random.randint(40, WIDTH - 40), 0))

# Функция для создания монеты с весом
def generate_coin():
    coin = {}
    coin['weight'] = random.choice([1, 2, 3])  # Вес монеты (очки)
    coin['image'] = pygame.image.load(ASSETS + "coin.jpg")
    coin['image'] = pygame.transform.scale(coin['image'], (COIN_SIZE, COIN_SIZE))
    coin['rect'] = coin['image'].get_rect(center=(random.randint(40, WIDTH - 40), random.randint(0, HEIGHT // 2)))
    return coin

coin = generate_coin()  # первая монета

# Событие для увеличения скорости
INCREASE_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INCREASE_SPEED, 1000)

# Главный цикл
running = True
while running:
    screen.blit(background, (0, 0))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == INCREASE_SPEED:
            ENEMY_SPEED += 0.5

    # Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += PLAYER_SPEED

    # Движение врага
    enemy_rect.y += int(ENEMY_SPEED)
    if enemy_rect.top > HEIGHT:
        SCORE += 1
        enemy_rect.center = (random.randint(40, WIDTH - 40), 0)

    # Движение монеты
    coin['rect'].y += int(ENEMY_SPEED)
    if coin['rect'].top > HEIGHT:
        coin = generate_coin()

    # Проверка столкновения с врагом
    if player_rect.colliderect(enemy_rect):
        crash_sound.play()
        screen.fill(RED)
        screen.blit(font_big.render("Game Over", True, BLACK), (50, 250))
        pygame.display.update()
        time.sleep(2)
        break

    # Проверка сбора монеты
    if player_rect.colliderect(coin['rect']):
        COINS += coin['weight']  # Добавляем очки по весу монеты
        if COINS % COINS_FOR_SPEEDUP == 0:
            ENEMY_SPEED += 1  # Увеличиваем скорость врага
        coin = generate_coin()  # Генерируем новую монету

    # Отрисовка объектов
    screen.blit(player_img, player_rect)
    screen.blit(enemy_img, enemy_rect)
    screen.blit(coin['image'], coin['rect'])
    screen.blit(font_small.render("Score: " + str(SCORE), True, BLACK), (10, 10))
    screen.blit(font_small.render("Coins: " + str(COINS), True, BLACK), (WIDTH - 130, 10))

    # Обновление экрана
    pygame.display.update()
    clock.tick(FPS)

# Выход
pygame.quit()
sys.exit()