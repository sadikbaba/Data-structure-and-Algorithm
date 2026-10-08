# Reverse String Using Two Pointers

Reverse a string using left and right pointers.

## Example

```text
"hello" -> "olleh"
```

## Approach

- Convert the string into a mutable list of characters.
- `left` starts at the beginning.
- `right` starts at the end.
- Swap the characters.
- Move both pointers toward the middle.
- Join the characters back into a string.

## Complexity

- Time: O(n)
- Extra space: O(n)

The extra space is O(n) because Python strings are immutable, so we create a list of characters and then create a new string.

## Edge Cases Tested

- Empty string
- One character
- Two characters
- Palindrome string
- Normal string