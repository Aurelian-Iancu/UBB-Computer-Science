public class Animal {
    private int weight;

    public Animal() {
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public int getWeight() {
        return weight;
    }

    public Animal(int weight) {
        this.weight = weight;
    }

    String sound(){
        String s = "Animal's sound";
        return s;
    }
}
