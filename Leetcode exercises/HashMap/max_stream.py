nums = [1,2,3,5,5,6,3]
res=[0]*len(nums)
dic = {}
maximum = nums[0]
for i in range(len(nums)):
    if nums[i] > maximum:
        maximum = nums[i]
        dic[i] = nums[i]
    else:
        dic[i] = maximum
    
print(dic)
for key,value in dic.items():
    res[key] = value

print(res)