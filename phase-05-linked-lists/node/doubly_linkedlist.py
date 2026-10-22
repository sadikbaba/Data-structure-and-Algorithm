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
        return slow.value

    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    

def merge_sorted(list_a, list_b):

    if list_a.head is None:
        return list_b
    if list_b.head is None:
        return list_a

    merged = DoublyLinkedList()
    
    current_a = list_a.head
    current_b = list_b.head

    while current_a is not None and current_b is not None:
        if current_a.value <= current_b.value:
            merged.append(current_a.value)
            current_a = current_a.next
        else:
            merged.append(current_b.value)
            current_b = current_b.next
    while current_a is not None:
        merged.append(current_a.value)
        current_a = current_a.next

    while current_b is not None:
        merged.append(current_b.value)
        current_b = current_b.next
    return merged

        


if __name__ == "__main__":
    # Test 1: Odd number of nodes
    linked_list = DoublyLinkedList()
    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(15)
    linked_list.append(20)
    linked_list.append(25)

    
    print("Odd list middle:", linked_list.find_middle())
    # Expected: 15

    # Test 2: Even number of nodes
    linked_list = DoublyLinkedList()
    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(15)
    linked_list.append(20)

    print("\n")
    print("Even list middle:", linked_list.find_middle())
    # Expected: 10
    # Your version returns the FIRST middle

    # Test 3: One node
    linked_list = DoublyLinkedList()
    linked_list.append(5)

    print("\n")
    print("Single node middle:", linked_list.find_middle())
    # Expected: 5

    # Test 4: Empty list
    linked_list = DoublyLinkedList()
    print("\n")
    print("Empty list middle:", linked_list.find_middle())
    # Expected: None

    # Test 1: No cycle
    linked_list = DoublyLinkedList()
    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(15)
    print("\n")
    print("No cycle:", linked_list.has_cycle())
    # Expected: False

    # Test 2: Has cycle
    linked_list = DoublyLinkedList()
    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(15)

    # Make 15 point back to 10
    linked_list.tail.next = linked_list.head.next
    print("\n")
    print("Has cycle:", linked_list.has_cycle())
    # Expected: True
    print("\n")

    list_a = DoublyLinkedList()
    list_a.append(1)
    list_a.append(4)
    list_a.append(7)

    list_b = DoublyLinkedList()
    list_b.append(2)
    list_b.append(3)
    list_b.append(8)

    merged = merge_sorted(list_a, list_b)
    
    print("Merged list:")
    merged.traverse_forward()

    # Test 3: Merge with empty list
    empty_list = DoublyLinkedList()

    merged = merge_sorted(empty_list, list_b)

    print("\n")
    print("Merge with empty list:")
    merged.traverse_forward()

