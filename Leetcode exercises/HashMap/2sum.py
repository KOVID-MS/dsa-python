def two_sum(nums,target):
    dict1 = {}
    res = []
    
    for i in range(len(nums)):
        if (target-nums[i]) in dict1.keys():
            res.append(dict1[target-nums[i]])
            res.append(i)
            return res
        else:
            dict1[nums[i]] = i
    return res
            
    
    
    
print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9))  
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
print(two_sum([1, 3, 5, 7, 9], 10))  
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )




