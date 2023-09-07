# Основи зі списком: додавання елементів, видалення елементів, вставлення елементів, поділ на фрагменти

names = []  # пустий список
print(names)

names.append('Shannon')  # Додавання одного елемента в кінець списку
print(names)

# Доступ до імен за допомогою нарізки:
print(names[0])  # Shannon

# Вставлення елемента (а не просто додавання його в кінець):
names.insert(0, 'Finn')
print(names)

# 0 – номер фрагмента, куди потрібно вставити елемент ПЕРЕД
# Іншими словами, це вставить 'Finn' просто *до* індексу 0

many_more = ['Jake', 'Princess Bubblegum', 'Marceline the Vampire Queen', 'Peppermint Butler']

# Тепер ми можемо додати всі імена many_more кінця списку
names.extend(many_more)
print(names)

# Тепер ми збираємося піти без цукру, тому всі з цукеркового королівства повинні піти.
# Давайте видалимо з нашого списку м'яту дворецьку та принцесу Бубблегум.

names.pop()  # це видалить останній елемент зі списку, яким виявляється Peppermint Butler
print(names)

names.pop(3)  # це видалить елемент під номером нарізки / індексом 3, який є Princess Bubblegum
print(names)

# Тепер ми збираємося шукати елемент і видаляти його.
remove_this = names.index('Jake')
print("I found Jake at slicing number / index #{0}".format(remove_this))
print("Now I can use .pop() to remove that item.")
names.pop(remove_this)
print(names)

# Ми також можемо використовувати .remove(), щоб скоротити це.
names.remove('Finn')
print(names)
