def remove_duplicates(from_list):

    """ 
        Функція list() перетворить елемент на список.
        Функція set() перетворить елемент на множину.

        Набір схожий на список, але всі значення мають бути унікальними.

        Перетворення списку на набір видаляє всі повторювані значення.
        Потім ми перетворюємо його назад на список, оскільки нам найзручніше працювати зі списками.

    """

    from_list = list(set(from_list))

    return from_list
