# Example #7: try-else

# Використовуйте блок else, приєднаний до блоку проби, якщо потрібно виконати код лише тоді, коли помилок не виникло.

user_input = input("Please enter a number: ")

try:
    user_input = int(float(user_input))
except ValueError:
    print("You didn't enter a number, did you?")
else:  # помилок не сталося
    print("Hooray! We didn't encounter any errors!")
    print("Oh, by the way, your number was: {0}".format(user_input))
