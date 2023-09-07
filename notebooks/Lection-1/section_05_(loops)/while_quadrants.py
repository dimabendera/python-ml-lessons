
nw_addresses = []
ne_addresses = []
sw_addresses = []
se_addresses = []
no_quadrant = []

address = input("Enter an address: ")

# Кожного разу, коли він досягає кінця циклу, він запитує:
# як тільки ви видалите всі зайві пробіли, адреса є порожнім рядком?
while address.strip() != "":
    
    address = address.split(" ") # Розділення адреси на список на основі пробілів

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
    # Дуже важливо, щоб ми включили цей рядок, щоб дати йому можливість змінити значення, яке перевіряє цикл time.
    address = input("Enter an address: ")


print("NW addresses include: {0}".format(nw_addresses))
print("NE addresses include: {0}".format(ne_addresses))
print("SW addresses include: {0}".format(sw_addresses))
print("SE addresses include: {0}".format(se_addresses))
print("Addresses without a quadrant include: {0}".format(no_quadrant))

# Це дуже схоже на for_quadrants.py приклад, але є деякі ключові відмінності.

# Зокрема, в for_quadrants.py потрібно вказати, скільки адрес приймати.
# Ця програма дозволить продовжувати вводити адреси до тих пір, поки ви не введете порожній рядок
# На старих комп'ютерах це чимось схоже на те, як вони змушували працювати "Натисніть будь-яку клавішу для продовження"
