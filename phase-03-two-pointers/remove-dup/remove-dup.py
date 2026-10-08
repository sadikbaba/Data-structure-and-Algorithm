# Brute force solution that checks every pair.
def remove_duplicates_brute_force(numbers):
    unique = []

    for number in numbers:
        duplicate = False

        for saved_number in unique:
            if number == saved_number:
                duplicate = True
                break

        if not duplicate:
            unique.append(number)

    return unique


numbers = [1, 1, 2, 2, 3]
print(remove_duplicates_brute_force(numbers))




## Remove duplicates in place using fast and slow pointers.
def remove_duplicates(numbers):
    if not numbers:
        return 0

    slow = 0

    for fast in range(1, len(numbers)):
        if numbers[fast] != numbers[slow]:
            slow += 1
            numbers[slow] = numbers[fast]

    return slow + 1


numbers = [1, 1, 2, 2, 3]

unique_count = remove_duplicates(numbers)

print(numbers[:unique_count])


print("edge cases")

numbers = []
unique_count = remove_duplicates(numbers)
print(numbers[:unique_count])       # []

numbers = [1]
unique_count = remove_duplicates(numbers)
print(numbers[:unique_count])       # [1]

numbers = [1, 1, 1, 1]
unique_count = remove_duplicates(numbers)
print(numbers[:unique_count])       # [1]

numbers = [1, 2, 3, 4]
unique_count = remove_duplicates(numbers)
print(numbers[:unique_count])       # [1, 2, 3, 4]