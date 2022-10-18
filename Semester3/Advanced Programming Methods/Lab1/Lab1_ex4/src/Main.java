import java.awt.font.NumericShaper;

public class Main{
    static void printer(){
        System.out.println("If the animal has the weight smaller than 10, it will throw an exception!");
    }

    static void thrower(Animal animal)throws Exception{
        if(animal.getWeight() < 10){
            throw new Exception("The animal can't be smaller than 10 kilograms");
        }
        else
            System.out.println(animal.getWeight());
    }


    public static void main(String[] args) throws Exception{

        Dog dog = new Dog(5);
        System.out.println("The dog " + dog.getName() + " makes the sound " + dog.sound());

        Cat cat = new Cat(10);
        System.out.println("The cat " + cat.getName() + " makes the sound " + cat.sound());

        printer();
        try {
            thrower(cat);
            thrower(dog);
        }
        catch(Exception e){
            System.out.println(e.toString());
        }


    }
}
