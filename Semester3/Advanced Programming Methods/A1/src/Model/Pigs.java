package Model;

public class Pigs implements Animal{
    private float weight;

    @Override
    public float getWeight() {
        return weight;
    }

    @Override
    public void setWeight(float weight) {
        this.weight = weight;
    }

    public Pigs(float weight) {
        this.weight = weight;
    }

    @Override
    public String toText() {
        return "Pig with the weight " + weight + " kg";
    }
}
