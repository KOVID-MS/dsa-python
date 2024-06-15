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

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next != None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def popfirst(self):
        if self.length == 0:
            print("Cannot Pop as list is empty")
            return None
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp
        
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
        
    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next
