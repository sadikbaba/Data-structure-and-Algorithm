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



if __name__ == "__main__":
    numbers = [1, 2]
    print(backtracking(numbers))


    print(generate_subsets(["A", "B"]))
    print(generate_subsets(["A", "B", "C"]))

    print(generate_subsets(numbers))
