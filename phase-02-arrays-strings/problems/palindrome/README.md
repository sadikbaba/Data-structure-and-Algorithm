# Palindrome

A palindrome reads the same forward and backward.

Examples:

```text
"madam" -> palindrome
"level" -> palindrome
"python" -> not a palindrome
```

## Approach

- Start `left` at the beginning of the string.
- Start `right` at the end.
- Compare `text[left]` with `text[right]`.
- If they are different, return `False`.
- If they are the same, move both indexes toward the middle.
- If all pairs match, return `True`.

## Complexity

- Time: O(n)
- Extra space: O(1)

## Edge Cases Tested

- Empty string
- One character
- Two different characters
- Repeated characters
- Palindrome strings
- Non-palindrome strings