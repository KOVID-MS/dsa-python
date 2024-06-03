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

    def prepend(self,value):
        new_Node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_Node
        new_Node.next = self.head
        self.head = new_Node
        self.length +=1

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

print("Linked List before popping from front")
my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.print_list()
print("\nLinked List after popping from front")
Popped_element = my_linked_list.popfirst()
my_linked_list.print_list()
print("Popped_element is : ", Popped_element.value,"\n")

Popped_element = my_linked_list.popfirst()
my_linked_list.print_list()
print("Popped_element is : ", Popped_element.value, "\n")

Popped_element = my_linked_list.popfirst()
my_linked_list.print_list()
print("Popped_element is :", Popped_element.value)

