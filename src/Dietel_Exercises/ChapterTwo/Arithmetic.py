x = int(input("Enter the First Value::-->:: "))
a = int(input("Enter the Second Value::-->:: "))


def sum_of_numbers(u, z):
    answer = u + z
    print(f"The Sum of the two values {u} and {z} is {answer}")
    return answer


def sum_of_squares(u, z):
    answer = (u ** 2) + (z ** 2)
    print(f"The Sum of the Square of {u} and {z} is {answer}")
    return answer


def difference_of_squares(u, z):
    answer = (u ** 2) - (z ** 2)
    print(f"The Difference of the Square of {u} and {z} is {answer}")
    return answer


sum_of_numbers(x, a)
sum_of_squares(x, a)
difference_of_squares(a,x)
