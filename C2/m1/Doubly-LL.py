class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtStart(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insertAtPosition(self, data, position):
        if position == 0:
            self.insertAtStart(data)
            return
        new_node = Node(data)
        current = self.head
        while current and position > 1:
            current = current.next
            position -= 1
        if current is None:
            print("Position out of bounds")
            return
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def printLL(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next


llist = DoublyLinkedList()

# add nodes to the linked list
llist.insertAtEnd("a")
llist.insertAtEnd("b")
llist.insertAtStart("c")
llist.insertAtEnd("d")
llist.insertAtPosition("g", 2)

# print the linked list
print("Node Data:")
llist.printLL()
