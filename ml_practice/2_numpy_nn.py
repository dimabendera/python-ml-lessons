import numpy as np

class NeuralNetwork:
    def __init__(self):
        self.w1 = np.random.rand()
        self.w2 = np.random.rand()

    def forward(self, x1, x2):
        return x1 * self.w1 + x2 * self.w2

    def loss(self, y_pred, y_true):
        return ((y_pred - y_true) ** 2).mean()

    def gradient(self, x1, x2, y_pred, y_true):
        grad_w1 = np.dot(2 * x1, y_pred - y_true).mean()
        grad_w2 = np.dot(2 * x2, y_pred - y_true).mean()
        return grad_w1, grad_w2

    def train(self, x1, x2, y_true, epochs, learning_rate):
        for epoch in range(epochs):
            y_pred = self.forward(x1, x2)

            loss = self.loss(y_pred, y_true)

            grad_w1, grad_w2 = self.gradient(x1, x2, y_pred, y_true)
            self.w1 -= learning_rate * grad_w1
            self.w2 -= learning_rate * grad_w2

            print(f"Epoch: {epoch+1}. Loss: {loss}. Weights: {self.w1}, {self.w2}")


x1 = np.array([1, 2, 3, 4])
x2 = np.array([2, 3, 4, 5])  # Другий вхідний масив
y = x1 * x2  # Правильні відповіді для множення

nn = NeuralNetwork()

nn.train(x1, x2, y, epochs=50, learning_rate=0.01)

pred = nn.forward(6, 7)
print(pred)
