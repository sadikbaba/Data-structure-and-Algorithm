def insertion_sort(numbers): # [5, 3, 8, 2, 1]
    for i in range(1, len(numbers)): 
        current = numbers[i] 
        j = i - 1 
        while j >= 0 and numbers[j] > current: 
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = current

    return numbers


if __name__ == "__main__":
    numbers = [5, 3, 8, 2, 1]
    print(insertion_sort(numbers))   # [1, 2, 3, 5, 8]


