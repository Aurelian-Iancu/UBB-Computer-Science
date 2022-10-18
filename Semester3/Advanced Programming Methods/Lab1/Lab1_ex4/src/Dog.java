public class Dog extends Animal{
    public static String name = "Pufi";

    String getName(){
        return name;
    }
    public Dog(int weight){
        super(weight);
    }
    String sound(){
        String s = "Woof, woof";
        return s;
    }
}
