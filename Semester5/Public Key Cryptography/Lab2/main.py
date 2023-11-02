import math


def is_carmichael(n):
    # Requires a positive integer.
    if n == 1:
        return '1'
    elif n == 2:
        return 'prime'
    elif n % 2 != 0 and all(n % k != 0 for k in range(3, math.ceil(n**0.5), 2)):
        return 'prime'
    elif all(pow(k, n, n) == k for k in range(1, n)):
        return 'carmichael'
    else:
        return 'non-carmichael composite'


def get_carmichael_lower_than_given_bound(n):
    for possibleCarmichael in range(1, n + 1):
        if is_carmichael(possibleCarmichael) == 'carmichael':
            print(possibleCarmichael, " is a carmichael number")


if __name__ == "__main__":
    get_carmichael_lower_than_given_bound(10000)
