# Example #8: try-finally

# Використовуйте остаточний блок, приєднаний до блоку проб, для виконання коду незалежно від того, що станеться

user_input = input("Please enter a number: ")

try:
    user_input = int(float(user_input))
except ValueError:
    print("You didn't enter a number, did you?")
else:  # помилок не сталося
    print("Hooray! We didn't encounter any errors!")
finally:  # Незважаючи ні на що
    print("Here was your input: {0}".format(user_input))

print("'finally' isn't that common though, and you could really just put your code outside of the block entirely.")
print("Here was your input: {0}".format(user_input))
