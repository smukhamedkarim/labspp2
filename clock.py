import pygame
from datetime import datetime

pygame.init()

clock_face = pygame.image.load("clock.png")
minute_hand = pygame.image.load("rightarm.png")
second_hand = pygame.image.load("leftarm.png")

WIDTH, HEIGHT = clock_face.get_size()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

center_x, center_y = WIDTH // 2, HEIGHT // 2 + 20

def draw_hand(image, angle, pivot):
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=pivot)
    screen.blit(rotated_image, rotated_rect.topleft)

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_face, (0, 0))

    current_time = datetime.now()
    minutes = current_time.minute
    seconds = current_time.second

    minute_angle = -(minutes * 6 + seconds * 0.1)
    second_angle = -seconds * 6

    draw_hand(minute_hand, minute_angle, (center_x, center_y))
    draw_hand(second_hand, second_angle, (center_x, center_y))
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()