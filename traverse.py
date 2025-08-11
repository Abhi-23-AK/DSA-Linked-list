def traverse(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
