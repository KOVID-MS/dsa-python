def longest_consecutive_sequence(nums):

    set1 = set(nums)
    length = 0
    for x in set1:
        if x+1 not in set1:
            temp = 1
            temp2 = x
        
            while(temp2-1 in set1):
                temp += 1
                temp2 -= 1
            length = max(length,temp)
    return length


print( longest_consecutive_sequence([100,99, 4, 200, 1, 3, 2]) )
