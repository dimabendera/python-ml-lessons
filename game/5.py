"""
Гра з текстом score
Ловити падаючі зірочкти
"""
import pygame
import sys
import random

# Ініціалізація Pygame
pygame.init()

# Створення вікна гри
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Збери Зірки')

# Кольори
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Позиція та розмір корабля
ship_x = 300
ship_y = 440  # Зробимо корабель трохи вище низу екрана
ship_width = 40
ship_height = 20

# Швидкість зірки
star_speed = 5

# Створення зірки (просто точка на початку)
star_x = random.randint(0, screen_size[0])
star_y = 0
star_radius = 5

# Лічильник зібраних зірок
score = 0

# Головний ігровий цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Вхід від користувача
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ship_x > 0:
        ship_x -= 5
    if keys[pygame.K_RIGHT] and ship_x < screen_size[0] - ship_width:
        ship_x += 5

    # Переміщення зірки
    star_y += star_speed

    # Перевірка на збір зірки
    if ship_y < star_y + star_radius < ship_y + ship_height and ship_x < star_x + star_radius < ship_x + ship_width:
        score += 1
        star_x = random.randint(0, screen_size[0])
        star_y = 0

    # Перезапуск зірки, якщо вона досягла нижнього краю екрана
    if star_y > screen_size[1]:
        star_x = random.randint(0, screen_size[0])
        star_y = 0

    # Очищення екрану
    screen.fill((0, 0, 0))

    # Малювання корабля і зірки
    pygame.draw.rect(screen, BLUE, (ship_x, ship_y, ship_width, ship_height))
    pygame.draw.circle(screen, WHITE, (star_x, star_y), star_radius)

    # Відображення рахунку
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

    # Оновлення екрану
    pygame.display.flip()

    # Контроль швидкості гри
    pygame.time.Clock().tick(60)

# Вихід з PyGame
pygame.quit()
sys.exit()
