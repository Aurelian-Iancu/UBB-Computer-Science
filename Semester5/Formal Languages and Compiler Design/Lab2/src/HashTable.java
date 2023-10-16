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
        int hash = 5381;
        for (int i = 0; i < key.length(); i++) {
            hash = ((hash << 5) + hash) + key.charAt(i);
        }
        return Math.abs(hash) % capacity;
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

    public void add(T key) {
        int hashValue = getHashValue(key);
        if (!hashTable.get(hashValue).contains(key)) {
            hashTable.get(hashValue).add(key);
        }
    }

    public int getPosition(T key) {
        int hashValue = getHashValue(key);
        if (hashValue != -1) {
            return hashValue;
        }
        return -1; // Key not found or not supported
    }

    @Override
    public String toString() {
        return "HashTable{" + "items=" + hashTable + '}';
    }
}
