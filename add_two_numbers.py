class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def add_two_numbers(l1, l2):
    dummy = Node(0)
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        sum = carry

        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        carry = sum // 10
        curr.next = Node(sum % 10)
        curr = curr.next

    return dummy.next

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
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example
l1 = create_list([2, 4, 3])  # represents 342
l2 = create_list([5, 6, 4])  # represents 465

print("First Number:")
print_list(l1)

print("Second Number:")
print_list(l2)

result = add_two_numbers(l1, l2)
print("Sum (as linked list):")
print_list(result)
