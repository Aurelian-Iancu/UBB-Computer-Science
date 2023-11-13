package fa;

import java.util.Objects;

public class Main {
    public static void main(String[] args) {
        var fa = new FA("./src/Files/FA.in");
        System.out.println("1. Print states");
        System.out.println("2. Print alphabet");
        System.out.println("3. Print output states");
        System.out.println("4. Print initial state");
        System.out.println("5. Print transitions");
        System.out.println("6. Check word");
        System.out.println("7. Get matching substring");
        System.out.println("0. Exit");
        while (true) {
            System.out.println("> ");
            var option = new java.util.Scanner(System.in).nextInt();
            switch (option) {
                case 1:
                    fa.printStates();
                    break;
                case 2:
                    fa.printAlphabet();
                    break;
                case 3:
                    fa.printOutputStates();
                    break;
                case 4:
                    fa.printInitialState();
                    break;
                case 5:
                    fa.printTransitions();
                    break;
                case 6:
                    var word = new java.util.Scanner(System.in).nextLine();
                    System.out.println(fa.checkAccepted(word));
                    break;
                case 7:
                    word = new java.util.Scanner(System.in).nextLine();
                    var accepted = fa.getNextAccepted(word);
                    if (Objects.equals(accepted, "")) {
                        System.out.println("No matching substring");
                    } else {
                        System.out.println(accepted);
                    }
                    break;
                case 0:
                    break;
                default:
                    System.out.println("Invalid option");
            }

        }
    }
}
