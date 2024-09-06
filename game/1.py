"""
Основи
"""
import pygame
import sys

# Ініціалізація PyGame
pygame.init()

# Створення вікна гри
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Назва гри')

# Завантаження зображення фону і зміна його розміру
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, screen_size)  # Змінюємо розмір зображення до розміру вікна

# Головний цикл гри
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Відображення зображення фону
    screen.blit(background, (0, 0))

    # Оновлення екрану
    pygame.display.flip()

# Вихід з PyGame
pygame.quit()
sys.exit()