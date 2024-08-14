def first_non_repeating_char(string):
    dict1 = {}
    for ch in string:
        dict1[ch] = dict1.get(ch,0) + 1 
    
    for ch in string:
        if dict1[ch] == 1:
            return ch



print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )

