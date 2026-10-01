# Use two indexes from opposite ends and swap until they meet.

def reverse_array(numbers):
    # Reverse the array in place.
    left = 0 
    right = len(numbers) - 1

    while left < right:
        numbers[left] , numbers[right] = numbers[right], numbers[left]
        left += 1
        right -= 1
    return numbers



numbers = [10, 20, 30, 40]
print(reverse_array(numbers))

numbers = [1, 2, 3, 4, 5]
print(reverse_array(numbers))

numbers = []
print(reverse_array(numbers))


numbers = [1]
print(reverse_array(numbers))

