# Bottleneck:
# The brute-force solution compares each number with the numbers
# that come after it, causing many repeated comparisons.
#
# We can optimize this by using a set to store numbers we have
# already seen.
#
# Set membership checking is O(1) on average, so we can check
# whether a number was already seen without scanning the list.


def contains_duplicate(numbers):

    seen = set()

    for num in numbers:
        if num in seen:
            return True
        seen.add(num)

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
