"""
База
"""
import pygame
import sys

# size = config.size
pygame.init()
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('GameProject')

background = pygame.image.load("L9BqEs.png")
screen.blit(background, (0,0), area=[0,0,*size])
background=pygame.transform.scale(background, size)
running = True
while running:
    pygame.draw.circle(screen, (255, 235, 70), (220, 140), 20, width=2)
    pygame.draw.line(screen, (0, 0, 0), (205, 135), (215, 135), 2)
    pygame.draw.line(screen, (0, 0, 0), (225, 135), (235, 135), 2)
    pygame.draw.rect(screen, (255, 235, 70), (210, 150, 20, 20))
    pygame.draw.rect(screen, (200, 0, 0), (195, 170, 50, 100))
    pygame.draw.rect(screen, (255, 235, 70), (180, 170, 15, 95))
    pygame.draw.rect(screen, (255, 235, 70), (245, 170, 15, 95))
    pygame.draw.rect(screen, (100, 150, 255), (195, 270, 20, 100))
    pygame.draw.rect(screen, (100, 150, 255), (225, 270, 20, 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
    pygame.display.flip()
pygame.quit()
sys.exit()
