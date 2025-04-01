import pygame
pygame.init()
width=500 
height=500
bg_color=(255,255,255)#white background
screen=pygame.display.set_mode((width,height))
radius=25
circle_color=(255,0,0)#red circle
step=20
circle_x,circle_y=width//2,height//2#it places the circle exatly at the center

running = True
while running:
    pygame.time.delay(50)  #for smooth movement
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and circle_x-radius-step >= 0:
        circle_x -= step
    if keys[pygame.K_RIGHT] and circle_x+radius+step <= width:
        circle_x += step
    if keys[pygame.K_UP] and circle_y-radius-step >= 0:
        circle_y -= step
    if keys[pygame.K_DOWN] and circle_y+radius+step <=height:
        circle_y += step
    
    # drawing everything on thee screem
    screen.fill(bg_color)
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y),radius)
    pygame.display.update()

pygame.quit()

