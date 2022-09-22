cont = []
for i in range(1, 11):
    cont.append(i)
print(cont)


"\n"
cont = [num for num in range(1, 11)]
print(cont)


"\n"
for i in range(1, 11):
    cont.append(i**2)
print(cont)


"\n"
cont = [(num ** 2) for num in range(1, 11)]
print(cont)


"\n"
names = ['bimpe', 'Banke', 'abimbola', 'James', 'Olalekan', 'Racheal']
my_names = []
for name in names:
    if name.istitle():
        my_names.append(name)
print(my_names)


"\n"
names = ['bimpe', 'Banke', 'abimbola', 'Kelechi', 'James', 'Olalekan', 'Racheal']
my_names = [name for name in names if name.istitle()]
print(my_names)

#
# "\n"
# # names = ['bimpe', 'Banke', 'abimbola', 'Kelechi', 'James', 'Olalekan', 'Racheal']
# # my_names = [name for name in names if name.istitle()]
# input_names = [input(f"{i + 1}. Name? ") for i in range(5)]
# print(input_names)
#
#
# "\n"
# # names = ['bimpe', 'Banke', 'abimbola', 'Kelechi', 'James', 'Olalekan', 'Racheal']
# # my_names = [name for name in names if name.istitle()]
# number_of_times = int(input("How many names will you like to enter? "))
# input_names = [input(f"{i + 1}. Name? ") for i in range(number_of_times)]
# print(input_names)
#

"\n"
evens = [even for even in range(1, 11) if even % 2 == 0]
print(evens)


"\n\n"
even_squared_odd_cubed = [num ** 2 if num % 2 == 0 else num ** 3 for num in range(1, 11)]
print(even_squared_odd_cubed)

x_and_y = []
for x in range(1, 6):
    for y in range(1, 6):
        x_and_y. append((x, y))
    x_and_y = [(x, y) for x in range(1, 6) for y in range(1, 6)]
    # x_and_y = [(x, y) if x > y else (y, x) for x in range(1, 6) for y in range(1, 6)]
    # x_and_y = [(x ** 2 if x 2 == 0 else x, y) if x > y else (y, x) for x in range(1, 6) for y in range(1, 6)]
print(x_and_y)


listcomp = [num % 3 for num in range(1, 10)]
setcomp = {num % 3 for num in range(1, 10)}
dictcomp = {k : v for k, v in enumerate(range(1, 10))}
genexp = (num for num in range(1, 10))

print(type(listcomp), listcomp)
print(type(setcomp), setcomp)
print(type(dictcomp), dictcomp)
print(type(genexp), genexp)

print(next(genexp))
print(next(genexp))
print(next(genexp))
print(list(genexp))
print((i for i in range(1_000)))
print([i for i in range(1_000)])

for i in genexp:
    print(i)
    