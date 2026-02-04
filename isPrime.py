def isPrime(n):
    if n == 1:
        print(False)
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(False)
            return False
    print(True)
    return True

isPrime(1); # returns false
isPrime(5); # returns true
isPrime(91); # returns false
isPrime(1000000); # returns false