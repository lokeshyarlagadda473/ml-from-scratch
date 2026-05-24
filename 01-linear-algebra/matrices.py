import numpy as np

class Matrix:
    def __init__(self, data):
        self.data = np.array(data, dtype=float)
        self.shape = self.data.shape

    def matmul(self, other):
        return Matrix(self.data @ other.data)

    def transpose(self):
        return Matrix(self.data.T)

    def __repr__(self):
        return f"Matrix({self.data})"
