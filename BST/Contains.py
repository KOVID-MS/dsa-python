class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    
    def contains(self,value):
        temp = self.root
        while temp is not None:
            if temp.value < value:
                temp = temp.right
            elif temp.value > value:
                temp = temp.left
            else:
                return True
        return False
        
bst = BinarySearchTree()
bst.insert(10)
bst.insert(11)
bst.insert(13)
bst.insert(14)
bst.insert(15)

print(bst.contains(10))
print(bst.contains(15))
print(bst.contains(13))
print(bst.contains(9))
