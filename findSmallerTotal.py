def find_smaller_total(lst, s):
    total = 0
    for num in lst:
        if num < s:
            total += num
    print(total)
    return total

find_smaller_total([1, 2, 3], 3) # returns 3
find_smaller_total([1, 2, 3], 1) # returns 0
find_smaller_total([3, 2, 5, 8, 7], 999) # returns 25
find_smaller_total([3, 2, 5, 8, 7], 0) # returns 0