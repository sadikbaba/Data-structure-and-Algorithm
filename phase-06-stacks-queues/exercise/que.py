from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.popleft()

    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    print(queue.peek())  # 1
    print(queue.dequeue())  # 1
    print(queue.peek())  # 2
    print(queue.dequeue())  # 2
    print(queue.peek())  # 3
    print(queue.dequeue())  # 3
    print(queue.peek())  # 4
    print(queue.dequeue())  # 4
    print(queue.peek())  # 5
    print(queue.dequeue())  # 5
