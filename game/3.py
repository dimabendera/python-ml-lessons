import pygame
import sys

# Ініціалізація PyGame
pygame.init()

# Створення вікна гри
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Понг для двох гравців')

# Налаштування кольорів
WHITE = (255, 255, 255)

# Початкові позиції палок та м'яча
paddle1_x, paddle1_y = 50, screen_size[1] // 2 - 60
paddle2_x, paddle2_y = screen_size[0] - 70, screen_size[1] // 2 - 60
ball_x, ball_y = screen_size[0] // 2, screen_size[1] // 2
ball_dx, ball_dy = 5, 5  # Швидкість м'яча

# Розміри палок та м'яча
paddle_width, paddle_height = 20, 120
ball_size = 20

# Швидкість палок
paddle_speed = 10

# Головний цикл гри
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отримання стану клавіш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < screen_size[1] - paddle_height:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < screen_size[1] - paddle_height:
        paddle2_y += paddle_speed

    # Рух м'яча
    ball_x += ball_dx
    ball_y += ball_dy

    # Відбивання м'яча від верхньої та нижньої стінок
    if ball_y <= 0 or ball_y >= screen_size[1] - ball_size:
        ball_dy = -ball_dy

    # Відбивання м'яча від палок
    if (ball_x <= paddle1_x + paddle_width and paddle1_y < ball_y < paddle1_y + paddle_height) or \
            (ball_x >= paddle2_x - ball_size and paddle2_y < ball_y < paddle2_y + paddle_height):
        ball_dx = -ball_dx

    # Перевірка на гол (м'яч залишив екран)
    if ball_x < 0 or ball_x > screen_size[0]:
        ball_x, ball_y = screen_size[0] // 2, screen_size[1] // 2  # Скидання м'яча до центру

    # Очищення екрану
    screen.fill((0, 0, 0))
    # Малювання палок та м'яча
    pygame.draw.rect(screen, WHITE, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (paddle2_x, paddle2_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, ball_size, ball_size))

    # Оновлення екрану
    pygame.display.flip()

    # Контроль частоти оновлень
    pygame.time.Clock().tick(60)

# Вихід з PyGame
pygame.quit()
sys.exit()