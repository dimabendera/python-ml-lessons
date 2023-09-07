# Рядкові методи: string.replace()

# string.replace() схожа на функцію find -> replace у програмах Word, Excel або інших програмах типу Office Y

song = "eat, eat, eat, apples and bananas"

# Почнемо тут:
print("I like to ... {0}".format(song))


# string.replace() дозволяє замінити всі екземпляри одного рядка іншим.
print("I like to ... {0}".format(song.replace("a", "o")))  # Ми замінюємо всі малі літери *a*s у пісні на *o*s

# Давайте подивимося на синтаксис.
# Ми бачили синтаксис {0}; Це заповнювач, який string.format() використовує для вставки змінної в рядок,
# що стоїть перед крапкою в .format()
# 0 відповідає першій змінній у списку в дужках (пам'ятайте, що Python починає рахувати з нуля)
# Яку змінну ми збираємося вставити в {0}? Це song.replace("a", "o")
# Python оцінить song.replace("a", "o") і помістить результат всередину {0}
# Як працює song.replace("a", "o"): .replace() замінить кожну "a", яку він знайде в пісні, на "o"
# Як я пам'ятаю, це .replace() виконає свою дію на те, що стоїть перед крапкою (що в song.replace("a", "o"), є піснею)

print("But note that the original song itself is unchanged: {0}".format(song))

print("string.replace() is case-sensitive.")
print(song.replace("Eat", "chop"))  # Це нічого не замінить!

print(song)
print(song.replace("eat", "chop"))
print(song)  # оригінал незмінний

# Якщо ви хочете, щоб ваші зміни залишилися, вам потрібно буде призначити змінній пісні нове значення
song = song.replace("eat", "chop")
# Те, що ми тут говоримо, по суті:
# Пісня тепер дорівнює новому значенню song.replace("їсти", "рубати")

# Якщо у вас є багато замін на рядку, ви * могли б * зробити це так:
song = song.replace("apples", "mangos")
song = song.replace(" and", ", pears, and")
song = song.replace("bananas", "kiwis")

print(song)

# Або ви можете об'єднати багато замін разом - пам'ятайте, що замінюється те, що передує крапці!
# Іншими словами, заміни будуть відбуватися в порядку зліва направо
song = "eat, eat, eat, apples and bananas"  # setting it back to the original
song = song.replace("eat", "chop").replace("apples", "mangos").replace(" and", ", pears, and")\
    .replace("bananas", "kiwis")

print(song)
