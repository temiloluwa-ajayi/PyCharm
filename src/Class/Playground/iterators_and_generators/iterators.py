lst = [1, 2, 3, 4, 5]
it = iter(lst)
print(it)
print(next(it))
print(next(it))
print(list(it))


# def custom_for(iterable):
#     it = iter(iterable)
#     while True:
#         try:
#             print(next(it))
#         except StopIteration:
#             print("End of loop")
#             return
#
#
# custom_for(lst)


def custom_for(iterable, func):
    it = iter(iterable)
    while True:
        try:
            func(next(it))
        except StopIteration:
            print("End of loop")
            return


custom_for(lst, print)

