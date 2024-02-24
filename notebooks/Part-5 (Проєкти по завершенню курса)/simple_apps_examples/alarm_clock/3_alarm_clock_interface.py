import tkinter as tk
from tkinter import messagebox
import time
import threading
from playsound import playsound


def set_alarm():
    alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    print(f"Будильник встановлено на {alarm_time}")
    messagebox.showinfo("Будильник", f"Встановлено на {alarm_time}")

    def check_alarm():
        while True:
            current_time = time.strftime("%H:%M:%S")
            if current_time == alarm_time:
                print("Будильник!")
                playsound('soundfile.mp3')
                break
            time.sleep(1)

    threading.Thread(target=check_alarm).start()


# Створення головного вікна
root = tk.Tk()
root.title("Будильник")

# Налаштування розмірів вікна
root.geometry("300x200")

# Створення полів для вводу часу
hour = tk.StringVar()
tk.Entry(root, textvariable=hour, width=5).place(x=110, y=30)
hour.set('ГГ')

minute = tk.StringVar()
tk.Entry(root, textvariable=minute, width=5).place(x=150, y=30)
minute.set('ХХ')

second = tk.StringVar()
tk.Entry(root, textvariable=second, width=5).place(x=190, y=30)
second.set('СС')

# Створення та розміщення кнопки для встановлення будильника
tk.Button(root, text="Встановити будильник", command=set_alarm).place(x=100, y=70)

# Запуск головного циклу Tkinter
root.mainloop()
