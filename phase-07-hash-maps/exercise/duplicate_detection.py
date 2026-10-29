def find_duplicates(transactions):
    seen = set()
    count = set()
    dup = []
    for txn in transactions:
        if txn in seen:
            if txn not in count:
                count.add(txn)
                dup.append(txn)
        else:
            seen.add(txn)
           

    return  dup

if __name__ == "__main__":
    tests = [
        ([101, 102, 103, 102, 104, 101], [102, 101]),
        ([1, 2, 3], []),
        ([5, 5, 5], [5]),
        ([], []),
    ]

    for transactions, expected in tests:
        result = find_duplicates(transactions)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} | input={transactions}")
        print(f"       expected={expected}")
        print(f"       got     ={result}\n")