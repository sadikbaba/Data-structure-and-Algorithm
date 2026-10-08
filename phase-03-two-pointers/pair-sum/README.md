# Pair Sum Using Two Pointers

Find two numbers in a sorted array whose sum equals a target.

## Example

```text
numbers = [1, 3, 5, 7, 9]
target = 12

result = (3, 9)
```

## Approach

- `left` starts at the beginning.
- `right` starts at the end.
- Add the two values.
- If the sum equals the target, return the pair.
- If the sum is too small, move `left` right.
- If the sum is too large, move `right` left.
- Stop when the pointers meet or cross.

## Why Two Pointers Work

The array is sorted.

Moving `left` right increases the sum.

Moving `right` left decreases the sum.

This avoids checking every possible pair with nested loops.

## Complexity

- Time: O(n)
- Extra space: O(1)

## Edge Cases Tested

- Pair exists
- Pair does not exist
- Empty array
- One element
- Duplicate values