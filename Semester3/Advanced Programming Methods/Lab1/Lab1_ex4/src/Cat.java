public class Cat extends Animal{
    public static String name = "Cerasela";

    String getName(){
        return name;
    }
    public Cat(int weight){
        super(weight);
    }
    String sound(){
        String s = "Meow, meow!";
        return s;
    }
}
