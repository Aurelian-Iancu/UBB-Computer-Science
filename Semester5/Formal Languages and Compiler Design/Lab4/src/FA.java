import java.io.*;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class FA {
    List<String> states;
    List<String> alphabet;
    String initialState;
    List<String> finalStates;
    List<Tuple<String, String, String>> transitions;

    public FA() {
        states = new ArrayList<>();
        alphabet = new ArrayList<>();
        finalStates = new ArrayList<>();
        transitions = new ArrayList<>();
    }

    public void readFromFile() throws IOException {
        File filename = new File("./src/files/FA.in");
        BufferedReader br = Files.newBufferedReader(filename.toPath());
        String line;
        while ((line = br.readLine()) != null) {
            String[] parts = line.split(":");

            String key = parts[0];
            switch(key){
                case"states":
                    String[] statesString = parts[1].trim().split(",");
                    states.addAll(Arrays.asList(statesString));
                    break;
                case"alphabet":
                    String[] alphabetString = parts[1].trim().split(",");
                    alphabet.addAll(Arrays.asList(alphabetString));
                    break;
                case"initial state":
                    initialState = parts[1].trim();
                    break;
                case"final states":
                    String[] finalStatesString = parts[1].trim().split(",");
                    finalStates.addAll(Arrays.asList(finalStatesString));
                    break;
                case"transitions":
                    String[] tuples = parts[1].trim().split(",");
                    for(var tuple: tuples){
                        Tuple<String,String,String> createTuple = new Tuple<>();
                        String[] tupleElements = tuple.trim().split(" ");
                        createTuple.setFirst(tupleElements[0]);
                        createTuple.setSecond(tupleElements[1]);
                        createTuple.setThird(tupleElements[2]);

                        transitions.add(createTuple);
                    }

                    break;
            }


        }
    }

    public void printFA() {
        System.out.println("States: " + states);
        System.out.println("Alphabet: " + alphabet);
        System.out.println("Initial State: " + initialState);
        System.out.println("Final States: " + finalStates);
        System.out.println("Transitions:");
        for (Tuple<String, String, String> transition : transitions) {
            System.out.println(transition.getFirst() + " " + transition.getSecond() + " " + transition.getThird());
        }
    }
}
