"""
Анімація героя
"""
import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

# Завантаження зображень
run_images = [pygame.image.load(f'sprite/MC_Private_walk_right{i}.png') for i in range(1, 4)]


x = 50  # початкова позиція X
y = 250  # початкова позиція Y
frame = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Оновлення кадру
    frame += 1
    if frame >= len(run_images):  # Повернення до першого кадру
        frame = 0

    # Очищення екрану та малювання наступного кадру
    screen.fill((127, 127, 127))
    screen.blit(run_images[frame], (x, y))

    pygame.display.flip()
    clock.tick(10)  # контроль швидкості анімації

pygame.quit()
