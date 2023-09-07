def is_alphaspace(string):

    """
    Повертає значення "True", якщо всі символи в рядку складаються з пробілів або літер; інакше повертає значення False.

    використання str.isalpha() повертає bool про те, чи ВСІ символи в рядку є літерами
    використання str.isspace() повертає bool щодо того, чи ВСІ символи в рядку є пробілами;

    Хоча це не строковий метод, ця функція поєднує в собі функціональність строковий методів, наведених вище
    """
    
    return all([any([char.isspace(), char.isalpha()]) for char in string])

# Ця користувацька функція працюватиме подібно до str.isalpha() та str.isspace(), об'єднаних разом.


test_string = "Цей рядок поверне false для кожної з isalpha та isspace, але повернеться true для користувацької функції"

print("test_string.isalpha() gives us: ", test_string.isalpha())
print("test_string.isspace() gives us: ", test_string.isspace())

# Зверніть увагу на те, чим відрізняється синтаксис.
# Це тому, що is_alphaspace() не є рядковим методом, це користувацька функція.
print("But is_alphaspace(test_string) gives us: ", is_alphaspace(test_string))

