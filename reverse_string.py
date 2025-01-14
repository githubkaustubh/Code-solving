class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev


def print_list(head):
    while head:
        print(head.data)  
        head = head.next
    print("None")


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

print("Original Linked List:")
print_list(node1)

reversed_head = reverse_linked_list(node1)
print("Reversed Linked List:")
print_list(reversed_head)
