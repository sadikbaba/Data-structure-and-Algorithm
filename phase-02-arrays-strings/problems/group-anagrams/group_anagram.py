from frequency_count import count_frequency


def signature(text):
    char_counts = count_frequency(text)
    signature = tuple(sorted(char_counts.items()))
    return signature


def group_anagrams(words):
    anagrams = {}

    for word in words:
        sig = signature(word)

        if sig in anagrams:
            anagrams[sig].append(word)
        else:
            anagrams[sig] = [word]

    return anagrams




if __name__ == "__main__":
    # test cases
    text1  = "eat"
    text2 = "tea"

    print(signature(text1))
    print(signature(text2))

    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(words))