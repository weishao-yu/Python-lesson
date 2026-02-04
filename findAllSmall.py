def findAllSmall(lst, s):
    new_lst = [num for num in lst if num < s]
    print(new_lst)
    return new_lst

findAllSmall([1, 2, 3], 10)  # returns [1, 2, 3]
findAllSmall([1, 2, 3], 2)   # returns [1]
findAllSmall([1, 3, 5, 4, 2], 4)  #  returns [1, 3, 2]