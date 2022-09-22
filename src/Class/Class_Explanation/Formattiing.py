import math

s = "Sorry, is this the {} minute {}? ". format(5, 'ARGUMENT')

print(s)

print("{} is {} years old".format("Bill", 25))
print(f"{'Bill'} is {math.pi * 100} years old")
s = f"Sorry, is this the {5} minute {'ARGUMENT'}? "
print("{:>10} is {:<5} years old".format("Bill", math.pi))
print("{:^10} is {:.2%} years old".format("Bill", math.pi * 100))

for i in range(1, 11):
    sym = '*' * i
    print('{:>10}'.format(sym))


for i in range(1, 11):
    sym = '*' * i
    print(f'{sym:>10}')
