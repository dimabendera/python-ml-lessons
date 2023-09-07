# enumerate() приклад

# enumerate() використовується для циклічного перегляду списку та для кожного елемента списку,
# щоб також надати індекс, де цей елемент можна знайти

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Ось як ми звикли циклічно - для кожного елемента в цьому списку надрукуйте цей елемент
for day in days:
	print(day)


# Тепер додаємо шар складності.  Зверніть увагу, як дві змінні (індекс, день) створюються циклом for.
for index, day in enumerate(days):
	print("days[{0}] contains {1}".format(index, day))
	print("day contains {0}".format(day))


# Since we humans aren't counting days by zero, we do a little addition inside the .format()
for index, day in enumerate(days):
	print("{0} is day # {1}".format(day, index+1))
