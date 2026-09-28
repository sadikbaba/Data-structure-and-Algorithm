# Brute force:
# Compare each number with every number that comes after it.
# If two numbers are equal, a duplicate exists, so return True.
# If all pairs are checked without finding a duplicate, return False.
def contains_duplicate(numbers):

    for i in range(len(numbers)):
        
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                return True

    return False


print(contains_duplicate([4, 7, 2, 4, 9]))
print(contains_duplicate([1, 2, 3, 4]))
print(contains_duplicate([]))
print(contains_duplicate([0, 0, 0]))
print(contains_duplicate([-5]))


# edge cases
print("\nEdge Cases:")

print(contains_duplicate([1, 1]))
print(contains_duplicate([1, 2, 1]))
print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([-5, -5]))