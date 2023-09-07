days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
foods_of_day = ['Manicotti', 'Tacos', 'Waffles', 'Raspberries', 'Franks', 'Salad', 'Soup']

# Приклад #1
for day in days_of_week:
    print("Today is {0}".format(day))
print("\n")


# Приклад #2: Перерахувати (повертає індекс елемента списку)
for (index, day) in enumerate(days_of_week):
    # Будь ласка, вибачте/ігноруйте 0-й день та граматику для "1-го", "2-го", "3-го"
    print("Today is the {0}th day of the week, which is {1}".format(index, day))

    # У цьому циклі за допомогою enumerate ми можемо отримати доступ до значень елементів списку двома способами:
    # безпосередньо за допомогою циклічної змінної day (що краще) або за допомогою індексу.
    print("So day_of_week[{0}] is: {1}, which is the same as day, which is: {2}".format(index,
                                                                                        days_of_week[index],
                                                                                        day))
print("\n")

# Приклад #3: Zip
for (day, food) in zip(days_of_week, foods_of_day):
    print("Today is {0} so obviously I'm having {1} for dinner.".format(day, food))

# ПРИМІТКА: zip покладається на те, що кожен список має однакову довжину! Якщо списки не однакової довжини,
# zip буде циклічно переглядати лише стільки елементів, скільки є в коротшому списку!
