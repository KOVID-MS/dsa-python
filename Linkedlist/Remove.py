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
        
    def remove(self,index):
        if index < 0 or index > self.length :
            return False
        if index == self.length-1 :
            return self.pop()
        if index == 0:
            return self.popfirst()
        else:
            temp = self.head
            pre = temp
            for _ in range(index):
                pre = temp
                temp = temp.next
            pre.next = temp.next
            temp.next = None
            self.length -= 1
            return temp

