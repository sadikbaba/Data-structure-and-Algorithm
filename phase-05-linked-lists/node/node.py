class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def traverse(head):
    current = head

    while current is not None:
        print(current.value)
        current = current.next

def insert_at_beginning(head, value):
    # create a new node
    new_node = Node(value)
    # connect it to the head
    new_node.next = head
    # make the head point to the new node
    head = new_node
    return head

def insert_at_end(head, value):

  
    # create a new node
    new_node = Node(value)

    if head is None:
            return new_node
    
    # traverse the linked list to find the last node
    current = head
    while current.next is not None:
        current = current.next
    # connect the new node to the last node
    current.next = new_node
    return head

def delete_value(head, value):
    if head is None:
        return None

    if head.value == value:
        return head.next

    current = head

    while current.next is not None:
        if current.next.value == value:
            current.next = current.next.next
            return head

        current = current.next

    return head


first_node = Node(5)
second_node = Node(10)
third_node = Node(15)
first_node.next = second_node
second_node.next = third_node



new_head = insert_at_beginning(first_node, 20)
print("\n")
head = insert_at_end(new_head, 25)
traverse(head)

print("\n")
traverse(new_head)
new_head = delete_value(new_head, 10)

print("After delete:")
traverse(new_head)