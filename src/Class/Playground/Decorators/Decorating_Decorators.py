import functools
import time
import time
# def hello():
#     return "Hello World"


def power(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        print("I am a before decorator")
        f = func(*args, **kwargs)
        print("I am after decorator")
        return f

    return wrap


def performance_counter(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func = f(*args, **kwargs)
        end = time.perf_counter()
        print(f"The function {f.__name__} took {end - start} to run")
        return func

    return wrapper


@power
def hello(name):
    return f"{name} Hello World"


hello("Lotus")


@performance_counter
@power
def add(x, y):
    """
add two numbers
    """
    return x + y


add(1, 2)


print(add.__name__)
print(add.__doc__)


def multiply(a, b):
    return (a * b)


multiply_by_5 = functools.partial(multiply, 5)
print(multiply_by_5(6))








# hello = decorate(hello)
