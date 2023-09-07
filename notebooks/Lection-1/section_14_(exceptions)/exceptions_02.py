# Example #2: Винятки запускають блок except і пропускають будь-який код після помилки.

try:
    print(1/0)  # Зробити це не вдасться.
    print("I'm code that will never run!")

    print(555/0)  # Це не вдасться, якщо ми ніколи не потрапимо сюди.
    # Ось чому найкраще використовувати блок проб на найменшій кількості рядків коду.

except ZeroDivisionError:
    print("You still can't divide by zero!")
