import time
import os

# Встановлення часу спрацьовування будильника
alarm_time = "10:00"  # Формат ГГ:ХХ
print(f"Будильник встановлено на {alarm_time}")

# Отримання поточного часу та перетворення його у формат ГГ:ХХ
current_time = time.strftime("%H:%M")
while current_time != alarm_time:
    print("Чекаю...")
    time.sleep(10)  # Чекати 10 секунд перед наступною перевіркою часу
    current_time = time.strftime("%H:%M")

# Відтворення звуку, коли поточний час дорівнює часу будильника
print("Будильник!")
os.system('play path/to/your/soundfile.mp3')  # Замініть 'path/to/your/soundfile.mp3' на шлях до вашого звукового файлу

