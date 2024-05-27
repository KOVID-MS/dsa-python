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

my_linked_list = Linkedlist(4)

print("Head value : ", my_linked_list.head.value)
print("Tail value : ", my_linked_list.tail.value)
print("Length : ", my_linked_list.length)