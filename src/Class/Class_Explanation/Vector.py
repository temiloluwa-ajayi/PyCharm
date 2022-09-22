import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"{self.x}i + {self.y}j"

    def __repr__(self):
        return f"Vector({self.x}i + {self.y}j`~)"

    def __len__(self):
        return 1

    # def __bool__(self):
    #     return True

    def __lt__(self, other):
        return abs(self) < abs(other)

v1 = Vector(2, 4)
v2 = Vector(1, 6)
v3 = v1 + v2
print(v1)
print(v3)
print(v3 < v2)
print(bool(v1))


lst = [v3, v1, v2]
print(lst)