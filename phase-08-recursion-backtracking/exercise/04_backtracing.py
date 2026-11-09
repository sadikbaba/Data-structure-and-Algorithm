def backtracking(numbers) -> list:

    if len(numbers) > 2:
        return

    current = []
    result = []

    current.append(numbers[0])
    result.append(current.copy())

    current.append(numbers[1])
    result.append(current.copy())
    
    current.pop(0)
    result.append(current.copy())

    current.pop()
    result.append(current.copy())
  
    return result


def generate_subsets(items):
    results = []
    current = []

    def backtrack(index):
        # Base case: we've considered every item
        if index == len(items):
            results.append(current.copy())
            return

        # Choice 1: include the current item
        current.append(items[index])
        backtrack(index + 1)

        # Undo the choice
        current.pop()

        # Choice 2: exclude the current item
        backtrack(index + 1)

    backtrack(0)
    return results


def generate_permutations(items):
    results = []
    current = []

    def backtrack():
        # Have we arranged every item?
        if len(current) == len(items):
            results.append(current.copy())
            return

        # Try every available item
        for item in items:
            if item in current:
                continue

            # Choose
            current.append(item)

            # Explore
            backtrack()

            # Undo
            current.pop()

    backtrack()
    return results



if __name__ == "__main__":

    numbers = [1, 2,]
    print(backtracking(numbers))
    print("\n")
    print(generate_subsets(["A", "B"]))
    print("\n")
    print(generate_subsets(["A", "B", "C", ]))
    print("\n")
    print(generate_subsets(numbers))

    # permutations
    print("\n")
    print(generate_permutations(["A", "B", "C"]))
