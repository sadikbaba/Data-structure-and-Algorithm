def next_greater(numbers):
    if len(numbers) == 0:
        return []

    stack = []
    result = [None] * len(numbers)

    for index in range(len(numbers)):
        current = numbers[index]

        while stack and current > numbers[stack[-1]]:
            previous_index = stack.pop()
            result[previous_index] = current

        stack.append(index)

    return result


if __name__ == "__main__":
    numbers = [5, 2, 7, 1, 3, 6, 4]
    print(next_greater(numbers))

    numbers = [1, 2, 3, 4, 5]
    print(next_greater(numbers))