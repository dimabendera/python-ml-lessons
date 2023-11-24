import numpy as np


class NeuralNetwork:
    def __init__(self):
        self.w = np.random.rand()

    def forward(self, x):
        return x * self.w

    def loss(self, y_pred, y_true):
        return ((y_pred - y_true) ** 2).mean()

    def gradient(self, x, y_pred, y_true):
        return np.dot(2 * x, y_pred - y_true).mean()

    def train(self, x, y_true, epochs, learning_rate):
        for epoch in range(epochs):
            y_pred = self.forward(x)

            loss = self.loss(y_pred, y_true)

            gradient = self.gradient(x, y_pred, y_true)
            self.w -= learning_rate * gradient

            print(f"Epoch: {epoch+1}. Loss: {loss}. Weight: {self.w}")


xs = np.array(range(1, 5))
y = xs * 2
print(xs)
print(y)

nn = NeuralNetwork()

nn.train(xs, y, epochs=50, learning_rate=0.01)

pred = nn.forward(6)
print(pred)