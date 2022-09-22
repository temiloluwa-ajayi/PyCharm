# iterable = list[1, 2, 3, 4, 5, 4, 3, 2, 1, 8, 9, 9, 1]
# iterable = list["1", "2", "3", "4", "5", "4", "3", "2", "1", "8", "9", "9", "1"]
#
# for key, value in iterable.items():
#     print(f"{key} -------------------> {value}")
# iterable = list[1, 2, 3, 4, 5, 4, 3, 2, 1, 8, 9, 9, 1]
#
# # print (counter("1", "2", "3", "4", "5", "4", "3", "2", "1", "8", "9", "9", "1"))
# #     print (counter("1", "2", "3", "4", "5", "4", "3", "2", "1", "8", "9", "9", "1"))
# # TypeError: counter() takes 1 positional argument but 13 were given
def counter(iterable: list | str | tuple) -> dict:
    item_dict = {}
    for item in iterable:
        if item in item_dict:
            item_dict[item] += 1
        else:
            item_dict[item] = 1
    return item_dict
print (counter("hello"))


def counter(iterable: list | str | tuple) -> dict:
    item_dict = {}
    for item in iterable:
        item_dict[item] = item_dict.get(item, 0) + 1
    return item_dict
print (counter("hello"))


def counter(iterable: list | str | tuple) -> dict:
    item_dict = {}
    for item in iterable:
        item_dict[item] = iterable.count(item)
    return item_dict
print (counter("hello"))



# def counter(iterable: list | str | tuple) -> dict:
#     from collections import Counter
#     return (counter(iterable))
# print (counter("hello"))


def counter(iterable: list | str | tuple) -> dict:
    from collections import Counter, defaultdict
    item_dict = defaultdict(int)
    for item in iterable:
        item_dict[item] += 1
    return (dict(item_dict))
print (counter("hello"))