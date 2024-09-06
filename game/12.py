import pygame
import random

# Ініціалізація Pygame
pygame.init()
# Ініціалізуємо всі модулі Pygame, необхідні для роботи.

# Налаштування екрану
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Pygame Game with Classes")
# Встановлюємо розміри екрану 800x600 пікселів та заголовок вікна "Simple Pygame Game with Classes".

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
# Визначаємо основні кольори, які будемо використовувати.

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
    # Ініціалізуємо головний клас гри, створюючи всі необхідні об'єкти та змінні.

    def spawn_enemy(self):
        enemy = Enemy()
        self.enemies.add(enemy)
        self.all_sprites.add(enemy)
    # Метод для створення нового ворога і додавання його до групи спрайтів.

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()
    # Основний цикл гри, який обробляє події, оновлює стан гри та відображає її. Завершується викликом pygame.quit().

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    # Обробка подій, зокрема закриття вікна гри.

    def update(self):
        if not self.game_over:
            self.all_sprites.update()
            # Оновлення стану всіх спрайтів.
            if pygame.sprite.spritecollideany(self.player, self.enemies):
                self.game_over = True
            # Перевірка зіткнення гравця з ворогами. Якщо зіткнення відбулося, гра завершується.

            if pygame.time.get_ticks() % 2000 < 20:
                self.spawn_enemy()
            # Спавн ворогів кожні 2 секунди.
            self.score += 1
            # Збільшення рахунку гри.

    def draw(self):
        screen.fill(WHITE)
        self.all_sprites.draw(screen)
        self.display_score()
        if self.game_over:
            self.display_game_over()
        pygame.display.flip()
    # Відображення всіх спрайтів та елементів інтерфейсу.

    def display_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(score_text, (10, 10))
    # Відображення поточного рахунку гри.

    def display_game_over(self):
        game_over_text = self.font.render("Game Over", True, RED)
        score_text = self.font.render(f"Final Score: {self.score}", True, BLACK)
        screen.blit(game_over_text, (screen_width // 2 - 50, screen_height // 2 - 20))
        screen.blit(score_text, (screen_width // 2 - 70, screen_height // 2 + 20))
    # Відображення повідомлення про завершення гри та фінального рахунку.

# Клас гравця
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images_right = [pygame.image.load(f'sprite/right/MC_Private_walk_right{i}.png') for i in range(4)]
        self.images_left = [pygame.image.load(f'sprite/left/MC_Private_walk_left{i}.png') for i in range(4)]
        self.images_stand = [pygame.image.load(f'sprite/stand/MC_Private_idle{i}.png') for i in range(2)]
        self.image = self.images_stand[0]
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 50)
        self.speed = 5
        self.animation_speed = 0.1
        self.time_accumulator = 0
        self.frame_index = 0
    # Ініціалізація об'єкта гравця з його зображеннями, позицією та іншими параметрами.

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= self.speed
            self.animate(self.images_left)
        elif keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.centerx += self.speed
            self.animate(self.images_right)
        else:
            self.animate(self.images_stand)
    # Оновлення стану гравця залежно від натиснутих клавіш.

    def animate(self, images):
        self.time_accumulator += self.animation_speed
        if self.time_accumulator >= 1:
            self.time_accumulator = 0
            self.frame_index = (self.frame_index + 1) % len(images)
            self.image = images[self.frame_index]
    # Анімація гравця шляхом зміни зображення залежно від накопиченого часу.

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
    # Ініціалізація об'єкта ворога з його зображенням, початковою позицією та швидкістю.

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > screen_height:
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speedy = random.randint(1, 8)
    # Оновлення стану ворога: рух вниз по екрану та повернення до верхньої частини екрану, якщо ворог вийшов за межі.

# Запуск гри
if __name__ == "__main__":
    game = Game()
    game.run()
# Ініціалізація та запуск гри.
