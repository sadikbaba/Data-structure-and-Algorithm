def first_occurrence(numbers, target):
    # Your implementation

    left = 0
    right = len(numbers) - 1

    result = None

    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            result =  mid
            right = mid -1
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if result is not None:
        return result
    return -1

if __name__ == "__main__":

    tests = [
        [1, 2, 4, 4, 4, 7, 9],
        [2, 2, 2, 2, 5],
        [1, 3, 5, 7], 
        [1, 3, 5, 7],
        []
    ]

    targets = [
       4,  2, 5, 4 ,4
    ]

    excepted = [
        2, 0, 2 ,-1,-1
    ]

    results = []
    for test, target in zip(tests, targets):
        results.append(first_occurrence(test, target))

    print(results)
    def check_result():
        all_results = []
        for result , exp in zip(results, excepted):
                all_results.append(result == exp)
        return all_results
            
    print(check_result())