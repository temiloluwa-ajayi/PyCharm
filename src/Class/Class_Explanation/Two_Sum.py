def two_sum(arr: list, target: int) -> list:

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return [-1, -1]


int_list = [3, -1, 5, 4]
two_sum(int_list, 4)


