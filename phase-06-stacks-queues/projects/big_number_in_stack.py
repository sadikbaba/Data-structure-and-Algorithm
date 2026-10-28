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

    numbers = [4, 2, 6, 3, 5, 1]
    print(next_greater(numbers))
    print("\n")


def hours_until_higher_traffic(visitors):
    """
    For each hour, return how many hours until traffic is higher.
    Uses a monotonic decreasing stack. O(n) time, O(n) space.
    """
    n = len(visitors)
    result = [None] * n
    stack = []  # stores indices, visitors[stack] is decreasing

    for i in range(n):
        # While current traffic is higher than the traffic at stack top
        while stack and visitors[i] > visitors[stack[-1]]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index  # hours waited
        stack.append(i)

    return result


if __name__ == "__main__":
    tests = [
        ([100, 80, 120, 90, 110, 150], [2, 1, 3, 1, 1, None]),
        ([50, 60, 70], [1, 1, None]),
        ([100, 100, 120], [2, 1, None]),
        ([90, 80, 70], [None, None, None]),
        ([], []),
    ]

    for visitors, expected in tests:
        output = hours_until_higher_traffic(visitors)
        status = "PASS" if output == expected else "FAIL"
        print(f"{status} | input={visitors}")
        print(f"       expected={expected}")
        print(f"       got     ={output}\n")
