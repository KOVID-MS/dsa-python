class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def swap_first_last(self):
        if self.length == 0:
            return None
        temp = self.head.value
        self.head.value = self.tail.value
        self.tail.value = temp


