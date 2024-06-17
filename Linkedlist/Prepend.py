class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def prepend(self,value):
        new_Node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_Node
        new_Node.next = self.head
        self.head = new_Node
        self.length +=1
