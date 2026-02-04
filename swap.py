def swap(n):
    s = ""
    for i in n:
        if i.isupper():
            i = i.lower()
        else:
            i = i.upper()
        s += i
    print(s)
    return s
    
swap("Hello")  # returns "hELLO"