import pygame


pygame.init()

pygame.display.set_caption("Dooms Day")

screen_size = (288, 512)
screen = pygame.display.set_mode(screen_size)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(0)
    screen.fill("cyan")

    pygame.display.flip()

pygame.quit()