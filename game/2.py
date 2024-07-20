"""
Базове малювання
pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
pygame.draw.circle(screen, color, (x, y), radius)
pygame.draw.line(screen, color, start_pos, end_pos, width)
pygame.draw.ellipse(screen, color, pygame.Rect(x, y, width, height))
pygame.draw.polygon(screen, color, points)
"""


import pygame
import sys

# Ініціалізація PyGame
pygame.init()

# Створення вікна гри
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Анімація руху об'єктів")


# Початкове положення квадрата
x = 50
y = 50

# Швидкість руху квадрата (пікселі за одне оновлення)
speed_x = 2
speed_y = 2

# Головний цикл гри
running = True
while running:
    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Оновлення положення об'єкта
    x += speed_x
    y += speed_y

    # Перевірка зіткнення з краями вікна
    if x + 50 > screen_size[0] or x < 0:
        speed_x = -speed_x
    if y + 50 > screen_size[1] or y < 0:
        speed_y = -speed_y

    # Заповнення екрана чорним кольором
    screen.fill((0, 0, 0))

    # Малювання об'єкта
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))

    # Оновлення відображення
    pygame.display.flip()

    # Контроль швидкості оновлення
    pygame.time.Clock().tick(60)

# Вихід з PyGame
pygame.quit()
sys.exit()
