def binary_search(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50, 60]
    print(binary_search(numbers, 30))
    print(binary_search(numbers, 50))
    print(binary_search(numbers, 70))  # -1
    print(binary_search([], 30))  # -1
