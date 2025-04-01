import pygame

pygame.init()
pygame.mixer.init()

playlist = [r"David Guetta Feat. Kid Cudi - Memories.mp3", r"Flo Rida - Whistle.mp3"]
current_track = 0
keys_pressed = set() 

def play():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play(0)

def stop():
    pygame.mixer.music.stop()

def next():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play()

def previous():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play()

done = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode((200, 200))

while not done:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.scancode not in keys_pressed:
            keys_pressed.add(event.scancode)

            if event.scancode == 81:  #вверх
                stop()
            elif event.scancode == 82:  #вниз
                play()
            elif event.scancode == 79:  #вправо
                next()
            elif event.scancode == 80:  #влево
                previous()

        if event.type == pygame.KEYUP:
            if event.scancode in keys_pressed:
                keys_pressed.remove(event.scancode)

    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()