package Model;

public class Birds implements Animal{
    private float weight;

    public Birds(float weight) {
        this.weight = weight;
    }

    @Override
    public float getWeight(){
        return weight;
    }


    public void setWeight(float weight) {
        this.weight = weight;
    }

    @Override
    public String toText() {
        return "Bird with the weight " + weight + " kg";
    }
}
