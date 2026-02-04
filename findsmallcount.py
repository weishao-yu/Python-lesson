def find_small_count(lst, s):
    count = 0
    for num in lst:
        if num < s:
            count += 1
    print(count)
    return count

find_small_count([1, 2, 3, 4, 5], 0)
find_small_count([1, 2, 3], 2); # returns 1
