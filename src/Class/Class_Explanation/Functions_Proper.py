# print(globals())
#
# def fun(num):
#     print(locals())
#
#     func(15)

a = 5


def func1():
    global a
    a = 7
    print(a)


func1()

a = 5


def func1():
    b = 10

    def inner_func():
        nonlocal b
        b += 2
        print(b)

    inner_func()
    print(b)


func1()

func1()


# def func(*nums):

def func(**kwargs):
    print(kwargs)

    func(1, 2, 3, 4, 5, 6)

    lst = [3, 1, 7, 4, -3, 4]

    dict_ = {"a": 2, "b": 6, "c": 7}
    func1(**dict_)

    func(*lst)  # func(lst[0], lst[1], lst[2])


def variance(*args):
    sum((sum(args) / len(args) - arg) ** 2 for arg in args) / len(args)

    print(variance(1, 2, 4))


def func_again(a, b, /, c, d):
    print(a, b, c, d)

    func_again(1, 2, 3, 4)  # OR func_again(1, 2, c = 3, d = 4)


def func_again(a, b, /, c, *, d):
    print(a, b, c, d)

    func_again(1, 2, 3, d=4)  # OR func_again(1, 2, c = 3, d = 4)
