class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def traverse(self):
        current = self.head

        while current is not None:
            print(current.value)
            current = current.next

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def delete(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next

            if self.head is None:
                self.tail = None

            return

        current = self.head

        while current.next is not None:
            if current.next.value == value:
                if current.next == self.tail:
                    self.tail = current

                current.next = current.next.next
                return

            current = current.next

    def reverse(self):
        current = self.head
        previous = None

        # Old head becomes the new tail
        self.tail = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous


if __name__ == "__main__":
    linked_list = SinglyLinkedList()

    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(15)
    linked_list.prepend(20)
    linked_list.append(25)

    print("Original:")
    linked_list.traverse()

    linked_list.delete(10)

    print("\nAfter delete:")
    linked_list.traverse()

    linked_list.reverse()

    print("\nAfter reverse:")
    linked_list.traverse()
