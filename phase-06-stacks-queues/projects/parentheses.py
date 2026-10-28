"Validate matched parentheses using a stack. Implement a queue using two stacks. Solve a basic monotonic-stack problem such as next greater element."


def is_valid_parentheses(text):
    stack = []

    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if len(stack) == 0:
                return False

            if (
                char == ")"
                and stack[-1] == "("
                or char == "}"
                and stack[-1] == "{"
                or char == "]"
                and stack[-1] == "["
            ):
                stack.pop()
            else:
                return False

    return stack == []


if __name__ == "__main__":
    print(is_valid_parentheses("()()[]{}"))
    print(is_valid_parentheses("()()"))
    print(is_valid_parentheses("()"))
    print(is_valid_parentheses("("))
    print(is_valid_parentheses(""))
    print(is_valid_parentheses(")("))
    print(is_valid_parentheses("())"))
    print(is_valid_parentheses("()[]{}"))
    print(is_valid_parentheses("{[()]}"))
    print(is_valid_parentheses("[({]})]"))
