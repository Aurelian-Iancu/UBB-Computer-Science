import math


def is_carmichael(n):
    if n == 1: #If a number is 1 it is not carmichael
        return '1'
    elif n == 2: # 2 is a prime number
        return 'prime'
    elif n % 2 != 0 and all(n % k != 0 for k in range(3, math.ceil(n**0.5), 2)): #checks if n number is prime
        return 'prime'
    elif all(pow(k, n, n) == k for k in range(1, n)): # checks for all the coprime numbers if k^n mod n is n
        return 'carmichael'
    else:
        return 'non-carmichael composite'


def get_carmichael_lower_than_given_bound(n):
    for possibleCarmichael in range(1, n + 1): #checks for all numbers between (1,n), n is the given bound if the number is carmichael
        if is_carmichael(possibleCarmichael) == 'carmichael':
            print(possibleCarmichael, " is a carmichael number")


if __name__ == "__main__":
    get_carmichael_lower_than_given_bound(10000) # prints all the carmichael numbers
