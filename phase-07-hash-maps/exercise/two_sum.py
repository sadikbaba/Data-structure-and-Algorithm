def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        current = nums[i]
        needed = target -  current
        if needed in seen:
            return [seen[needed], i]
        seen[current] = i
    return []



if __name__ == "__main__":

    nums = [2, 7, 11, 15]
    print(two_sum(nums, 9 ))