import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255, 255, 255))
    rect = pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))
    rect = rect.center
    pygame.display.flip()