# class Human:
#     name = "Hadiza"
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self, name):
#         self.name = name
#
# h1 = Human()
# print(h1.get_name())
# print(h1.name)
# h1.set_name("Raul")
# print(h1.get_name)




# class Human:
#     def __int__(self, name="", age=0):
#         self.name = name
#         self.age = age
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, age):
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self, name):
#         self.name = name
#
#
# h1 = Human("Hadiza", 25)
# print(h1.__init__())
# print(h1.name)
# h1.set_name("Raul")
# print(h1.get_name)








# class Human:
#     legs = 0
#     def __int__(self, name="", age= 0):
#         self._name = name
#         self._age = age
#
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#
#     @name.setter
#     def name(self, name: str):
#         print("calling the setter")
#         if name.islower():
#             raise ValueError("Name cannot be all lower case")
#             self._name = name
#
#     @age.setter
#     def age(self, age: int):
#         print("calling the setter")
#         self._age = age
#
#
#     @name.deleter
#     def name(self):
#         print("deleting...")
#         del self._name
#
#     @age.deleter
#     def age(self):
#         print("deleting...")
#         del self._age





# class Singleton:
#     def_new_(cls,*args, **kwargs):
#     pass
#
# s1 = Singleton()
# s2 = Singleton()
#
# print(s1)
# print(s2)
# print(s1 = s2)







class Human:
    def __init__(self, first_name: str, last_name: str, age: int, sex: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def full_name(self):
        return f"{self.last_name} {self.first_name}"


    def __str__(self):
        return f"name = {self.last_name} {self.first_name}, age = {self.age}, sex = {self.sex} "


class Manager(Human):
    def __init__(self, first_name: str, last_name: str, age: int, bonus: float, sex: str):
        self.bonus = bonus
        super().__init__(first_name, last_name, age, sex)

    def full_name(self):
        return f"{self.last_name[0].upper()}. {self.first_name}"

    def pay_salary(self, salary):
        return salary + self.bonus


class Employee(Human):
    def pay_salary(self, salary):
        return salary


employee1 = Employee("Hadiza", "Umar", 21, "Female")
manager1 = Manager("Egusi", "Cappy", 65, "Unknown")

print(employee1.full_name())
print(employee1.__str__())
print(manager1.full_name())


human_list = [employee1, manager1, Human("Sapien", "Homo", 0, "Unknown")]
for human in human_list:
    print(human.full_name())