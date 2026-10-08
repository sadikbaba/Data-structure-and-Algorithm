from frequency_count import count_frequency


def signature(text):
    char_counts = count_frequency(text)
    sig = tuple(sorted(char_counts.items()))
    return sig


def group_anagrams(words):
    anagrams = {}

    for word in words:
        sig = signature(word)

        if sig in anagrams:
            anagrams[sig].append(word)
        else:
            anagrams[sig] = [word]

    return list(anagrams.values())


if __name__ == "__main__":
    # test cases
    text1 = "eat"
    text2 = "tea"

    print(signature(text1))
    print(signature(text2))

    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(words))

    print(group_anagrams([]))
    # expected: []

    print(group_anagrams(["a"]))
    # expected: [["a"]]

    print(group_anagrams(["ab", "ba"]))
    # expected: [["ab", "ba"]]

    print(group_anagrams(["abc", "def"]))
    # expected: [["abc"], ["def"]]

    print(group_anagrams(["", ""]))
    # expected: [["", ""]]
