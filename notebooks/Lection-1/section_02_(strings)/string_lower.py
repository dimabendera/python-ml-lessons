# Методи рядків: string.lower()

# string.lower() використовується для перетворення всіх символів у рядку нижнього регістру.
# Існують також деякі пов'язані методи рядка, такі як string.upper()

name = "SHANNON!!"

print(name.lower())  # shannon!!
print(name)  # Це повернення до оригіналу SHANNON!!

# Щоб внести зміни:
name = name.lower()

print(name)  # shannon!!


# string.upper() перетворить усі символи у верхньому регістрі рядка,
# але в іншому випадку працюватиме так само, як string.lower()

greeting = "hello, hi"  # не дуже буйний...

print(greeting.upper())  # НАБАГАТО КРАЩЕ!

# Внесення змін залишається:
greeting = greeting.upper()

print(greeting)  # HELLO, hi


# string.lower() і .upper() в основному використовуються для тестування рядків нечутливим до регістру способом

gender = 'F'

if gender.lower() == 'f':
    print("Hi lady!")

# Щоб виконати те ж саме без string.lower(), вам доведеться зробити:
if gender == 'F' or gender == 'f':
    print("Hi lady!")
