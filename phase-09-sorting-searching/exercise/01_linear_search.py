def linear_search(numbers, target):

    for n in range(len(numbers)):
        current = numbers[n]
        if current == target:
            return n
    return -1


if __name__ == "__main__":
    numbers = [12, 5, 8, 20, 3]

    print(linear_search(numbers, 20))  # 3
    print(linear_search(numbers, 100))  # -1
    print(linear_search([], 20))  # -1
