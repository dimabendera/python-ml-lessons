import pygame
import sys

# Ініціалізація Pygame
pygame.init()

# Розміри екрану
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Назва вікна
pygame.display.set_caption('Гра з Чоловічком')

# Колір фону
WHITE = (255, 255, 255)

# Завантаження зображення чоловічка
man_image = pygame.image.load('L9BqEs.png')  # Припускаємо, що ваше зображення називається man.png
man_image = pygame.transform.scale(man_image, (40, 40))  # Зміна розміру зображення, якщо потрібно

# Позиція чоловічка
man_x = 50
man_y = 350

# Головний цикл гри
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Вхід від користувача
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and man_x > 0:
        man_x -= 0.05
    if keys[pygame.K_RIGHT] and man_x < screen_width - 50:  # 50 - ширина зображення чоловічка
        man_x += 0.05

    # Очищення екрану
    screen.fill(WHITE)

    # Малювання чоловічка
    screen.blit(man_image, (man_x, man_y))

    # Оновлення екрану
    pygame.display.update()

# Вихід з Pygame
pygame.quit()
sys.exit()
