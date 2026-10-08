


numbers = [1, 3, 5, 7, 9]
target = 12


def find_pair(numbers, target):
    
    left = 0
    right = len(numbers) - 1

    while left < right:
        if numbers[left] + numbers[right] == target:
            return numbers[left], numbers[right]
            
        elif numbers[left] + numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
            right -= 1

    return None

print(find_pair(numbers, target))
print(find_pair([1, 2, 3, 4, 5], 9))   # expected (4, 5)
print(find_pair([1, 2, 3, 4, 5], 20))  # expected None
print(find_pair([], 5))                 # expected None
print(find_pair([5], 10))               # expected None
print(find_pair([1, 1, 2, 3], 2))      # expected (1, 1)



