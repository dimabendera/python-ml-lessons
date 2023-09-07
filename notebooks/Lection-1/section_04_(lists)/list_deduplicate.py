# Дедублювання списку

# Дедублювання списку є одним з найбільш часто використовуваних дій в комп'ютерному програмуванні

# Ось, у нас є список абревіатур штатів ... Але в нашому списку багато дублікатів!
list_with_duplicates = ['CT', 'DE', 'MN', 'OH', 'CT', 'OK', 'MT', 'FL', 'TX', 'CT', 'OK', 'TX', 'PA', 'OK']

# Спочатку перетворюємо наш список з дублікатами в заданий тип, що усуне дублікати
# Далі ми перетворюємо цей набір назад у список, щоб ми могли використовувати його за призначенням.
list_without_duplicates = list(set(list_with_duplicates))

print("List with duplicates: {0}".format(list_with_duplicates))

print("List without duplicates: {0}".format(list_without_duplicates))