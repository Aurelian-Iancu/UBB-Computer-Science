import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        float sum = 0, nr = 0;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of numbers you want to read");
        int n = scanner.nextInt();
        for(int i = 1; i <= n; i++){
            sum += scanner.nextInt();
            nr ++;
        }
        System.out.println("The average of the " + n + " numbers is " + sum/nr);
    }
}