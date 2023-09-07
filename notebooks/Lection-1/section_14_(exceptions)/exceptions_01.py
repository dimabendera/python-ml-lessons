# Example #1: Обробка простих винятків

try:
    print(1/0)  # Зробити це не вдасться.
except ZeroDivisionError:
    print("You can't divide by zero!")
