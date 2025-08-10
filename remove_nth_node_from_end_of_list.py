class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    fast = slow = dummy

    # Move fast ahead by n + 1 to maintain the gap
    for _ in range(n + 1):
        fast = fast.next

    # Move both fast and slow until fast reaches the end
    while fast:
        fast = fast.next
        slow = slow.next

    # Remove nth node
    slow.next = slow.next.next
    return dummy.next

# Helper functions for testing
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

def create_list(arr):
    head = Node(arr[0])
    temp = head
    for val in arr[1:]:
        temp.next = Node(val)
        temp = temp.next
    return head

# Usage
head = create_list([1, 2, 3, 4, 5])
print("Original List:")
print_list(head)

new_head = remove_nth_from_end(head, 2)
print("After Removing 2nd Node from End:")
print_list(new_head)
