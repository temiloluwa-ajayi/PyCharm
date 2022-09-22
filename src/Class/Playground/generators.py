import contextlib


@contextlib.contextmanager
def manage_context():
    print("Entering the context manager")
    yield 1
    print("Entering the context manager")


with manage_context() as one:
    print(one)

# class ContextManager:
#     def __enter__(self): # This function is what the opens a class
#         print("Entering the context manager")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):  # This function is what the closes a class
#         pass
#
#     def __call__(self, *args, **kwargs):  # This function is what makes the class a callable
#         print("hello")