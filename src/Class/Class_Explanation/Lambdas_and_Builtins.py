def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


print(add.__name__)
print(add.__doc__)
print(add.__annotations__)


def operate(x, y, func):
    return func(x, y)


print(operate(2, 3, add))


def sub(x, y):
    return y - x


print(operate(5, 8, sub))


# Currying
def multiply(a):
    def by(b):
        return a * b

    return by


multiply_by_five = multiply(5)
print(multiply_by_five(6))
# OR
multiply_by_five = multiply(5)(6)
print(multiply_by_five)


def multiply(a):
    def by(b):
        def another(c):
            return a * b * c

        return another

    return by


multiply_by_five = multiply(5)(6)(7)
print(multiply_by_five)

add = lambda a, b: a + b
print(add.__name__)
print(add(10, 9))
print(operate(2, 3, add))
print(operate(2, 3, lambda a, b: a + b))
print(operate(2, 3, lambda a, b: b - a))
print(operate(2, 3, lambda a, b: a * b))
print(operate(2, 3, lambda a, b: a / b))
# By the way
# buzz = lambda a, b, c: a / b * c
# print(operate(2, 3, 4 lambda a, b, c: a / b * c))

import math
print(operate(2, 3, lambda a, b: math.sqrt(a + b)))


import builtins
# L - Local
# E - Enclosure
# G - Global
# B - Builtins

# sum = 67

print(builtins.sum([10, 20, 30]))
print(abs(-1))
print(round(56.67854))
print(round(56.67854, 2))
print(round(56.67854, -1))

arr = [1, 6, 4, 7, 2]
print(sum(arr))

print(sum(arr, 100))

letters = [['a'], ['b', 'c'], ['d'], ['e', 'f']]
print(sum(letters, []))
#USED TO FLATTEN A LIST
# sum takes at most 2 iterables


print(max(1, 2, 3, 4, 5, 6))
print(max([1, 2, 3, 4, 5, 6]))

fruits = "apple pear cucumber mango grape melon".split()
print(max(fruits))
print(max(fruits, key = len))

print(min(fruits))
print(min(fruits, key = len))
# Only functions are assigned to the key in the maximum and minimum functions When checking for the length of the
# split strings, and there are multiple strings with the same length, it returns the very first one.


print(max(fruits, key = lambda x: x[-1]))

print(max(fruits, key = lambda x: x[-3 : ]))

def last_three(x):
    return x[-3 : ]

print(max(fruits, key = last_three))

iterable1 = (1, 2, 3, 4)
iterable2 = ('hello', 'how', 'are', 'you')
print(list(zip(iterable2, iterable1)))
print(list(zip(iterable2, iterable1, strict=True)))

print(sorted('hello'))

print(sorted('hello', reverse=True))
print(sorted(fruits, key=len))
print(sorted(fruits, key=lambda x: x[-1]))

# Any(or) All(and)


lst = [1, 2, 3, 4, 5]
print(list(map(lambda x: x ** 2,  lst)))
# OR
print([x ** 2 for x in lst])


print(list(map(str.upper, fruits)))
# OR
print(list(map(lambda x: x.upper(),  fruits)))

fruits.append('Agbado')
print(fruits)
print(list(map(str.istitle, fruits)))

print(list(filter(str.istitle, fruits)))
# OR
print(list(filter(lambda x: x.istitle(),  fruits)))

print(list(filter(lambda x: not x.istitle(),  fruits)))

print(list(map(lambda y: y.upper(), filter(lambda x: not x.istitle(), fruits))))
# OR
print([x.upper() for x in fruits if not x.istitle()])


from functools import reduce
# from functools import
from math import prod

def reduce_func(acc, item):
    print(f"acc --> {acc} <> item --> {item}")
    return acc + item

print("\n#################### Reduce ####################\n")
# print(reduce(lambda acc, item: acc + item, lst))
print(lst)
print(reduce(reduce_func, lst))
print(reduce(reduce_func, lst, 100))
print(reduce(lambda acc, item: acc if acc > item else item, lst))
print(reduce(lambda acc, item: acc if acc > item else item, fruits))
print(reduce(lambda acc, item: acc if len(acc) > len(item) else item, fruits))
# print(reduce(max_func, fruits))
print(sum(lst, 100))
print(prod(lst, start=100))

num = int(input("Enter a number: "))

match num:
    case 1:
        print(1)
    case 2:
        print(2)
    case _ as x if 1 <= x <= 10:
        print(x)
    case _ as x if 1 <= x <= 20:
        print(x)
    case 30 | 40 | 50:
        print(x)
    case _:
        print("Don't know you.")


lst = [20, {13, 15}, 16]

match lst:
    case [i1, i2, i3]:
        print(i3, i2, i1)
    case [a, [b, c], d]:
        print(a, b, c, d)
    case _:
        print("Nothing Matched")


d = {
    "Name": "Hadiza",
    "Age": 18,
    "is_SWIT": True
}

match d:
    case {"Name": str(name), "Age": int(age)}:
        print(name, age)
    case _:
        print("Nothing Matched")


def fizzbuzz(num):
    three = num % 3
    five = num % 5
    match (three, five):
        case (0, 0):
            return "FIZZBUZZ"
        case (0, _):
            return "FIZZ"
        case (_, 0):
            return "BUZZ"
        case _:
            return num


for i in range(1, 101):
    print(fizzbuzz(i))


def summing_list(list_: list[int]) -> int:
    match list_:
        case[]:
            return 0
        case [first_value, *another_list]:
            return first_value + summing_list(another_list)
        case _:
            print("Can only accept an int")
            return None


print(summing_list([1, 2, 3, 4, 5]))


import itertools
print(summing_list([1, 2, 3, 4, 5]))
print(list(itertools.zip_longest([1,2], [3, 4, 5], fillvalue=0)))