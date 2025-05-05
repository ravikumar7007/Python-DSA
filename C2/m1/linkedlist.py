class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self, data):
        if self.head is None:
            self.insertAtBegin(data)
            return
        new_node = Node(data)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBegin(data)
            return
        pos = 0
        curr = self.head

        while curr and pos < index - 1:
            pos += 1
            curr = curr.next
        if curr:
            new_node = Node(data)
            new_node.next = curr.next
            curr.next = new_node
        else:
            print("Index out of bounds")

    def updateAtIndex(self, data, index):
        pos = 0
        curr = self.head

        while curr and pos < index:
            pos += 1
            curr = curr.next
        if curr:
            curr.data = data
        else:
            print("Index out of bounds")

    def remove_first(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    def remove_last(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        curr = self.head
        while curr.next and curr.next.next:
            curr = curr.next
        curr.next = None

    def remove_at_index(self, index):
        if self.head is None:
            print("List is empty")
            return
        if index == 0:
            self.remove_first()
            return
        pos = 0
        curr = self.head

        while curr and pos < index - 1:
            pos += 1
            curr = curr.next
        if curr and curr.next:
            curr.next = curr.next.next
        else:
            print("Index out of bounds")

    def remove_node(self, data):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next and curr.next.data != data:
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next
        else:
            print("Node not found")

    def sizeofLL(self):
        size = 0
        curr = self.head
        while curr:
            size += 1
            curr = curr.next
        return size

    def printLL(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next


# create a new linked list
llist = LinkedList()

# add nodes to the linked list
llist.insertAtEnd("a")
llist.insertAtEnd("b")
llist.insertAtBegin("c")
llist.insertAtEnd("d")
llist.insertAtIndex("g", 2)

# print the linked list
print("Node Data:")
llist.printLL()

# remove nodes from the linked list
print("\nRemove First Node:")
llist.remove_first()
llist.printLL()

print("\nRemove Last Node:")
llist.remove_last()
llist.printLL()

print("\nRemove Node at Index 1:")
llist.remove_at_index(1)
llist.printLL()

# print the linked list after all removals
print("\nLinked list after removing a node:")
llist.printLL()

print("\nUpdate node Value at Index 0:")
llist.updateAtIndex("z", 0)
llist.printLL()

print("\nSize of linked list:", llist.sizeofLL())
