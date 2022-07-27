# Solve the problem from the third set here
# Problem 15
#function to calculate the sum of a number's divisors
def sum_of_divisors(n):
    s = 0
    for i in range (1,n):
        if n % i == 0:
            s += i
    return s

if __name__ == "__main__":
    n = int(input("Enter a number: ")) #here we get a number from keyboard
    copy = n - 1 #in variable copy we check the numbers smaller than n
    ok = 0 #boolean variable for the case we dont find a perfect number smaller than n
    while copy > 1:
        if sum_of_divisors(copy) == copy:#if the number is perfect we print the number and break the program
            ok = 1
            print("The largest perfect number smaller than n is", copy)
            break
        copy = copy - 1
    if ok == 0:# if we cant find a perfect number smaller than n we print this message
        print("There is no perfect number smaller than n")
