def merge_sorted(left, right):

    result = []
    i = 0
    j = 0


    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i +=1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

    



def merge_sort(numbers):

    if len(numbers) <= 1:
        return numbers

    # 2. Find midpoint

    mid = len(numbers) // 2

    # 3. Split into left and right
    left = numbers[:mid]
    right = numbers[mid:]

    # 4. Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)


    # 5. Merge the sorted halves
    return merge_sorted(left, right)


if __name__ == "__main__":

    left = [2, 6, 9]
    right = [1, 5, 8]
    print(merge_sorted(left, right))
    # [1, 2, 5, 6, 8, 9]

    numbers = [5, 3, 8, 2, 1, 9, 4]
    print(merge_sort(numbers))
    # [1, 2, 3, 4, 5, 8, 9]
