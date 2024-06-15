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

    def print_list(self):
        if self.length == 0:
            print("List is empty")
        else:
            temp = self.head
            while temp != None:
                print(temp.value)
                temp = temp.next
            
    def append(self,value):
        new_Node = Node(value)
        if self.length == 0:
            self.head = new_Node
            self.tail = new_Node
        else:    
            self.tail.next = new_Node
            self.tail = self.tail.next
        self.length += 1

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



