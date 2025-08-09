class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

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

    def delete_front(self):
        if not self.head:
            print("List is empty.")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_end(self):
        if not self.head:
            print("List is empty.")
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

# Usage
dll = DoublyLinkedList()
dll.insert_end(10)
dll.insert_front(5)
dll.insert_end(20)
dll.insert_front(1)

print("After insertions:")
dll.display()

dll.delete_front()
dll.delete_end()

print("After deletions:")
dll.display()
