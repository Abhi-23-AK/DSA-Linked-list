class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reorder_list(head):
    if not head or not head.next:
        return

    # Step 1: Find the middle
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse second half
    prev, curr = None, slow.next
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    slow.next = None  # Split the list

    # Step 3: Merge two halves
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2

# Helper Functions
def create_list(arr):
    head = Node(arr[0])
    curr = head
    for num in arr[1:]:
        curr.next = Node(num)
        curr = curr.next
    return head

def print_list(head):
    while head:
        print(head.val, end=" → ")
        head = head.next
    print("None")

# Example
head = create_list([1, 2, 3, 4, 5])
print("Original List:")
print_list(head)

reorder_list(head)

print("Reordered List:")
print_list(head)
