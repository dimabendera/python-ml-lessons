
# Отримання мітки часу в форматі YYYYMMDDHHMMSS

# ПРИМІТКИ: Для ясності та послідовності
# всі приклади нижче використовуватимуть однакову мітку часу; 2013 20 жовтня 09:38:26

import time

print(time.localtime())  # Часові шматки менше десяти не є нульовими
# time.struct_time(tm_year=2013, tm_mon=10, tm_mday=20,
#                  tm_hour=9, tm_min=38, tm_sec=26, tm_wday=6, tm_yday=293, tm_isdst=1)

# Потрібні фрагменти від року (від нуля) до секунди (фрагмент п'ять), тому мені потрібні індекси нарізки [0:6]

print(time.localtime()[:6])
# (2013, 10, 20, 9, 38, 26

# Тому мій інстинкт полягає в тому, щоб використовувати str.join(), щоб склеїти всі шматочки, які я хочу, скибочки [0:6]
# >>> ''.join(time.localtime()[:6])
#
# Traceback (most recent call last):
#   File "<pyshell#9>", line 1, in <module>
#     ''.join(time.localtime()[:6])
# TypeError: sequence item 0: expected string, int found

# Але цей інстинкт виявляється неправильним, тому що з'єднання хоче склеїти струни, а не інтри.


# Існує безліч варіантів вирішення цієї проблеми.

# Method #1: Циклічність (легкий, але довгий шлях)
timestamp = []

for time_chunk in time.localtime()[:6]:
    timestamp.append(str(time_chunk))

print("Method #1: ", ''.join(timestamp))

# Method #2: Проходження довільної кількості аргументів (швидко, але дещо некрасиво)

print("Method #2: ", '{0}{1}{2}{3}{4}{5}'.format(*time.localtime()[:6]))

# Method #3: Розуміння списку

print("Method #3: ", ''.join([str(time_chunk) for time_chunk in time.localtime()[:6]]))
