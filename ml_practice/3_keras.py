import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

# Створення моделі
model = keras.Sequential([
    layers.Dense(units=64, activation='relu', input_shape=(2,)),
    layers.Dense(units=1)
])

# Компіляція моделі
model.compile(optimizer='adam', loss='mean_squared_error')

# Підготовка даних для тренування
# Приклад: множимо числа від 0 до 99
x = np.array([[i, j] for i in range(100) for j in range(100)])
y = np.prod(x, axis=1)

# Тренування моделі
model.fit(x, y, epochs=10)

# Перевірка результату
test_input = np.array([[5, 6]])
predicted = model.predict(test_input)
print(f"Результат множення {test_input[0][0]} на {test_input[0][1]}: {predicted[0][0]}")