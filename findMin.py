def findMin(lst):
    if lst:
        min = lst[0]
        for num in range(1, len(lst)):
            if lst[num] < min:
                min = lst[num]
        print(min)
        return min
    else:
        print("undefined")
        return None

findMin([1, 2, 5, 6, 99, 4, 5]); # returns 1
findMin([]); # returns undefined
findMin([1, 6, 0, 33, 44, 88, -10]); # returns -10