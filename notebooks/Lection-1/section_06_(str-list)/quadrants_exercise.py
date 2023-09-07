# Вправа, яку ви будете виконувати перед групою під час групової вправи.
# Це приблизне наближення коду, яке ви в кінцевому підсумку отримаєте.
# Це не те, з чого ви почнете.
# Перша версія вашого коду буде неповною і трохи неправильною.
# Ви будете говорити про вправу, запитуючи відгуки від класу.
# Обов'язково задавайте багато питань, особливо "що ми очікуємо, що тут станеться?"
# Кожну проблему спеціально розроблено, щоб спричинити неочікувану поведінку, якщо програму написано неретельно.
# Добре перейматися цими проблемними рішеннями. Студенти нічого не дізнаються, побачивши,
# як ви робите це ідеально за один раз.
# Але вони багато чому навчаться з процесу повторення, пошуку проблеми та вдосконалення.

NW = []
NE = []
SE = []
SW = []
Other = []

address = ""  # Введіть свої адреси тут.
# Problem 1: 123 SEA LANE SW
# Problem 2: 456 fake st se
# Problem 3: 678 lincoln ave

print(address)

address_as_list = address.upper().split(' ')

if 'NW' in address_as_list:
    NW.append(address)
elif 'NE' in address_as_list:
    NE.append(address)
elif 'SE' in address_as_list:
    SE.append(address)
elif 'SW' in address_as_list:
    SW.append(address)
else:
    Other.append(address)

print("NW is {0}".format(NW))
print("NE is {0}".format(NE))
print("SE is {0}".format(SE))
print("SW is {0}".format(SW))
print("Other is {0}".format(Other))
