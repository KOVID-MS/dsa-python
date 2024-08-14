def find_duplicates(nums):
    dict1 = {}
    result = []
    for i in nums:
        if i not in dict1.keys():
            dict1[i] = 1
        else:
            dict1[i] +=1
        
    for key in dict1.keys():
        if dict1[key] > 1:
            result.append(key)
            
    return result



print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )


