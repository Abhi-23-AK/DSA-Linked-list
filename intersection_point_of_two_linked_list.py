class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None

    ptr1 = headA
    ptr2 = headB

    # Loop until both pointers are equal or None
    while ptr1 != ptr2:
        ptr1 = ptr1.next if ptr1 else headB
        ptr2 = ptr2.next if ptr2 else headA

    return ptr1  # Can be the intersection node or None

# Helper to print linked list
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Example creation with intersection
# List A: 1 -> 2 -> 3 \
#                      -> 6 -> 7
# List B:       4 -> 5 /

# Common part
common = Node(6)
common.next = Node(7)

# List A
headA = Node(1)
headA.next = Node(2)
headA.next.next = Node(3)
headA.next.next.next = common

# List B
headB = Node(4)
headB.next = Node(5)
headB.next.next = common

# Print both lists
print("List A:")
print_list(headA)
print("List B:")
print_list(headB)

# Find intersection
intersection = get_intersection_node(headA, headB)

# Output
if intersection:
    print(f"Intersection at node with value: {intersection.data}")
else:
    print("No intersection found.")
