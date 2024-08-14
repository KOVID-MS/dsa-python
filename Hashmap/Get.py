class Hashmap:
    def __init__(self,size = 7) :
        self.data_map = [None] * size
    
    def gethash(self,key):
        index = 0
        for ch in key:
            index = (index + ord(ch)*23) % len(self.data_map)
        
        return index
    
    def printhash(self):
        for key,value in enumerate(self.data_map):
            print(key , value)

    def set_item(self,key,value):
        index = self.gethash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get_item(self,key):
        index = self.gethash(key)
        if self.data_map[index] == None:
            return False
        for i in range(len(self.data_map[index])):
            if self.data_map[index][i][0] == key:
                return True
        return False    

hash = Hashmap()
hash.set_item("a",1)
hash.set_item("b",2)
print(hash.get_item("b"))
hash.printhash()


