package fa;

public class Transition {
    private String from;
    private String to;
    private String label;

    public Transition(){

    }

    public Transition(String from, String to, String label) {
        this.from = from;
        this.to = to;
        this.label = label;
    }

    public String getFrom() {
        return from;
    }

    public String getTo() {
        return to;
    }

    public String getLabel() {
        return label;
    }

    public void setFrom(String from) {
        this.from = from;
    }

    public void setTo(String to) {
        this.to = to;
    }

    public void setLabel(String label) {
        this.label = label;
    }
}