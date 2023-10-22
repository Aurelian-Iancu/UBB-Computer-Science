import java.util.ArrayList;

public class HashTable<T> {
    private final ArrayList<ArrayList<T>> hashTable;
    private final int capacity;

    public HashTable(int capacity){
        this.capacity = capacity;
        this.hashTable = new ArrayList<>();
        for(int i = 0; i < capacity; i++){
            this.hashTable.add(new ArrayList<>());
        }
    }

    public int getCapacity() {
        return capacity;
    }

    private int hash(int key){
        return key % capacity ;
    }

    private int hash(String key) {
        int sum = 0;
        for (int i = 0; i < key.length(); i++) {
            sum += key.charAt(i);
        }
        return sum % capacity;
    }

    public boolean contains(T key){
        int hashValue = getHashValue(key);
        return hashTable.get(hashValue).contains(key);
    }

    public int getHashValue(T key){
        int hashValue = -1;
        if(key instanceof Integer){
            hashValue = hash((int)key);
        }
        else if (key instanceof String){
            hashValue = hash((String) key);
        }

        return hashValue;
    }

    public Pair<Integer, Integer> add(T key) throws Exception {
        int hashValue = getHashValue(key);
        if (!hashTable.contains(key)) {
            hashTable.get(hashValue).add(key);
            return new Pair<>(hashValue, hashTable.get(hashValue).indexOf(key));
        }
        throw new Exception("Key " + key + " is already in the table!");
    }

    public Pair<Integer, Integer> getPosition(T key) {
        if (this.contains(key)) {
            int hashValue = getHashValue(key);
            return new Pair<>(hashValue, hashTable.get(hashValue).indexOf(key));
        }
        return new Pair<>(-1, -1);
    }

    @Override
    public String toString() {
        return "HashTable{" + "items=" + hashTable + '}';
    }
}
