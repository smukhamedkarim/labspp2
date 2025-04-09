import pygame
import random
import sys
import time

# Инициализация Pygame
pygame.init()
pygame.mixer.init()

# Размер окна
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game Demo")
clock = pygame.time.Clock()

# Шрифт
font = pygame.font.Font(None, 30)

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Настройки змейки
snake_pos = [100, 50]  # Начальная позиция головы змейки
snake_body = [[100, 50], [90, 50], [80, 50]]  # Начальное тело змейки
snake_direction = "RIGHT"  # Начальное направление
change_to = snake_direction
speed = 10  # Начальная скорость

# Счёт и уровень
game_score = 0
level = 1

# Класс еды с весом и таймером
class Food:
    def __init__(self):
        self.weight = random.choice([1, 2, 3])  # Случайный "вес" еды
        self.color = YELLOW if self.weight == 2 else (RED if self.weight == 1 else (255, 165, 0))  # Цвет по весу
        self.pos = self.generate_position()
        self.spawn_time = time.time()  # Время появления еды
        self.lifetime = random.randint(5, 8)  # Еда исчезает через 5–8 секунд

    def generate_position(self):
        """Генерация позиции, не пересекающейся со змейкой."""
        while True:
            x = random.randrange(0, WIDTH, 10)
            y = random.randrange(0, HEIGHT, 10)
            if [x, y] not in snake_body:
                return [x, y]

    def is_expired(self):
        """Проверка, прошло ли время жизни еды."""
        return time.time() - self.spawn_time > self.lifetime

# Первая еда
food = Food()

# Игровой цикл
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"

    # Изменение направления змейки
    snake_direction = change_to
    if snake_direction == "UP":
        snake_pos[1] -= 10
    elif snake_direction == "DOWN":
        snake_pos[1] += 10
    elif snake_direction == "LEFT":
        snake_pos[0] -= 10
    elif snake_direction == "RIGHT":
        snake_pos[0] += 10

    # Обновление позиции змейки
    snake_body.insert(0, list(snake_pos))

    # Проверка, съела ли змейка еду
    if snake_pos == food.pos:
        game_score += food.weight
        if game_score % 4 == 0:
            level += 1
            speed += 2  # Увеличиваем скорость с каждым уровнем
        food = Food()  # Генерируем новую еду
    else:
        snake_body.pop()

    # Проверка, исчезла ли еда
    if food.is_expired():
        food = Food()

    # Проверка столкновений со стенами
    if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
        snake_pos[1] < 0 or snake_pos[1] >= HEIGHT):
        isRunning = False

    # Проверка на столкновение с телом змейки
    for block in snake_body[1:]:
        if snake_pos == block:
            isRunning = False

    # Отрисовка объектов
    screen.fill(BLACK)
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], 10, 10))

    # Рисуем еду
    pygame.draw.rect(screen, food.color, pygame.Rect(food.pos[0], food.pos[1], 10, 10))

    # Отображение счёта и уровня
    score_text = font.render(f"Score: {game_score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (20, 20))

    pygame.display.update()
    clock.tick(speed)

# Экран завершения игры
game_over_text = font.render("GAME OVER", True, WHITE)
game_over_rectangle = game_over_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(3000)
pygame.quit()