def access(dictionary, nested_keys):

    """ Спробуйте отримати доступ до вкладених клавіш у словнику.
        Повертає значення False (хибність) замість помилки ключа (KeyError) у разі помилки.

        Написано, щоб уникнути необхідності виконувати кілька спроб/за винятком
        блоків при спробі отримати доступ до певних значень у JSON.

        Раніше:
            try:
                title = response['response']['docs'][0]['descriptiveNonRepeating']['title']['content']
            except KeyError:
                pass

            # ... і повторюючи цю структуру для кожної змінної, яку ми хотіли б зберегти.
            # Ми могли б загорнути *цілу* річ у спробу/крім, але тоді це спровокувало б хіба що на першій невдачі.

        Зараз:
            title = access(response, ['response', 'docs', 0, 'descriptiveNonRepeating', 'title', 'content'])

            # ... і повторюючи цю структуру для кожної змінної, яку ми хотіли б зберегти.

    """

    for index, key in enumerate(nested_keys):

        print(index, key)

        try:
            if key in dictionary:
                if nested_keys[index + 1:] != []:
                    return access(dictionary[key], nested_keys[index + 1:])
                else:
                    return dictionary[key]
            else:
                return False
        except AttributeError:  # На даний момент словник являє собою список, можливо, містить словники
            if key < len(dictionary):
                if nested_keys[index + 1:] != []:
                    return access(dictionary[key], nested_keys[index + 1:])
                else:
                    return dictionary[key]
            else:
                return False
