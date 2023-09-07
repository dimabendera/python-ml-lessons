# Словники та списки разом

investigations = {
  "type": "FeatureCollection",
  "features": [
      {
       "type": "Feature",
       "geometry": {
          "type": "Point",
          "coordinates": [
             -112.073032,
             33.453527
            ]
       },
       "properties": {
          "marker-symbol": "marker",
          "marker-color": "#D4500F",
          "address": " AZ ",
          "name": "Arizona State University"
          }
      },
      {
       "type": "Feature",
       "geometry": {
          "type": "Point",
          "coordinates": [
             -121.645734,
             39.648248
            ]
        },
       "properties": {
          "marker-symbol": "marker",
          "marker-color": "#D4500F",
          "address": " CA ",
          "name": "Butte-Glen Community College District"
       }
      },
  ]
}

# Перший рівень - словник з двома ключами: тип і особливості
# Значення типу – рядок: FeatureCollection
# features' значення - список словників

# Ми зосередимося на списку функцій.

# Кожен елемент у списку функцій є словником, який має три ключі: тип, геометрія та властивості

# Якби ми хотіли отримати доступ до всіх переваг для першої точки карти, ось як це зробити:
print(investigations['features'][0]['properties'])
#   Список словників     ^       ^        ^
#              Перша точка карти |        | Властивості

# {
#   "marker-symbol": "marker",
#   "marker-color": "#D4500F",
#   "address": " AZ ",
#   "name": "Arizona State University"
# }

# Як ми бачимо вище, властивості самі по собі є словником

# Щоб отримати назву цієї точки карти:
print(investigations['features'][0]['properties']['name'])


# Взагалі кажучи, якщо між квадратними дужками є число, ви отримуєте доступ до списку.
# Якщо це рядок, ви отримуєте доступ до словника.
# Якщо ви застрягли або отримуєте помилки, спробуйте роздрукувати елемент і ключ або індекс.
