def count_frequency(text):

    counts = {}

    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts


if __name__ == "__main__":
    text = "abba"
    print(count_frequency(text))

    text = "baba"
    print(count_frequency(text))

    text = ""
    print(count_frequency(text))
