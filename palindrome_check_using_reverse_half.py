class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Helper to reverse a linked list
def reverse_list(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev

# Palindrome check function
def is_palindrome(head):
    if not head or not head.next:
        return True

    # Step 1: Find middle
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse second half
    second_half = reverse_list(slow)

    # Step 3: Compare halves
    first_half = head
    temp = second_half
    while temp:
        if first_half.data != temp.data:
            return False
        first_half = first_half.next
        temp = temp.next

    # (Optional Step 4: Restore list if needed)
    reverse_list(second_half)

    return True

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
arr = [1, 2, 3, 2, 1]
head = create_linked_list(arr)

print("Linked List:")
print_linked_list(head)

if is_palindrome(head):
    print("Result: The linked list is a palindrome.")
else:
    print("Result: The linked list is NOT a palindrome.")
