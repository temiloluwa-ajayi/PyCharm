class CustomClass:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __getattr__(self, item):
        pass

    def __mul__(self, other):
        return "Multiplication"

    def __lt__(self, other):
        return self.num < other.num

    def __str__(self):
        return str(self.num)

    def __repr__(self):
        return str(self.num)


c1 = CustomClass(7)
c2 = CustomClass(8)

print(c1 + c2)
print(c1 * c2)
print(c1 < c2)

lst = [c2, c1]
print(lst)
print(c1)
lst.sort()
print(lst)
