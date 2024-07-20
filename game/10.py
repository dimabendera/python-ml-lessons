"""
Приклад гри "Влуч у блок"
Цей приклад буде демонструвати просту гру, де гравець керує платформою, щоб ловити падаючі блоки. Ми створимо наступні функції:
"""
import pygame
import random

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    return screen

def create_block():
    return {'rect': pygame.Rect(random.randint(0, 775), 0, 25, 25), 'color': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))}

def move_block(block):
    block['rect'].move_ip(0, 5)

def draw_elements(screen, blocks, paddle):
    screen.fill((0, 0, 0))
    for block in blocks:
        pygame.draw.rect(screen, block['color'], block['rect'])
    pygame.draw.rect(screen, (255, 255, 255), paddle)
    pygame.display.flip()

def check_collision(block, paddle):
    return block['rect'].colliderect(paddle)

def main_loop():
    screen = init_game()
    paddle = pygame.Rect(300, 550, 200, 50)
    blocks = []
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.move_ip(-10, 0)
        if keys[pygame.K_RIGHT] and paddle.right < 800:
            paddle.move_ip(10, 0)

        if random.randint(1, 20) == 1:
            blocks.append(create_block())

        for block in blocks:
            move_block(block)
            if check_collision(block, paddle):
                blocks.remove(block)

        draw_elements(screen, blocks, paddle)
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main_loop()
