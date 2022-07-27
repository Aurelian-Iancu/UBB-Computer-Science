# Solve the problem from the second set here
# Problem 7
#function to check if a number is prime
def verify_prime_number(n):
    ok = 1
    for i in range(2, n):
        if n % i == 0:
            ok = 0
    if ok == 1:
        return 1
    else:
        return 0

if __name__ == "__main__" :
    n = int(input("Enter a number: "))
    ok = 0
    counter = n + 1 #with counter we pass throw the numbers we want to check
    p1 = 0 #we initialize the numbers we are trying to find with 0 so that we can see if they changed during our processes
    p2 = 0
    while ok != 1: #we search till we find the 2 numbers we need
        if verify_prime_number(counter) == 1 and p1 == 0:
            p1 = counter
        elif verify_prime_number(counter) == 1 and p2 == 0 and p1 != 0:
            p2 = counter
        elif verify_prime_number(counter) == 1 and p1 != 0 and p2 != 0:
            p1 = p2
            p2 = counter
        if p1 != 0 and p2 != 0: #if the numbers are different than 0 and the difference in module is 2, we print them and break the program
            if abs(p1 - p2) == 2:
                ok = 1
                print("The first twin prime numbers larger than n are: " , p1, p2)
                break
        counter = counter + 1 #here we increase the counter otherwise we will have an infinite cicle