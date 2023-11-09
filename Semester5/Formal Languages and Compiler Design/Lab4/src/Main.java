import java.io.IOException;

public class Main {

    public static void main(String[] args) throws IOException {
        FA fa = new FA();
        fa.readFromFile();
        fa.printFA();
    }
}