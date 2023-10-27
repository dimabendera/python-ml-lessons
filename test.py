data = [
    [0, 'A', 100.5, 1, 0],
    [1, 'B', 1000.0, 5, 1],
    [0, 'C', 50.0, 2, 0],
    [1, 'D', 1200.0, 10, 1],
    [0, 'A', 150.0, 1, 0],
    [1, 'B', 750.0, 4, 1],
    [0, 'C', 80.0, 3, 0],
    [1, 'D', 900.0, 8, 1],
    [0, 'B', 200.0, 2, 0],
    [1, 'C', 600.0, 3, 0],
    [0, 'A', 110.0, 1, 0],
    [1, 'D', 950.0, 7, 1],
    [0, 'C', 70.0, 2, 0],
    [1, 'B', 700.0, 5, 1],
    [0, 'D', 250.0, 3, 0],
    [1, 'A', 800.0, 4, 0],
    [0, 'B', 140.0, 2, 0],
    [1, 'C', 650.0, 5, 1],
    [0, 'D', 220.0, 3, 0],
    [1, 'A', 850.0, 6, 1]
]


def min_max_normalize(data, min_val, max_val):
    return (data - min_val) / (max_val - min_val)


min_sum = min([row[2] for row in data])
max_sum = max([row[2] for row in data])
min_transactions = min([row[3] for row in data])
max_transactions = max([row[3] for row in data])

normalized_data = []

for row in data:
    row[2] = min_max_normalize(row[2], min_sum, max_sum)
    row[3] = min_max_normalize(row[3], min_transactions, max_transactions)

    type_encoding = [0, 0, 0, 0]
    if row[1] == 'A':
        type_encoding = [1, 0, 0, 0]
    elif row[1] == 'B':
        type_encoding = [0, 1, 0, 0]
    elif row[1] == 'C':
        type_encoding = [0, 0, 1, 0]
    elif row[1] == 'D':
        type_encoding = [0, 0, 0, 1]
    normalized_row = [row[0], row[2], row[3], row[
        4]] + type_encoding  # Залишаємо бінарний параметр, числові параметри і кодовані категоріальні параметри
    normalized_data.append(normalized_row)

for row in normalized_data:
    print(row)