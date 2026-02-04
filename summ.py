def summ(lst):
    total = 0
    if lst:
        for num in lst:
            total += num
    print(total)
    return total
summ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # returns 55
summ([])  # return 0
summ([-10, -20, -30])  # return -60