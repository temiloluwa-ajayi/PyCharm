class DoubleIt(int):
    def __new__(cls, value):
        return super().__new__(cls, value * 2)


d = DoubleIt(4)


class MyList(list):
    def __setitem__(self, index, value):
        print("No problem")
        if index < 1:
            raise IndexError("Index can neither be negative nor zero")
        super().__setitem__(index - 1, value)

    def __getitem__(self, index):
        print("I can't anything")
        if index < 1:
            raise IndexError("Index can neither be negative nor zero")
        super().__setitem__(index - 1)


l = MyList()

# l.append(1)
# print(l)
# l[0] = 67
# print(l)

l = MyList("hello")

# l.append(1)
# print(l)
# l[0] = 67
# print(l)

# l[0]


# print(d)
# d += 6
# print(d)

print(l)
l[1] = 67
print(l)


class UniqueDict(dict):
    def __setdict__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("Can only take a String ")
        super().__setitem__(key, value)

    def __getdict__(self, keyword):
        super().__setitem__(keyword)


phonebook = {'Chris': '555−1111', 'Katie': '555−2222', 'Joanne': '555−3333'}
print(phonebook)
phonebook = {'Katie': '555−2222'}
print(phonebook)

myDicy = UniqueDict()
myDicy['1'] = 6
print(myDicy)
print(type("") != str)