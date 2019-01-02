import pygame
from dobjects import Cube

pygame.init()
running = True
x = 800
y = 600
screen = pygame.display.set_mode((x, y))
clock = pygame.time.Clock()

cuboid = Cube()
point_list = []


while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for points in cuboid.disp():
        pygame.draw.polygon(screen, (255, 255, 255), points)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        cuboid.translate_x()

    pygame.display.update()
    clock.tick(30)
