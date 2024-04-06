import pygame
import math

# Ініціалізація Pygame
pygame.init()

# Встановлення розміру екрану
screen = pygame.display.set_mode((600, 400))

# Колір фону
background_color = (150, 150, 150)

# Координати вершин куба
cube_points = [
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
]


# Функція для обертання точок навколо осі Y
def rotate_y(point, angle):
    x, y, z = point
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    return [x * cos_theta - z * sin_theta, y, x * sin_theta + z * cos_theta]


# Функція для обертання точок навколо осі X
def rotate_x(point, angle):
    x, y, z = point
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    return [x, y * cos_theta - z * sin_theta, y * sin_theta + z * cos_theta]


# Головний цикл програми
running = True
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка екрану
    screen.fill(background_color)

    # Обертання куба
    angle += 0.0001  # Змінити це число для швидшого або повільнішого обертання
    rotated_points = [rotate_y(p, angle) for p in cube_points]
    rotated_points = [rotate_x(p, angle) for p in rotated_points]

    # Проекція 3D точок на 2D площину
    projected_points = [[300 + z[0] * 100, 200 + z[1] * 100] for z in rotated_points]

    # Малювання ребер куба
    for i, p in enumerate(projected_points):
        for j in range(i, len(projected_points)):
            if sum([abs(a - b) for a, b in zip(cube_points[i], cube_points[j])]) == 2:
                pygame.draw.line(screen, (0, 0, 0), p, projected_points[j], 1)

    # Оновлення екрану
    pygame.display.flip()

pygame.quit()