class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def get_nth_from_end(head, n):
    first = head
    second = head

    # Move first pointer n steps ahead
    for _ in range(n):
        if not first:
            return None  # n is greater than the number of nodes
        first = first.next

    # Move both pointers until first reaches the end
    while first:
        first = first.next
        second = second.next

    return second.data

# Helper function to create a linked list
def create_linked_list(elements):
    head = Node(elements[0])
    current = head
    for item in elements[1:]:
        current.next = Node(item)
        current = current.next
    return head

# Example usage
elements = [10, 20, 30, 40, 50]
head = create_linked_list(elements)
n = 2
print(f"{n}th node from end is:", get_nth_from_end(head, n))
