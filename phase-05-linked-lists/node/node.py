class Node:
    def __init__(self, value):
        self.value = value
        self.next = None






first_node = Node(5)
second_node = Node(10)
third_node = Node(15)
first_node.next = second_node
second_node.next = third_node




def traverse(head):
    current = head

    while current is not None:
        print(current.value)
        current = current.next


# print(first_node.value)        # 5
# print(first_node.next.value)   # 10
# print(first_node.next.next.value)  # 15

# print(first_node.next.next.next)  # None

traverse(first_node)