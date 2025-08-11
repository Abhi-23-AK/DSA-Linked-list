class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def display_forward(self):
        print("Forward Traversal:")
        temp = self.head
        last = None
        while temp:
            print(temp.data, end=" <-> ")
            last = temp
            temp = temp.next
        print("None")
        return last  # Return last node for backward traversal

    def display_backward(self, last_node):
        print("Backward Traversal:")
        temp = last_node
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

# Usage
dll = DoublyLinkedList()
dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_end(40)

last_node = dll.display_forward()
dll.display_backward(last_node)
