import doctest

from .exception import MyCustomException


def add(x, y):
    """ adds two numbers
    >>> add(5, 5)
    10
    >>> add(2, -6)
    -4
    >>> add(2, "hi") # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError:

    """
    if x > y:
        raise MyCustomException("Just fooling around")
    return x + y


if __name__ == "__main__":
    doctest.testmod(verbose=True)
