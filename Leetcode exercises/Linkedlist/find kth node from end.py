class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  
  
        
def find_kth_from_end(self,k):
    if k == 1:
        return self.tail
    else:
        slow = self.head
        fast = self.head
        for _ in range(k):
            if fast == None:
                return None
            fast = fast.next
        while fast != None:
            slow = slow.next
            fast = fast.next
        return slow
            





