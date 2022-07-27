# Solve the problem from the first set here
# Problem 3
#function to read a number from keyboard
def read_number():
    n = int(input("Enter a number: "))
    return n

#created a list of frequency
def freq_digits_of_n(n):
    L = [0] * 10 #initialized the list wtih 0
    while n > 0: #creating the list
        L[int(n % 10)] += 1
        n = int(n / 10)
    return L #returned the list


def create_number():
    num = 0 #in num we will create the smallest number.
    L2 = freq_digits_of_n(read_number())
    if L2[0] == 0: #in case we dont have 0 in number we calculate normally. We go through the list from the smallest to the largest and create the number with those
        for i in range(0, 10):
            if L2[i] > 0:
                while L2[i] > 0:
                    num = int(num) * 10 + i
                    L2[i] -= 1
    else: #in case we have a 0 we must find the smallest digit different from 0 because a number can't start with 0
        for i in range(1,10):
            if L2[i] > 0:
                num = int(num) * 10 + i
                L2[i] -= 1
                break
        for i in range(0, 10):
            if L2[i] > 0:
                while L2[i] > 0:
                    num = int(num) * 10 + i
                    L2[i] -= 1
    return num #we return the number we built


print("The smallest natural number written with the same digits as n is", create_number()) #we print the smallest number


