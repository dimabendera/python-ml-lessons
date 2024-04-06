import pygame

pygame.init()
pygame.mixer.init()

# Завантаження звукового файлу
sound_effect = pygame.mixer.Sound("path/to/your/sound_effect.wav")
background_music = pygame.mixer.music.load("path/to/your/background_music.mp3")


# Відтворення звукового ефекту
sound_effect.play()

# Відтворення фонової музики
pygame.mixer.music.play(-1)  # Аргумент -1 означає повторення відтворення нескінченно


# Припустимо, що player.rect і item.rect - це прямокутники PyGame, що представляють гравця та предмет відповідно
if player.rect.colliderect(item.rect):
    sound_effect.play()
    # Логіка видалення предмету або нагороди гравця