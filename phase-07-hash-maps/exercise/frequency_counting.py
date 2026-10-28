def frequency(items):

    if len(items) == 0:
        return {}
    count = {}

    for i in items:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    return count


if __name__ == "__main__":
    numbers = [2, 3, 2, 4, 3, 2]
    print(frequency(numbers))

    networks = ["MTN", "Airtel", "MTN", "Glo", "Airtel", "MTN"]
    print(frequency(networks))

    empty = []
    print(frequency(empty))
