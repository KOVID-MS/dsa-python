class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1
        
    def swap_pairs(self):
        if self.head == None:
            return None
        if self.head.next == None:
            return self.head
        else:
            temp = self.head
            self.head = temp.next
            while temp!= None and temp.next!= None:
                after = temp.next
                temp.next = after.next
                if after.next != None:
                    after.next.prev = temp
                after.prev = temp.prev
                if temp.prev != None:
                    temp.prev.next = after
                after.next = temp
                temp.prev = after
                
                temp = temp.next
        return self.head



