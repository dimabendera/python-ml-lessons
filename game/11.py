import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Налаштування екрану
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Pygame Game with Classes")

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Головний клас гри
class Game:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.enemies = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.spawn_enemy()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.game_over = False

    def spawn_enemy(self):
        enemy = Enemy()
        self.enemies.add(enemy)
        self.all_sprites.add(enemy)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        if not self.game_over:
            self.all_sprites.update()
            # Перевірка на зіткнення гравця з ворогами
            if pygame.sprite.spritecollideany(self.player, self.enemies):
                self.game_over = True
            # Спавн ворогів кожні 2 секунди
            if pygame.time.get_ticks() % 2000 < 20:
                self.spawn_enemy()
            self.score += 1

    def draw(self):
        screen.fill(WHITE)
        self.all_sprites.draw(screen)
        self.display_score()
        if self.game_over:
            self.display_game_over()
        pygame.display.flip()

    def display_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(score_text, (10, 10))

    def display_game_over(self):
        game_over_text = self.font.render("Game Over", True, RED)
        score_text = self.font.render(f"Final Score: {self.score}", True, BLACK)
        screen.blit(game_over_text, (screen_width // 2 - 50, screen_height // 2 - 20))
        screen.blit(score_text, (screen_width // 2 - 70, screen_height // 2 + 20))

# Клас гравця
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 50)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.centerx += self.speed

# Клас ворога
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speedy = random.randint(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > screen_height:
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speedy = random.randint(1, 8)

# Запуск гри
if __name__ == "__main__":
    game = Game()
    game.run()
