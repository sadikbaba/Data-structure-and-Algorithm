"LIFO means last in First out"

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    
    print(stack.peek()) # 5
    print(stack.size()) # 5
    print(stack.pop()) # 5
    print(stack.peek()) # 4
    print(stack.size()) # 4
    print(stack.pop()) # 4
    print(stack.peek()) # 3
    print(stack.size()) # 3
    print(stack.pop()) # 3
    print(stack.peek()) # 2
    print(stack.size()) # 2
    print(stack.pop()) # 2
    print(stack.peek()) # 1
    print(stack.size()) # 1
    print(stack.pop()) # 1
    print(stack.is_empty()) # True

