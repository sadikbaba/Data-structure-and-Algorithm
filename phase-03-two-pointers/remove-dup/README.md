# Remove Duplicates from Sorted Array

Remove duplicate values from a sorted array in place.

## Example

```text
[1, 1, 2, 2, 3]
```

Useful part after processing:

```text
[1, 2, 3]
```

## Approach

- `fast` scans through every value.
- `slow` tracks the last unique value kept.
- If `numbers[fast]` is different from `numbers[slow]`, a new unique value was found.
- Move `slow` forward.
- Copy the new unique value into that position.

## Complexity

- Time: O(n)
- Extra space: O(1)

## Edge Cases Tested

- Empty list
- One element
- All duplicates
- No duplicates
- Normal mixed duplicates