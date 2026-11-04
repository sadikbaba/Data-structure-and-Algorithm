def fibonacci(n):
    if n <= 1:
        return n
   
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    print(fibonacci(4))  # Output: 3
    print(fibonacci(5))  # Output: 5
    print(fibonacci(10))  # Output: 55
    print(fibonacci(15))  # Output: 610

    for n in range(11):
        print(f"Fibonacci of {n} is {fibonacci(n)}")