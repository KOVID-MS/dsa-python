class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def reverse(self):
        if self.length == 0:
            return False
        if self.length == 1:
            return True
        else:
            before = None
            temp = self.head
            self.head = self.tail
            self.tail = temp
            after = temp.next
            for _ in range(self.length):
                temp.next = before
                before = temp
                temp = after
                if(after):
                   after = temp.next
    
           
