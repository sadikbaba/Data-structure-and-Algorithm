# Phase 2: Arrays and Strings

This phase strengthens array and string fundamentals and introduces common problem-solving patterns.

## Topics

- Indexing, traversal, insertion, deletion, searching, and updating
- Array operation complexity
- Counting and frequency tracking
- Prefix sums
- In-place modification
- Reversing and rotation
- Strings, substrings, character counting, and palindromes

## Problems

- [x] `reverse-array`
- [ ] `prefix-sum`
- [ ] `palindrome`
- [ ] `group-anagrams`

## Current Progress

### Reverse Array In Place

Learned how to reverse the original array without creating another array.

Approach:

- Use `left` and `right` indexes.
- Swap values from opposite ends.
- Move both indexes toward the middle.
- Stop when they meet or cross.

Complexity:

- Time: O(n)
- Extra space: O(1)

Edge cases tested:

- Empty array
- One element
- Even number of elements
- Odd number of elements

## Goal

Recognize when to use in-place modification, prefix sums, or frequency counting before writing code.