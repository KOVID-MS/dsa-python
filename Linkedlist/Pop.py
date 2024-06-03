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
        if self.length == 0:
            print(None)
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1

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

print("Before Popping \n")
my_linked_list = Linkedlist(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print("Linked List is :")
my_linked_list.print_list()

print("\nAfter Popping \n")
Popped_element = my_linked_list.pop()
print ("Popped Element is :",Popped_element.value)
print("Linked List is :")
my_linked_list.print_list()


