import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Завантаження датасету Boston Housing
(x_train_full, y_train_full), (x_test, y_test) = keras.datasets.boston_housing.load_data()

# Поділ тренувальних даних на тренувальний та валідаційний набори
x_train, x_val, y_train, y_val = train_test_split(x_train_full, y_train_full, test_size=0.2, random_state=0)

# Нормалізація даних
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_val = scaler.transform(x_val)
x_test = scaler.transform(x_test)

# Створення моделі
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(x_train.shape[1],)),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
])

# Компіляція моделі
model.compile(optimizer='adam', loss='mean_squared_error')

# Тренування моделі
history = model.fit(x_train, y_train, epochs=50, validation_data=(x_val, y_val))

# Оцінка моделі
test_loss = model.evaluate(x_test, y_test)
print(f"Тестова втрата: {test_loss}")

# Опціонально: Виведення історії тренування (наприклад, втрата та втрата на валідації)
import matplotlib.pyplot as plt

plt.plot(history.history['loss'], label='Training loss')
plt.plot(history.history['val_loss'], label='Validation loss')
plt.title('Training and Validation Loss')
plt.legend()
plt.show()
