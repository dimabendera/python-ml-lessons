
# Дванадцять днів Різдва, стиль Python

gifts = ["A partridge in a pear tree",
         "Two turtle doves",
         "Three french hens",
         "Four colly birds",
         "Five golden rings",
         "Six geese-a-laying",
         "Seven swans-a-swimming",
         "Eight maids-a-milking",
         "Nine ladies dancing",
         "Ten lords-a-leaping",
         "Eleven pipers piping",
         "Twelve drummers drumming"
         ]

gifts_given = []

for day in range(1, 13):  # ідентичні заяві за день в [1,2,3,4,5,6,7,8,9,10,11,12]:
    # використовувати list.extend() при додаванні одного або декількох елементів в кінець списку;
    gifts_given.extend(gifts[:day])
    # Якби ви використовували тут .append() замість .extend(), ви отримали б список списків
    # - не зовсім те, що ми хочемо в цьому випадку.

    if day == 1:
        suffix = "st"
    elif day == 2:
        suffix = "nd"
    elif day == 3:
        suffix = "rd"
    elif day >= 4:
        suffix = "th"

    print("---------------------------------------------------------")
    print("On the {0}{1} day of Christmas, my true love gave to me: ".format(day, suffix))
    print("---------------------------------------------------------")

    print("\t" + "\n\t".join(reversed(gifts[:day])))

print("---------------------------------------------------------")
print("The gifts I have received in total are: ")
print("---------------------------------------------------------")

print("\t" + "\n\t".join(sorted(gifts_given)))

print("---------------------------------------------------------")
print("Over all twelve days I received: ")
print("---------------------------------------------------------")

total_gifts = 0

for repetitions, day in zip(reversed(list(range(1, 13))), list(range(1, 13))):
    # Тут відбувається складна нарізка!
    print("{0} of {1}".format(repetitions * day, gifts[day-1][gifts[day-1].index(' ')+1:]))
    total_gifts += repetitions * day

print("I received {0} gifts in total".format(total_gifts))

# Примітка про складну нарізку:

# Перше слово в кожному подарунку - скільки було отримано в той день.
# Таким чином, я можу отримати доступ до самого подарунка (а не до отриманого номера) за допомогою
# розрізання повз індекс першого пробілу в кожному рядку.

# gifts[day-1] це поточний подарунок, який представляє собою рядок, що містить назву подарунка (включно з номером)
# Нарізка на цьому рядку (починаючи з індексу, де відбувається перший пробіл)
# дозволяє нам вийняти номер і просто отримати сам подарунок.

# Отже, іншими словами:

# gifts = ["A partridge in a pear tree", ... ]
# Оскільки подарунки - це список, ми можемо отримати доступ до подарункових предметів шляхом нарізки.

# gifts[2] – рядок, "Three french hens"
# gifts[2][0] – рядок, "T"

# Але ми не хочемо починати з gifts[2][0].
# Ми хочемо почати з gifts[2][5] -але кожного разу це не буде 5; Для кожного подарунка вона буде різною.

# Якби ми зробили "Three french hens".index(' ')+1, Ми отримаємо індекс лише за першим пробілом, який з'явиться.

# Отже, ми вставляємо це в індекс другого фрагмента і додаємо : щоб гарантувати, що він триватиме до кінця.

# Так: gifts[day-1][gifts[day-1].index(' ')+1:]
