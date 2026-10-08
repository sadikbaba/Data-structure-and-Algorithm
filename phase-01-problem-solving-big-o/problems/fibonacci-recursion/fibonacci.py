# Fibonacci is a sequence where each number is the sum of the two numbers
# before it. The sequence starts: 0, 1, 1, 2, 3, 5, 8, 13...
#
# This function takes an index n and returns the Fibonacci number
# at that index.
#
# Example:
# fibonacci(5) returns 5 because index 5 contains the value 5.
#
# This naive recursive solution is useful for learning recursion,
# but it is inefficient because it recalculates the same values many times.
# Time complexity: O(2^n)
# Space complexity: O(n)


def fibonacci(n):
    # Base cases: Fibonacci at index 0 is 0 and at index 1 is 1.
    if n <= 1:
        return n

    # Calculate the two previous Fibonacci numbers and add them.
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
print(fibonacci(10))


# Edge cases
print("\nEdge Cases:")
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))


# fibonacci(200) is intentionally not executed because
# this recursive solution takes an impractical amount of time.
