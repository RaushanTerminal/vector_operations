import numpy as np

class Vector:
    def __init__(self, elements):
        self.elements = np.array(elements)

    def add(self, other):
        return self.elements + other.elements

    def subtract(self, other):
        return self.elements - other.elements

    def scalar_multiply(self, scalar):
        return self.elements * scalar

    def dot_product(self, other):
        return np.dot(self.elements, other.elements)

    def normalize(self):
        norm = np.linalg.norm(self.elements)
        return self.elements / norm if norm != 0 else self.elements

    def project_onto(self, other):
        dot_product = np.dot(self.elements, other.elements)
        norm_squared = np.dot(other.elements, other.elements)
        return (dot_product / norm_squared) * other.elements if norm_squared != 0 else self.elements

# Example Usage:
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("Addition:", v1.add(v2))
print("Subtraction:", v1.subtract(v2))
print("Scalar Multiplication:", v1.scalar_multiply(2))
print("Dot Product:", v1.dot_product(v2))
print("Normalization:", v1.normalize())
print("Projection:", v1.project_onto(v2))

