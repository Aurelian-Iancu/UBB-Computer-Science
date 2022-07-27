#include <stdio.h>
#include <string.h>
// Problem number 10
void print_menu()
{
    // In this function we print the menu
    printf("Read the vector: 0\n");
    printf( "First functionality: 1\n");
    printf("Second functionality: 2\n");
    printf("Exit: 3\n");
    printf("Lab work: 4\n");
}
int read_vector(int v[])
{
    // In this function we read an array and it's length
    // v[] - the array we want to read
    int n_of_elems = 0;
    printf("The number of elements for the vector is: ");
    scanf("%d", &n_of_elems);
    for(int i = 0; i < n_of_elems; i++)
    {
        printf("Element %d: ", i);
        scanf("%d", &v[i]);
    }
    return n_of_elems;

}

void print_vector(int v[], int n_of_elems)
{
    // In this function we print an array
    // v[] - the array we want to print
    // n_of_elems - the number of elements of the array
    printf("The elements of the vector are: ");
    for (int i = 0; i < n_of_elems; i++)
        printf("%d ", v[i]);
    printf("\n");
}

int first_functionality(int n)
{
    // In this function we resolve the first functionality
    // We check if a number is prime in this function
    int d = 2, ok = 1;

    while(d * d <= n) {
        if (n % d == 0) {
            while (n % d == 0)
                n = n / d;
            ok = 0;
        }
        d++;
    }
    return ok;
}


void second_functionality(int n, int *first_position, int *last_position, int v[])
{
    // In this function we resolve the second functionality
    // Basically, we save 2 actual positions and 2 best positions which we will also send by reference in our main.
    // Every time we find a sequence longer than our previous one we update the positions. I had to find the longest
    // sequence where 2 numbers from the vector had at least 2 different digits. I did that with 2 frequency vectors
    // completed with the number of apparitions from each digit of the 2 numbers.
    int a[10], b[10], A, B, actual_first_position, actual_last_position, nr;
    *first_position = 0;
    *last_position = 0;
    actual_first_position = 0;
    actual_last_position = 0;
    for(int i = 0; i < n-1; i++)
    {
        nr = 0;
        for(int j = 0;j <= 9; j++)
        {
            a[j] = 0;
            b[j] = 0;
        }
        A = v[i];
        B = v[i+1];
        while(A != 0)
        {
            a[A%10] ++;
            A /= 10;
        }
        while(B != 0)
        {
            b[B%10] ++;
            B /=10;
        }
        for(int j = 0;j <= 9; j++)
        {
            if(a[j] != 0 && b[j] != 0)
                nr++;
        }
        if(nr >= 2)
            actual_last_position++;
        else
        {
            if(actual_last_position - actual_first_position > *last_position - *first_position)
            {
                *first_position = actual_first_position;
                *last_position = actual_last_position;
            }
            actual_last_position = i + 1;
            actual_first_position = i + 1;
        }

    }
    if(actual_last_position - actual_first_position > *last_position - *first_position)
    {
        *first_position = actual_first_position;
        *last_position = actual_last_position;
    }

}

int lab_functionality(int n)
{
    // It's basically the prime number algorithm. It return 1 if it's prime, 0 if it's not
    int d = 2, ok = 1;

    while(d * d <= n) {
        if (n % d == 0) {
            while (n % d == 0)
                n = n / d;
            ok = 0;
        }
        d++;
    }
    return ok;
}

int main()
{
    //variable declaration
    char command[100];
    int n_of_elems, v[100], prime[100], n , ok1, ok2, t = 1, ok, first_position, last_position;
    //menu printing
    print_menu();
    // vector initialization
    for(int i = 0;i <= 99; i++) {
        prime[i] = 0;
        v[i] = 0;
    }
    //loop for commands
    while (t == 1){

        printf("The command you want to enter is: ");
        scanf("%s", &command);
        fflush(stdout);
        fflush(stdin);
        // For 0 we read a vector
        if(strcmp(command, "0") == 0) {
            n_of_elems = read_vector(v);
            print_vector(v, n_of_elems);
        }
        // For 1 we resolve the first functionality
        else if(strcmp(command, "1") == 0) {
            // For every number bigger than 3 we see if it can be represented as a sum of 2 prime numbers and we print
            // them, we print a proper message otherwise
            n = 0;
            ok = 0;
            while (n < 3) {
                printf("The number you want to read from keyboard is: ");
                scanf("%d", &n);
                if(n < 3) {
                    printf("The number has to be higher than 2!!\n");
                    //fflush(stdout);
                }
            }
            for (int i = 2; i <= n - 1; i++) {
                ok1 = first_functionality(i);
                ok2 = first_functionality(n - i);
                if (ok1 == 1 && ok2 == 1) {
                    printf("Can be repr as the sum of %d and %d\n", i, n - i);
                    ok = 1;
                    break;
                }

            }
            if(ok == 0) {
                printf("Can't be repr as a sum of 2 primes!\n");
                fflush(stdout);
            }
        }
        // For 2 we resolve the second functionality
        // If the vector wasn't initialized we bring an error
        // Else we call the function second_functionality which sends the first and last position of our subarray
        //that fits the required condition
        else if(strcmp(command, "2") == 0)
        {
            first_position = 0;
            last_position = 0;
            ok = 1;
            for(int i = 0;i <= 99; i++)
                if(v[i] != 0)
                    ok = 0;
            if(ok == 1)
                printf("In order to use the first functionality you should initialize the vector at 0!");
            else {
                second_functionality(n_of_elems, &first_position, &last_position, v);
                for(int i = first_position; i <= last_position; i++)
                    printf("%d ", v[i]);
            }
            printf("\n");

        }
        //For 3 we stop the loop
        else if(strcmp(command, "3") == 0)
            t = 0;
        else if(strcmp(command, "4") == 0)
        {
            printf("The number you want to read from keyboard is:");
            scanf_s("%d", &n);
            printf("The prime numbers smaller than n are: ");
            for (int i = 2; i <= n -1; i++) {
                ok = lab_functionality(i);
                if(ok == 1)
                    printf("%d ", i);
            }
            printf("\n");
        }
        //For any other command we tell the user that it s an invalid command
        else
            printf("Invalid command!\n");
    }






}