def add(first_number, second_number):
    """
    Add two numbers
    :param first_number: int
    :param second_number: int
    :return: int
    """

    return first_number + second_number


print(add(2, 3))


def add(first_number: int, second_number: int) -> int:
    """
    Add two numbers
    :param first_number: int
    :param second_number: int
    :return: int
    """

    return first_number + second_number


print(add(2, 3))
print(add.__doc__)
print(add.__name__)
print(add.__annotations__)


def get_digit(number, position):
    """return digit at position in number, counting from right"""
    return number // (10 ** position) % 10


print(get_digit(12, 10))


def get_length(number: int) -> int:
    import math
    return len(str(number))


print(get_length(45432))


def get_length(number: int) -> int:
    import math
    return math.ceil(math.log10(number))


print(get_length(4563))

a: list = []