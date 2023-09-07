# Почніть зі створення чотирьох списків квадрантів.  Ми дізнаємося про кращий спосіб зробити це на наступному уроці.

nw_addresses = []
ne_addresses = []
sw_addresses = []
se_addresses = []
no_quadrant = []

for entry in range(3):  # Зробіть це три рази:
    address = input("What is your address? ")  # отримати адресу від користувача

    address = address.split(" ")  # Розділення адреси на список на основі пробілів

    if 'NW' in address:
        # якщо в адресі відображається "NW", додайте адресу (приєднану назад у вигляді рядка) до відповідного списку
        nw_addresses.append(' '.join(address))
    elif 'NE' in address:
        ne_addresses.append(' '.join(address))
    elif 'SW' in address:
        sw_addresses.append(' '.join(address))
    elif 'SE' in address:
        se_addresses.append(' '.join(address))
    else:
        # У всіх інших випадках
        no_quadrant.append(' '.join(address))


print("NW addresses include: {0}".format(nw_addresses))
print("NE addresses include: {0}".format(ne_addresses))
print("SW addresses include: {0}".format(sw_addresses))
print("SE addresses include: {0}".format(se_addresses))
print("Addresses without a quadrant include: {0}".format(no_quadrant))

# Про що варто подумати:

# 1) До якого списку буде додано 1500 CORNWALL ST? Чому так?
# 2) Іншими словами, як працює оператор 'in', коли ви використовуєте його в рядку проти списку?
# 3) Подумайте про це по-іншому, якби ви прокоментували рядок 12 і провели цю адресу, ви отримали б інший результат.
