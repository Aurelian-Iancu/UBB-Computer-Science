import datetime
import time


def gcd_brute_force(x, y):
    """
    We initialise the greatest_common_divisor variable with the smallest of the numbers and we try to see if we find a
    smaller number which for both of the numbers.
    More straight forward, we try every number between min(x,y) and 1 to see if both x and y can divide by it
    """
    if x == 0 or x == y:
        return y
    elif y == 0:
        return x
    greatest_common_divisor = min(x, y)
    while x % greatest_common_divisor != 0 or y % greatest_common_divisor != 0:
        greatest_common_divisor -= 1
    return greatest_common_divisor


def gcd_euclidean_subtractions(x, y):
    """
    This is the Euclidean algorithm using subtractions
    The trick is that we subtract the smaller number from the bigger number until they are equal.
    """
    if x == 0 or x == y:
        return y
    elif y == 0:
        return x
    while x != y:
        if x < y:
            y = y - x
        else:
            x = x - y
    return x


def gcd_euclidean_divisions(x, y):
    """
    The algorithm repeatedly takes the remainder of y divided by x and continues the process with the new values until
    x becomes zero, at which point the GCD is found. The algorithm is implemented recursively.
    """
    if x == 0 or x == y:
        return y
    elif y == 0:
        return x
    if (x == 0):
        return y;
    return gcd_euclidean_divisions(y % x, x);



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tests = [
        (5, 0),
        (18, 12),
        (30, 17),
        (256, 14),
        (17, 19),
        (17, 34),
        (4137524, 1227244),
        # (294733, 10383680172),
        (2 ** 50, 4 ** 20),
        # (17**23, 17**16),
        (182364, 116033),
        (70004, 43602),
        #(106626666, 783764444)
    ]
    for test in tests:
        first = test[0]
        second = test[1]
        print("\nx={},y={}".format(first, second))

        print("Start Brute Force")
        start_time = time.perf_counter()
        gcd = gcd_brute_force(first, second)
        end_time = time.perf_counter()
        print(f"Time elapsed: {end_time - start_time:.6f} seconds")
        print(f"GCD is {gcd}\n")

        print("Start Euclidean with subtractions")
        start_time = time.perf_counter()
        gcd = gcd_euclidean_subtractions(first, second)
        end_time = time.perf_counter()
        print(f"Time elapsed: {end_time - start_time:.6f} seconds")
        print(f"GCD is {gcd}\n")

        print("Start Euclidean with divisions")
        start_time = time.perf_counter()
        gcd = gcd_euclidean_divisions(first, second)
        end_time = time.perf_counter()
        print(f"Time elapsed: {end_time - start_time:.6f} seconds")
        print(f"GCD is {gcd}\n")
        print("--------------------------------------------------------------------------")


