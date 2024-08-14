class Hashmap:
    def __init__(self,size = 7) :
        self.data_map = [None] * size
    
    def gethash(self,key):
        index = 0
        for ch in key:
            index = (index + ord(ch)*23) % len(self.data_map)
        
        return index
    

hash = Hashmap()
print(hash.gethash("letter"))
