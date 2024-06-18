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

    def is_palindrome(self):
        if self.head == None:
            return True
        if self.head == self.tail:
            return True
        else:
            pre = self.head
            after = self.tail
            for _ in range(self.length//2):
                if pre.value == after.value:
                    pre = pre.next
                    after = after.prev
                else:
                    return False
            return True


