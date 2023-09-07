# Рядкові методи: string.find()

# string.find() повідомляє, де можна знайти частину одного рядка у більшому рядку.
# string.find() поверне число:
# 		Якщо string.find() повертає -1, він не зможе знайти рядок всередині більшого рядка.
# 		В іншому випадку string.find() поверне номер фрагмента/індекс того місця, де знайдено цей рядок

email_address = "hoorayforpython@notarealwebsite.com"

print("I found the snail at: {0}".format(email_address.find("@")))  # Номер/індекс, де з'являється символ @

# string.find() + slicing = Супер!

# Все, що передує @, є частиною email_handle; Все, що після @ є частиною домену, де зареєстрована електронна пошта.
# Давайте використаємо string.find() і slice разом, щоб розділити їх на частини.

at_symbol_index = email_address.find("@")
print("I found the snail at: {0}".format(at_symbol_index))

email_handle = email_address[0:at_symbol_index]

print("The email_handle is: {0}".format(email_handle))

# Без +1 символ @ був би включений.
# Зверніть увагу, що після двокрапки немає числа, тому Python припускає, що ви хочете, щоб все було до кінця.
email_domain = email_address[at_symbol_index + 1:]

print("The email_domain is: {0}".format(email_domain))

print("When string.find() can't find a string, it'll give a -1.  So since there's no 'QQQ' in email_address, "
      "this will return a -1: {0}".format(email_address.find("QQQ")))
