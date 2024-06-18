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

    def reverse(self):
        if self.head == None:
            return None
        if self.head == self.tail:
            return True
        else:
            temp = self.head
            pre = None
            after = temp.next
            for _ in range(self.length):
                temp.next = pre
                temp.prev = after
                pre = temp
                temp = after
                if after != None:
                    after = after.next
            self.head,self.tail = self.tail,self.head
            




