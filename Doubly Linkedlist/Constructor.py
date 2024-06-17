class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None
        

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1