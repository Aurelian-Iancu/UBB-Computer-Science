package Model;

public class Cows implements Animal{
    private float weight;

    public Cows(float weight) {
        this.weight = weight;
    }

    @Override
    public float getWeight() {
        return weight;
    }

    @Override
    public void setWeight(float weight) {
        this.weight = weight;
    }

    @Override
    public String toText() {
        return "Cow with the weight " + weight + " kg";
    }
}
