numbers = [10, 20, 30, 40]


def build_prefix_sum(numbers):
    prefix = []
    running_total = 0
    for num in numbers:
        running_total += num
        prefix.append(running_total)

    return prefix

def range_sum(prefix, left, right):

    if left == 0:
        return prefix[right]
    return prefix[right] - prefix[left - 1]


prefix = build_prefix_sum(numbers)
print(prefix)

left, right = 0, 0
print(range_sum(prefix, left, right))

print(range_sum(prefix, 1, 3))
print(range_sum(prefix, 0, 2))
print(range_sum(prefix, 2, 2))
