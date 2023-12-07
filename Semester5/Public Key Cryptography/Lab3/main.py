import random

"""
d such that d*2^r=n-1, r >= 1
n is the number we are trying to verify if
"""
def miillerTest(d, n):
    """
    Pick a random base a:
    """
    a = 2 + random.randint(1, n - 4)
    """
    Computer a^d mod n
    """
    x = pow(a, d, n)

    """
    Check for primality conditions:
    1. If x = 1 or x = n - 1 the number n is probably prime
    2. Otherwise iterating while d != n-1 square x and double d then check if x = 1(n is composite), x = n-1(n is probably prime)
    """
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True

    """
    Return composite
    """


def isPrime(n, k):
    """
    Corner cases
    """
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    """
    Find d such that n = 2^d*r+1
    """
    d = n - 1
    while d % 2 == 0:
        d //= 2

    """
    Do the miller-rabin test k times
    If all iterations pass, the number is prime
    """
    for i in range(k):
        if not(miillerTest(d, n)):
            return False
    return True


k = 4

for n in range(1, 101):
    if isPrime(n, k):
        print(n)
