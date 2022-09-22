class Human(object):
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def __str__(self):
        return f"name = {self.last_name} {self.first_name}, age = {self.age}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.last_name} {self.first_name}')"


class Manager(Human):
    def __init__(self, first_name: str, last_name: str, age: int, bonus: float, ):
        self.bonus = bonus
        super().__init__(first_name, last_name, age)

    def full_name(self):
        return f"{self.last_name[0].upper()}. {self.first_name}"

    def pay_salary(self, salary):
        return salary + self.bonus


class Employee(Human):
    def pay_salary(self, salary):
        return salary


employee1 = Employee("Hadiza", "Umar", 21)
manager1 = Manager("Egusi", "Cappy", 65, 1_200)

print(employee1.full_name())
print(employee1.__str__())
print(manager1.full_name())

human_list = [employee1, manager1, Human("Sapien", "Homo", 0)]
for human in human_list:
    print(human.full_name())
    print(f"{employee1:}")
    print(employee1.pay_salary(50_000))


class Practice:
    count = 0

    def __init__(self, first):
        self.first = first
        Practice.count += 1

    def play(self):
        return f"playing with {self.first}"

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def create(cls, name):
        return cls(name)

    # @classmethod
    # def create(cls, name, modifier):
    #     return cls(modifier + " " + name)

    @staticmethod
    def just_here():
        return "Just hanging out here!!!"


p1 = Practice("Banke")
p2 = Practice.create("Hadiza")
Practice.just_here()
p1.just_here()

# Work on this later on
# p3 = Practice.create("Hadiza", "Mrs")
# print(p3)
# print(p2.first)


# ------------------------------------------------- INHERITANCE -------------------------------------------------
class A:
    def do_this(self):
        print("From A")


class B(A):
    pass


class C(A):
    def do_this(self):
        print("From C")


class D(B, C):
    pass


# d = D()
# d.do_this()
# print(D.mro())
# print(D.__mro__)
# help(D)

# ------------------------------------------------- COMPOSITION -------------------------------------------------
class Address:
    def __init__(self, number, street, city):
        self.number = number
        self.street = street
        self.city = city


class Person:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address


addr = Address(312, "Herbert Macaulay", "Yaba")
p1 = Person("Hadiza", addr)
print(addr)
print(addr.street)
print(p1.address.number)




