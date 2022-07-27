#
# Write the implementation for A2 in this file
#

# UI section
# (write all functions that have input or print statements here).
# Ideally, this section should not contain any calculations relevant to program functionalities


#Function to read a complex number by real part and imaginary part
def read_complex():
    r = int(input("The real part is: "))
    i = int(input("The imaginary part is: "))
    return [r, i]

#Function to print the menu
def print_menu():
    print("1. Read a list of complex numbers (in z = a + bi form) from the console.")
    print("2. Display the entire list of numbers on the console.")
    print("3. Display on the console the longest sequence that observes a given property. The numbers are real.")
    print("4. Display on the console the longest sequence that observes a given property. Real part is in the form of a mountain (first the values increase, then they decrease).")
    print("5. Exit the application.")


def read_list_of_numbers(List):
    n = int(input("The number of numbers you want to read is:")) #here we store how many numbers the user wants to read
    if n == 1:
        try:
            L = read_complex()
            List.append(L)  #when we read a number, we add it to the list
        except ValueError:
            print("invalid numerical value!") #in case the command isn't valid, we print a sugestive message
    else:
        for i in range(0,n):
            try:
                L = read_complex()
                List.append(L)
            except ValueError:
                print("invalid numerical value!")

#Function to print a numeber in the form z = a + bi
def print_complex(L):
    real = str(L[0]) #here we keep the real part in a string
    sign = "+" #in this variable we keep the sign of the imaginary part
    img = str(L[1]) + "i" #here we keep the imaginary part in a string
    if L[1] < 0 and L[1] != 1:
        img = str(-L[1]) + "i"
        sign = "-"
    elif L[1] == 0:
        img = ""
        sign = ""
    elif L[1] == 1:
        img = "i"
    if L[0] == 0:
        if(L[1] == 0):
            print("0")
        else:
            real = ""
            print(sign + img)
    else:
        print(real + " " + sign + " " + img)


def run_menu():
    List = [[7, 0], [2, 0], [2, 1], [2, 3], [2, 2], [2, 5], [2, 1], [1, 0], [2, 1], [1, 2]]#initialize the list with 10 numbers
    while True:
        cmd = input("The command you want to choose from the menu is:")#in this variable we will get the command from the user
        if cmd == "1":
            read_list_of_numbers(List)
        elif cmd == "2":
            for i in range(len(List)):
                print_complex(List[i])
        elif cmd == "3":
            print(property_5(List))
        elif cmd == "4":
            print(property_11(List))
        elif cmd == "5":
            return
        else:
            print("Invalid command!")


# Function section
# (write all non-UI functions in this section)
# There should be no print or input statements below this comment
# Each function should do one thing only
# Functions communicate using input parameters and their return values


#getter for the real part of the number
def get_real(L):
    return L[0]

#getter for the imaginary part of the number
def get_imaginary(L):
    return L[1]


def property_5(List):
    length_max_sequence = 0 #here we store the maximum length of our sequence
    length_actual_sequence = 0# here we store the actual length of our sequence
    max_first_position = 0#here we store the first position of the longest sequence
    max_last_position = 0#here we store the last position of the longest sequence
    actual_first_position = 0#here we store the first position of the actual sequence
    actual_last_position = 0#here we store the last position of the actual sequence
    copy = [] #in copy we store the longest sequence which we will return
    for i in range(len(List)):# we go throw the list
        if get_imaginary(List[i]) == 0 and length_actual_sequence == 0:#in the case we have a real number and we didn't start the sequence
            length_actual_sequence += 1
            actual_first_position = i
        elif get_imaginary(List[i]) == 0 and length_actual_sequence > 0:#in the case we have a real number ad we are in the middle of the sequence
            length_actual_sequence += 1
            actual_last_position = i
        elif get_imaginary(List[i]) != 0:#in the case we have a complex number we must stop the loop and check if this sequence is max
            if length_actual_sequence > length_max_sequence:
                max_first_position = actual_first_position
                max_last_position = actual_last_position
                length_max_sequence = length_actual_sequence
            length_actual_sequence = 0

    if length_actual_sequence > length_max_sequence:#we verify again in case we have our sequence at the end of the program
        max_first_position = actual_first_position
        max_last_position = actual_last_position
        length_max_sequence = length_actual_sequence

    for i in range(max_first_position, max_last_position + 1):#from first to last position we create a list with the longest wanted sequence
        copy.append(List[i])
    return copy


def property_11(List):
    i = 0#we start from 0
    mountain_first_index = -1 #we initialize the first position of the mountain
    mountain_last_index = -1#we initialize the last position of the mountain
    length_longest_mountain = 0#here we store the longest length of the mountain
    stop_longest_mountain = 0#here we store the position where our longest mountain stops
    copy = [] #in copy we store the longest mountain which we will return
    if (len(List) < 3):#we cant have a mountain with less than 3 numbers
        return 0
    for i in range(len(List) - 1):#we go throw the list
        if (get_real(List[i + 1]) > get_real(List[i])):
            if (mountain_last_index != -1):#When a new mountain sequence is found, there is a need to initialize the variables mountain_last_index and mountain_first_index
                mountain_last_index = -1
                mountain_first_index = -1
            if (mountain_first_index == -1):#j marks the starting index of a new mountain
                mountain_first_index = i
        else:
            if (get_real(List[i + 1]) < get_real(List[i])):# Checks if next element is less than current element
                if (mountain_first_index != -1):#Checks if starting element exists or not, if the starting element of the mountain sub-array exists then the index of ending element is stored in mountain_last_index
                    mountain_last_index = i + 1
                if (mountain_last_index != -1 and mountain_first_index != -1):#If we have the first and the last positions, we calculate the length of the mountain
                    if (length_longest_mountain < mountain_last_index - mountain_first_index + 1):#He see if the length is the longest
                        stop_longest_mountain = i + 1
                        length_longest_mountain = mountain_last_index - mountain_first_index + 1
            else:#otherwise we will reset the sequence
                mountain_last_index = -1
                mountain_first_index = -1
    if (mountain_last_index != -1 and mountain_first_index != -1):#we check again in the case our sequence is at the end
        if (length_longest_mountain < mountain_last_index - mountain_first_index + 1):
            length_longest_mountain = mountain_last_index - mountain_first_index + 1
            stop_longest_mountain = len(List) - 1

    start_longest_mountain = stop_longest_mountain - length_longest_mountain + 1
    for i in range(start_longest_mountain, stop_longest_mountain + 1):#we store the longest mountain in copy
        copy.append(List[i])
    return copy#we return the longest mountain

def start():
    print_menu()
    run_menu()



start()