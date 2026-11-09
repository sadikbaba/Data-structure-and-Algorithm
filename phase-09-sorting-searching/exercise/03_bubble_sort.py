def bubble_sort(numbers):

    n = len(numbers)

    for i in range(n):
        for j in range( n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j+ 1] = numbers[j+ 1], numbers [j]

                swapped = True
        if not swapped:
            break
    return numbers



if __name__ == "__main__":

    numbers = [5, 3, 8, 2, 1]
    print(bubble_sort(numbers))
    # [1, 2, 3, 5, 8]





