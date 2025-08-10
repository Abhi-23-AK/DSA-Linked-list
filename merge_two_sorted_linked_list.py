class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_sorted_lists(l1, l2):
    dummy = Node(0)  # dummy node to build the result list
    current = dummy

    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Attach the remaining part
    if l1:
        current.next = l1
    elif l2:
        current.next = l2

    return dummy.next

# Helper function to create linked list from list
def create_linked_list(elements):
    head = Node(elements[0])
    current = head
    for val in elements[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Example usage
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

l1 = create_linked_list(list1)
l2 = create_linked_list(list2)

print("Merged Sorted Linked List:")
merged_head = merge_sorted_lists(l1, l2)
print_linked_list(merged_head)
