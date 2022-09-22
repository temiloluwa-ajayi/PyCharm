import random

lst = list(range(1, 11))
print(lst)

random.shuffle(lst)
print(lst)

lst.append(20)
print(lst)

lst.append([20, 30, 40])
print(lst)

lst.extend([20, 30, 40])
print(lst)
# OR
lst += [20, 30, 40]
print(lst)

lst.insert(0, 56)
print(lst)

lst.insert(-1, 56)
print(lst)

last_item = lst.pop()
print(last_item)
print(lst)

item_at_index_0 = lst.pop()
print(item_at_index_0)
print(lst)

lst.remove(8)
print(lst)

# print("count", lst.count(8))
# lst.remove(8)
# print(lst)

print(lst.index(3))

lst.reverse()
print(lst)

lst.insert(0, [56, 10])
print(lst)

lst[0].reverse()
print(lst)

# s = "write a sentence and reverse it"
# s_list = s.split()


# lst.sort()
# print(lst)

# lst.sort(reverse=True)
# print(lst)

# del lst

# lst.clear()
# print(lst)