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

    def delete(self, value):

        #  a list is empty
        if self.head is None:
            return

        #  a list 5->10->15->None
        #   case 5
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:  # new node is None
                self.tail = None
            else:
                self.head.prev = None  # new node has no prev
            return

        #  a list 5->10->15->None
        # case we want to delete tail
        if self.tail.value == value:
            self.tail = self.tail.prev  # 10 becomes tail
            self.tail.next = (
                None  # 10 becomes tail and next should become none since we delete it.
            )
            return

        #  a list 5->10->15->None
        # case we want to delete 10
        current = self.head  # current is 5
        while current.next is not None:  # current.next.value is 10
            if current.next.value == value:  #  if we reach 10
                current.next = (
                    current.next.next
                )  # remove 10 by making 5 point directly to 15
                current.next.prev = current  # 15.prev = 5
                return
            current = current.next  # we move to next node

    def reverse(self):
        # list 5->10->15->None

        current = self.head

        self.tail = self.head

        while current is not None:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def find_middle(self):

        if self.head is None:
            return None

        slow = self.head
        fast = self.head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == "__main__":
    linked_list = DoublyLinkedList()

    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(15)
    linked_list.prepend(2)

    linked_list.traverse_forward()
    print("\n")
    linked_list.traverse_backward()
print("\nRe")
