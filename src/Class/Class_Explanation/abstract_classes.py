import abc


# class Mammal(metaclass=abc.ABCMeta):
class Mammal(abc.ABC):

    def move(self):
        pass


class Person(Mammal):
    def move(self):
        pass


m1 = Mammal()
p1 = Person()
