def remove_duplicates(my_list):
    new_list = set()
    if len(my_list) == 0:
        return []
    for num in my_list:
        new_list.add(num)
    return list(new_list)


my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
new_list = remove_duplicates(my_list)
print(new_list)
