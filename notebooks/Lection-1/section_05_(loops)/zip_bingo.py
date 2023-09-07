# Базове бінго з використанням zip()

words = ['apple', 'banana', 'carrot', 'danke', 'elephant', 'fruit', 'gorilla', 'horse, michael', 'ice cream',
         'jack, one eye', 'kazoo', 'lollerskates', 'mango', 'noodles', 'oboe', 'porcupine', 'quill', 'rowboat',
         'sailboat', 'trolley', 'umbrella', 'voltage', 'watermelon', 'xylophobe', 'yarn', 'zebra-clops']

print("words has {0} words in the list.".format(len(words)))

output = ''

# Звичайний для циклів дозволяє циклічно переглядати список і робити щось для кожного елемента в цьому списку.
# Цикл for за допомогою zip() дозволяє циклічно переглядати декілька списків
# і робити щось із кожним елементом цих списків одночасно.
# Зазвичай це потрібно зробити зі списками однакового розміру.
# Але це все одно працює, якщо один список коротший; Просто він поводиться трохи інакше.

# У цьому випадку довжина слів становить 26 елементів, а довжина діапазону (25) становить 25 елементів
# Таким чином, for цикл буде запущений лише 25 разів у цьому випадку.

# Незалежно від того, скільки ще предметів ви додаєте до слів, ваша дошка бінго повинна мати лише 25 квадратів.

# Якщо ви розкоментуєте наступні рядки , ви отримуватимете випадкову дошку бінго щоразу, коли запускаєтесь!
# import random
# random.shuffle(words)

for word, position in zip(words, list(range(25))):
    if position == 12:
        output += 'Free space,'
    else:
        output += "{0},".format(word)
    if position in (4, 9, 14, 19, 24):
        output += "\n"

print(output)

# apple,banana,carrot,danke,elephant,
# fruit,gorilla,horse, michael,ice cream,jack, one eye,
# kazoo,lollerskates,Free space,noodles,oboe,
# porcupine,quill,rowboat,sailboat,trolley,
# umbrella,voltage,watermelon,xylophobe,yarn,
