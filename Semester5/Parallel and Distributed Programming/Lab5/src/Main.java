import Models.Polynomial;
import Options.ParallelClassic;
import Options.ParallelKaratsuba;
import Options.SequentialClassic;
import Options.SequentialKaratsuba;

import java.util.Scanner;
import java.util.concurrent.ExecutionException;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Enter the degree of the first polynomial (or -1 to exit):");
            int degree1 = scanner.nextInt();
            if (degree1 == -1) {
                break;
            }

            System.out.println("Enter the degree of the second polynomial:");
            int degree2 = scanner.nextInt();
            Polynomial p1 = new Polynomial(degree1);
            Polynomial p2 = new Polynomial(degree2);

            System.out.println("Choose the multiplication algorithm:");
            System.out.println("1. Sequential Classic");
            System.out.println("2. Sequential Karatsuba");
            System.out.println("3. Parallel Classic");
            System.out.println("4. Parallel Karatsuba");
            System.out.println("5. Exit");

            int choice = scanner.nextInt();

            if (choice == 5) {
                break;
            }

            try {
                long startTime = System.currentTimeMillis();
                switch (choice) {
                    case 1:
                        SequentialClassic.multiply(p1, p2);
                        break;
                    case 2:
                        SequentialKaratsuba.multiply(p1, p2);
                        break;
                    case 3:
                        ParallelClassic.multiply(p1, p2);
                        break;
                    case 4:
                        ParallelKaratsuba.multiply(p1, p2, 1);
                        break;
                    default:
                        System.out.println("Invalid choice. Please enter a number between 1 and 5.");
                }
                long endTime = System.currentTimeMillis();
                System.out.println("Time taken: " + (endTime - startTime) + " milliseconds");
            } catch (InterruptedException | ExecutionException e) {
                e.printStackTrace();
            }
        }

        System.out.println("Exiting the program.");
        scanner.close();
    }
}