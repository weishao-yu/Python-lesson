def factorPrime(n):
    result = str(n) + " = "
    p = 2
    while n >= p:
        if n % p == 0:
            result += str(p) + " * "
            n /= p
        else:
            p += 1
    return result[:len(result)-3]
print(factorPrime(120)) # returns "2 x 2 x 2 x 3 x 5"