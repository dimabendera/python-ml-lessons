# Якщо ви новачок у словниках, ви можете почати з dict_access.py

# Створюємо словник.

contacts = {
    'Shannon': '202-555-1234',
    'Amy': '410-515-3000',
    'Jen': '301-600-5555',
    'Julie': '202-333-9876'
}

# Ми можемо використовувати метод словника .items(), щоб дати нам список усіх елементів у контактах.

print(list(contacts.items()))

# Строго кажучи, .items() не дає нам список, він дає нам *кортеж*,
# що є ще одним способом зберігання інформації в Python.
# Кортежі майже ідентичні спискам, за винятком того, що вони доступні лише для читання.
# Ви не можете додавати/видаляти з кортежу.
# Але доступ до них і вони використовуються майже однаково, тому ми будемо ставитися до цього так,
# ніби Python дає нам список, і він буде вести себе так, як ми очікуємо.

# .items() дає нам ключ і ціннісну пару разом - щоб ми могли використовувати це безпосередньо, коли ми циклічно.

for contact, phone in list(contacts.items()):
    print("{0}'s number is {1}".format(contact, phone))

# .items() ймовірно, найчастіше використовується з .keys(), .values() і .items(),
# оскільки він надає вам ключ і значення разом.
