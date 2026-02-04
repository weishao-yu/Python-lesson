def findMin(lst):
    min_ele = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < min_ele:
            min_ele = lst[i]
    return min_ele

def my_sort(mylist):
    new_lst = []
    while mylist:
        min_ele = findMin(mylist)
        new_lst.append(min_ele)
        mylist.remove(min_ele)
    print(new_lst)  
    return new_lst

my_sort([17, 0, -3, 2, 1, 0.5]); # returns [-3, 0, 0.5, 1, 2, 17]