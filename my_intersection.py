def my_intersection(lst1, lst2):
    return list(set(lst1).intersection(set(lst2)))

print(my_intersection([1, 3, 4, 6, 10], [5, 11, 4, 3, 100, 144, 0])) # returns [3, 4]

def my_intersection1(lst1, lst2):
    result = []
    for ele in lst1:
        if ele in lst2:
            result.append(ele)
    return result
print(my_intersection1([1, 3, 4, 6, 10], [5, 11, 4, 3, 100, 144, 0])) # returns [3, 4]