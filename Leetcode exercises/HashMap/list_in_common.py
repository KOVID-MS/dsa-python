def item_in_common(list1,list2):
    dict1 = {}
    for i in list1:
        dict1[i] = "True"
    
    for j in list2:
        if j in dict1.keys():
            return True
            
    return False
      
list1 = [1,3,5]
list2 = [2,4,5]

print(item_in_common(list1, list2))


