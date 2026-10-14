def min_subarray_length(nums, target):
    left = 0
    window_sum = 0
    min_length = float("inf")

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum >= target:
            window_length = right - left + 1
            min_length = min(min_length, window_length)

            window_sum -= nums[left]
            left += 1

    if min_length == float("inf"):
        return 0

    return min_length


numbers = [1, 2, 4]
target = 6

print(min_subarray_length(numbers, target))