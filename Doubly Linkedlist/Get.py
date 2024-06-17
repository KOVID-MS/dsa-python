
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

    def get(self,index):
        temp = self.head
        if index < 0 or index >= self.length:
            return None
        if index <= self.length /2:
            for _ in range(index):
                temp = temp.next
        if index > self.length/2:
            temp = self.tail
            for _ in range(self.length-index-1):
                temp = temp.prev
        return temp
