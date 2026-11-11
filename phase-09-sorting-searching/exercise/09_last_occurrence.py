def last_occurrence(numbers, target):
    left = 0
    right = len(numbers) - 1
    result = None

    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            result = mid
            left = mid + 1          # keep searching right for a later occurrence
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result if result is not None else -1


if __name__ == "__main__":
    tests = [
        [1, 2, 4, 4, 4, 7, 9],
        [2, 2, 2, 2, 5],
        [1, 3, 5, 7],
        [1, 3, 5, 7],
        []
    ]
    targets = [4, 2, 5, 4, 4]
    expected = [4, 3, 2, -1, -1]

    results = [last_occurrence(test, target) for test, target in zip(tests, targets)]

    print("Results :", results)
    print("Expected:", expected)
    print("Pass    :", results == expected)