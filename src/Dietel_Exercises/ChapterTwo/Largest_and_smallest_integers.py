max_num = 0
min_num = 101
lst = []


def comparison():
    global min_num, max_num
    if numbers < min_num:
        min_num = numbers
    if numbers > max_num:
        max_num = numbers


for i in range(5):
    for j in range(5):
    numbers = int(input(f"Please Enter a number {i + 1} --> "))
    print(numbers)
    comparison()


print(f"The 5 Numbers entered are {lst}")
print(f"The Minimum value of the values entered is {min_num}")
print(f"The Minimum value of the values entered is {max_num}")
