class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.data

# Helper function to create a linked list
def create_linked_list(elements):
    head = Node(elements[0])
    current = head
    for item in elements[1:]:
        current.next = Node(item)
        current = current.next
    return head

# Example usage
elements = [1, 2, 3, 4, 5]
head = create_linked_list(elements)
print("Middle node is:", find_middle(head))
