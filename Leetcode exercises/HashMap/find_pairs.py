def find_pairs(list1,list2,target):
    res = []
    set2 = set(list2)
    for num in list1:
        temp = target - num
        if temp in set2:
            res.append((num,target-num))
    return res



arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)
