# Prefix Sum

A prefix sum stores the running total of an array.

Example:

```text
numbers = [10, 20, 30, 40]
prefix  = [10, 30, 60, 100]
```

## Range Sum

To get the sum from `left` to `right`:

```text
prefix[right] - prefix[left - 1]
```

If `left == 0`:

```text
prefix[right]
```

Example:

```text
Range 1 to 3

100 - 10 = 90
```

## Complexity

Building the prefix sum:

- Time: O(n)
- Extra space: O(n)

Range query:

- Time: O(1)
- Extra space: O(1)

## Edge Cases Tested

- Range starts at index 0
- Range contains one element
- Normal range