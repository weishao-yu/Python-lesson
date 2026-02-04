def has_33(lst):
    for i in range(len(lst) - 1):
        if lst[i] == 3 and lst[i + 1] == 3:
            return True
    return False
print(has_33([1, 5, 7, 3, 3])) # True
print(has_33([])) # False
print(has_33([4, 3, 2, 1, 0])) # False