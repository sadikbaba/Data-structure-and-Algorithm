# factorial means multiplying positive integers by all the positive integers less than it.
#  For example, 5! = 5 * 4 * 3 * 2 * 1 = 120. The factorial of 0 is defined to be 1.

def factorial(n):
    # Base case: if n is 0, return 1
    if n == 0:
        return 1
    # Recursive case: multiply n by the factorial of (n - 1)
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(5))  # Output: 120
    print(factorial(0))  # Output: 1
    print(factorial(1))  # Output: 1
    print(factorial(3))  # Output: 6
    print(factorial(10))  # Output: 3628800