public class Main {
    public static void main(String[] args) {
        SymbolTable symbolTable = new SymbolTable(15);
        Pair<Integer, Integer> p1 = new Pair<>(-1, - 1);
        Pair<Integer, Integer> p2 = new Pair<>(-1, - 1);

        try{
            p1 = symbolTable.addIdentifier("abc");
            System.out.println("abc -> " + p1);
            System.out.println("_a ->" + symbolTable.addIdentifier("_a"));
            System.out.println("bdfas ->" + symbolTable.addIdentifier("bdfas"));

            p2 = symbolTable.addConstant("1");
            System.out.println("2 -> " + symbolTable.addConstant("2"));
            System.out.println("3 -> " + symbolTable.addConstant("3"));
            System.out.println("string1 -> " + symbolTable.addConstant("string1"));
            System.out.println("another -> " + symbolTable.addConstant("another"));

            System.out.println(symbolTable);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

}