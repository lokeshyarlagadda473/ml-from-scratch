import numpy as np

class Vector:
    def __init__(self, data):
        self.data = np.array(data, dtype=float)

    def dot(self, other):
        return np.sum(self.data * other.data)

    def norm(self):
        return np.sqrt(self.dot(self))

    def __add__(self, other):
        return Vector(self.data + other.data)

    def __repr__(self):
        return f"Vector({self.data})"
