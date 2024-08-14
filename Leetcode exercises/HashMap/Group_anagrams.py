def hashing(key):
    index = 0;
    for i in key:
        index = (index + ord(i)) % 7
    return index
    
def group_anagrams(strings):
    result = []
    Hashmap = [None]*7
    for string in strings:
        index = hashing(string)
        if Hashmap[index] == None:
            Hashmap[index] = []
        Hashmap[index].append(string)
        
    for i in range(len(Hashmap)):
        if Hashmap[i] is not None:
            result.append(Hashmap[i])
    
    return result




print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )

