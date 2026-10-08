# Group Anagrams

Group words that contain the same characters with the same character frequencies.

Example:

```text
["eat", "tea", "tan", "ate", "nat", "bat"]
```

Result:

```text
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

## Approach

1. Count the frequency of each character in a word.
2. Convert the frequency dictionary into a sorted tuple.
3. Use that tuple as the word's signature.
4. Words with the same signature belong to the same group.
5. Store each group in a dictionary.
6. Return only the grouped word lists.

Example signature:

```text
"eat" -> (('a', 1), ('e', 1), ('t', 1))
"tea" -> (('a', 1), ('e', 1), ('t', 1))
```

Because the signatures are equal, the words belong together.

## Complexity

Let:

```text
m = number of words
k = average word length
```

Time:

```text
O(m × k log k)
```

Extra space:

```text
O(m × k)
```

## Edge Cases Tested

- Empty list
- One word
- Two anagrams
- Words with no matching anagrams
- Empty strings

## Python Concepts Used

- Dictionaries
- `dict.items()`
- `dict.values()`
- `sorted()`
- Tuples
- Lists
- `if __name__ == "__main__"`