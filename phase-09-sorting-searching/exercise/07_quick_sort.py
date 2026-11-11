def partition(numbers, pivot):
    left = []
    right = []

    for n in numbers:
        if n < pivot:
            left.append(n)
        else:
            # if  n >= pivot:
              right.append(n)

    return left, right


def quick_sort(numbers):

    
    # 1. Base case
    if len(numbers) <= 1:
        return numbers
    
    result = []
    # 2. Choose a pivot
    pivot = numbers[ len(numbers) // 2]
 
    # 3. Remove the pivot from the remaining values
    remaining = numbers[1:]

    # 4. Partition the remaining values
    left, right = partition(remaining, pivot)

    # 5. Recursively sort both partitions
    left = quick_sort(left)
    right = quick_sort(right)

    # 6. Combine the results
    
    result.extend(left)
    result.append(pivot)
    result.extend(right)

    return result


if __name__ == "__main__":
    # numbers = [8, 3, 6, 2, 9, 1, 5]

    # left, right = partition(numbers, 5)

    # print(left)   # [3, 2, 1]
    # print(right)  # [8, 6, 9]

    # numbers = [5, 2, 5, 8, 3, 5]
    # pivot = 5
    # left, right = partition(numbers, pivot)
    # print(left)   
    # print(right)  

    print("\n quick sorted")
    tests =  [   [5, 3, 8, 2, 9],
    [8, 3, 6, 2, 9, 1, 5],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [4, 2, 4, 1, 2],
    [] , 
    [7] ]
    for test in tests:
        print(quick_sort(test))


