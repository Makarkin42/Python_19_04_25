import pygame

VIDTH = 800
HEIGHT = 500
FPS = 90

pygame.init()

window = pygame.display.set_mode((VIDTH,HEIGHT))
pygame.display.set_caption("Игра")
clock = pygame.time.Clock()

x = 400
y = 250
run = True
while run:
    x += 1
    y += 1
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        print(event)
        if event.type == pygame.QUIT:
            run = False
    window.fill("grey")
    pygame.draw.circle(window,"black",center=(x,y),radius=100)
    pygame.display.flip()
pygame.quit()