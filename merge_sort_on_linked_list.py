class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Merge two sorted linked lists (same as earlier)
def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return dummy.next

# Find the middle node using fast and slow pointers
def get_middle(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    if prev:
        prev.next = None  # split the list into two halves
    return slow

# Merge Sort function
def merge_sort(head):
    if not head or not head.next:
        return head

    middle = get_middle(head)
    left = merge_sort(head)
    right = merge_sort(middle)

    return merge_sorted_lists(left, right)

# Helper functions
def create_linked_list(elements):
    head = Node(elements[0])
    current = head
    for val in elements[1:]:
        current.next = Node(val)
        current = current.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Example usage
arr = [4, 2, 5, 1, 3]
head = create_linked_list(arr)

print("Original Linked List:")
print_linked_list(head)

sorted_head = merge_sort(head)

print("Sorted Linked List:")
print_linked_list(sorted_head)
