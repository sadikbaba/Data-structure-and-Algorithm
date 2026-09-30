## Recursion Complexity

Recursion is when a function calls itself with a smaller version of the problem until it reaches a base case.

### Patterns Practiced

#### Decrease by 1

Example: `countdown(n - 1)`

- Time: O(n)
- Space: O(n)
- The number of recursive calls grows linearly.
- Each unfinished call uses space on the call stack.

#### Divide by 2

Example: `halve(n // 2)`

- Time: O(log n)
- Space: O(log n)
- Each recursive call reduces the problem by half.
- The call stack grows with the number of halvings.

#### Branching Recursion

Example: naive recursive Fibonacci.

```python
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)