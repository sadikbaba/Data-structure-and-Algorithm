def max_sum_brute_force(nums, k):
    n = len(nums)
    if n < k:
        return None
    max_sum = 0
    for i in range(n - k + 1):
        window_sum = 0
        for j in range(i, i + k):
            window_sum += nums[j]
        if window_sum > max_sum:  # noqa: PLR1730
            max_sum = window_sum
    return max_sum




def max_sum_sliding_window(nums, k):
    n = len(nums)
    if n < k:
        return None

    window_sum =  sum(nums[:k])
    max_sum = window_sum
    for i in range(k, n):
        window_sum += nums[i] - nums[i - k]
        if window_sum > max_sum:  # noqa: PLR1730
            max_sum = window_sum
    return max_sum



numbers = [4, 2, 7, 1, 8]
k = 3
print(max_sum_brute_force(numbers, k))  
print(max_sum_sliding_window(numbers, k))
