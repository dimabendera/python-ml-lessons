

instructions = """Введіть однобуквену команду та натисніть Enter:
A, щоб додати ім'я до списку
R, щоб видалити ім'я зі списку
S, щоб відобразити імена у списку
Q, щоб вийти
>"""

allowed_commands = ['a', 'r', 's', 'q']
names = []

command = input(instructions)

while command.lower() in allowed_commands:
    
    if command.lower() == 'a':
        name = input("Введіть ім'я, яке потрібно додати до списку. ")
        names.append(name)
    elif command.lower() == 'r':
        name = input("Введіть ім'я, яке потрібно видалити зі списку: ")
        # Це видалить перший екземпляр цього імені, який з'явиться; Якщо дублікати є, буде видалений тільки перший
        names.pop(names.index(name))
    elif command.lower() == 's':
        print('\n'.join(names))
    elif command.lower() == 'q':
        break  # Це вирветься з циклу While

    command = input(instructions)
