public class Main {
    public static void main(String[] args) {
        HashTable<Object> myTable = new HashTable<>(10);

        myTable.add(5);
        myTable.add("apple");
        myTable.add(42);
        myTable.add(45);
        myTable.add("banana");
        myTable.add("cherry");

        System.out.println(myTable);

        System.out.println("Position of 'apple': " + myTable.getPosition("apple"));
        System.out.println("Position of 'banana': " + myTable.getPosition("banana"));
        System.out.println("Position of 42: " + myTable.getPosition(42));
        System.out.println("Position of 42: " + myTable.getPosition(45));
        System.out.println("Position of 10: " + myTable.getPosition(10)); // Not found
    }

}