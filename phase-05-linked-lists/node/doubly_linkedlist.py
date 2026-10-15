
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def traverse_forward(self):
        current = self.head

        while current is not None:
            print(current.value)
            current = current.next
    def traverse_backward(self):
        current = self.tail

        while current is not None:
            print(current.value)
            current = current.prev

    


if __name__ == "__main__":
    linked_list = DoublyLinkedList()

    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(15)
    linked_list.prepend(2)

    linked_list.traverse_forward()
    print("\n")
    linked_list.traverse_backward()