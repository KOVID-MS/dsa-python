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
    
    def keys(self):
        all_keys = []
        all_values = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
                    all_values.append(self.data_map[i][j][1])
        return all_keys

hash = Hashmap()
hash.set_item("a",1)
hash.set_item("b",2)

print(hash.get_item("b"))
print(hash.keys())
hash.printhash()


