def subarray_sum(nums,target):
    dict1 = {0:-1}
    temp = 0
    for i in range(len(nums)):
        temp += nums[i]
        
        if temp - target in dict1.keys():
            return [dict1[temp-target]+1,i]
        else:
            dict1[temp] = i
    return []
 


nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )

