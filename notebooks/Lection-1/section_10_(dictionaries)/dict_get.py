# Якщо ви новачок у словниках, ви можете почати з dict_access.py

# Створюємо словник.

contacts = {
    'Shannon': '202-555-1234',
    'Amy': '410-515-3000',
    'Jen': '301-600-5555',
    'Julie': '202-333-9876'
}

name = input("Enter the name of the person whose phone number you want: ")

print("We will get a KeyError if you entered a name that wasn't in the dictionary.")
print("{0}'s number is: {1}".format(name, contacts[name]))

print("But there's a way we don't need to worry about KeyErrors.")

name = input("Enter the name of the person whose phone number you want ... might I suggest Frankenstein? ")

# .get() - це метод словника, який дозволяє нам безпечно отримати доступ до словника, навіть якщо цього ключа не існує.

print("{0}'s number is ... {1}".format(name, contacts.get(name, " ... I couldn't find it!")))
