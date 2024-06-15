class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self,start_index,end_index):
        if self.length == 0 or self.length == 1:
            return None
        start = self.head
        for _ in range(start_index):
            start = start.next
        while start_index <= end_index:
            temp = start
            for _ in range(end_index-start_index):
                temp = temp.next
            x = start.value
            start.value = temp.value
            temp.value = x
            start = start.next
            start_index += 1
            end_index -= 1
            