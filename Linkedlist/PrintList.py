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

    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next
    

my_linked_list = Linkedlist(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.print_list()