"""
Cтворення простого головного меню
"""

import pygame
import sys

# Ініціалізація Pygame
pygame.init()

# Розміри вікна
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Кольори
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
RED = (255, 0, 0)

# Налаштування шрифту
font = pygame.font.Font(None, 36)

# Пункти меню
menu_items = ['Start', 'Options', 'Quit']

# Функція для відображення тексту
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.centerx = x
    textrect.centery = y
    surface.blit(textobj, textrect)

# Функція для гри
def game():
    running = True
    x, y = screen_width // 2, screen_height // 2
    player_size = 50
    player_speed = 5

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= player_speed
        if keys[pygame.K_RIGHT]:
            x += player_speed
        if keys[pygame.K_UP]:
            y -= player_speed
        if keys[pygame.K_DOWN]:
            y += player_speed

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, (x, y, player_size, player_size))
        pygame.display.flip()

# Головний цикл меню
def main_menu():
    while True:
        screen.fill(BLACK)  # Очистка екрана

        # Визначення позиції миші
        mx, my = pygame.mouse.get_pos()

        # Відображення пунктів меню
        for i, item in enumerate(menu_items):
            if screen_height / 2 + 50 * i - 20 < my < screen_height / 2 + 50 * i + 20:
                draw_text(item, font, GREY, screen, screen_width // 2, screen_height / 2 + 50 * i)
            else:
                draw_text(item, font, WHITE, screen, screen_width / 2, screen_height / 2 + 50 * i)

        # Обробка подій
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if screen_height / 2 - 20 < my < screen_height / 2 + 20:
                    # Запуск гри
                    game()
                elif screen_height / 2 + 30 < my < screen_height / 2 + 70:
                    # Логіка для "Options"
                    print("Options menu")
                elif screen_height / 2 + 80 < my < screen_height / 2 + 120:
                    # Логіка для "Quit"
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()  # Оновлення екрану


main_menu()
