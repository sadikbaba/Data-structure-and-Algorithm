class SupportQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, ticket):
        self.in_stack.append(ticket)

    def dequeue(self):
        if self.is_empty():
            return None

        # Move items only when out_stack is empty
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        return self.out_stack.pop()   # call the method

    def peek(self):
        if self.is_empty():
            return None

        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        return self.out_stack[-1]

    def is_empty(self):
        return len(self.in_stack) == 0 and len(self.out_stack) == 0


if __name__ == "__main__":
    queue = SupportQueue()

    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")

    print(queue.dequeue())  # A

    queue.enqueue("D")

    print(queue.peek())     # B
    print(queue.dequeue())  # B
    print(queue.dequeue())  # C
    print(queue.dequeue())  # D
    print(queue.is_empty()) # True