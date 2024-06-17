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
        
    def set_value(self,index,value):
        new_node = Node(value)
        temp = self.get(index)
        if temp != None:
            temp.value = value
            return True
        else:
            return False
