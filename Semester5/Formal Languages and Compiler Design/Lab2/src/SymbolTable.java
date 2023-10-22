

public class SymbolTable {
    private int size;
    private final HashTable<String> identifiersHashTable;
    private final HashTable<String> constantsHashTable;

    public SymbolTable(int size){
        this.size = size;
        this.identifiersHashTable = new HashTable<>(size);
        this.constantsHashTable = new HashTable<>(size);
    }

    public Pair<Integer, Integer> addIdentifier(String name) throws Exception {
        return this.identifiersHashTable.add(name);
    }

    public Pair<Integer, Integer> addConstant(String name) throws Exception{
        return this.constantsHashTable.add(name);
    }

    public boolean hasIdentifier(String name) {
        return identifiersHashTable.contains(name);
    }

    public boolean hasConstant(String constant) {
        return constantsHashTable.contains(constant);
    }

    public Pair<Integer, Integer> getPositionIdentifier(String name) {
        return identifiersHashTable.getPosition(name);
    }

    public Pair<Integer, Integer> getPositionConstant(String constant) {
        return constantsHashTable.getPosition(constant);
    }

    @Override
    public String toString() {
        return "SymbolTable{" +
                "identifiersHashTable=" + identifiersHashTable +
                "\nconstantsHashTable=" + constantsHashTable +
                '}';
    }
}



