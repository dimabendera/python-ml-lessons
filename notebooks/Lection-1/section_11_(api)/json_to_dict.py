# Перетворення словників (а також списків, рядків тощо) у JSON

# Для початку використовуйте вбудовану бібліотеку json.  Вам не потрібно встановлювати це, він поставляється з python.
import json

# Тепер завантажте файл (contacts.json) section_11_(api)/dict_to_json.py
with open('contacts.json', 'r') as contacts_file:
    contacts = contacts_file.read()

print(contacts)

print("\n\n contacts above is a string")

# Тепер ми завантажили вміст файлу у вигляді рядка, який виглядає як JSON.
# json.loads() дозволить нам завантажити його назад у форму, яку Python може використовувати (і циклічно переключити)
contacts = json.loads(contacts)

print(contacts)

print("\n\n Тепер ви можете циклічно переглядати контакти, оскільки це список "
      "(зі словниками та іншими смаколиками, вкладеними всередині)")
