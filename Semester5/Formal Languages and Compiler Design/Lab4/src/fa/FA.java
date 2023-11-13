package fa;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Pattern;

public class FA {
    List<String> states;
    List<String> alphabet;
    String initialState;
    List<String> finalStates;
    List<Transition> transitions;

    String filename;


    public FA(String filename) {
        this.states = new ArrayList<>();
        this.alphabet = new ArrayList<>();
        this.finalStates = new ArrayList<>();
        this.transitions = new ArrayList<>();
        this.initialState = "";
        this.filename = filename;
        try{
            readFromFile();
        } catch (Exception e) {
            System.out.println("Error when initializingFA");
        }
    }


    public void readFromFile() throws IOException {
        File filename = new File(this.filename);
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
                        Transition createTuple = new Transition();
                        String[] tupleElements = tuple.trim().split(" ");
                        createTuple.setFrom(tupleElements[0]);
                        createTuple.setTo(tupleElements[1]);
                        createTuple.setLabel(tupleElements[2]);

                        transitions.add(createTuple);
                    }

                    break;
            }


        }
    }

    private void printListOfString(String listname, List<String> list) {
        System.out.print(listname + " = {");
        for (int i = 0; i < list.size(); i++) {
            if (i != list.size() - 1) {
                System.out.print(list.get(i) + ", ");
            } else {
                System.out.print(list.get(i));
            }
        }
        System.out.println("}");
    }

    public void printStates() {
        printListOfString("states", states);
    }

    public void printAlphabet() {
        printListOfString("alphabet", alphabet);
    }

    public void printOutputStates() {
        printListOfString("out_states", finalStates);
    }

    public void printInitialState() {
        System.out.println("initial_state = " + initialState);
    }

    public void printTransitions() {
        System.out.print("transitions = {");
        for (int i = 0; i < transitions.size(); i++) {
            if (i != transitions.size() - 1) {
                System.out.print("(" + transitions.get(i).getFrom() + ", " + transitions.get(i).getTo() + ", " + transitions.get(i).getLabel() + "); ");
            } else {
                System.out.print("(" + transitions.get(i).getFrom() + ", " + transitions.get(i).getTo() + ", " + transitions.get(i).getLabel() + ")");
            }
        }
        System.out.println("}");
    }

    public boolean checkAccepted(String word) {
        List<String> wordAsList = List.of(word.split(""));
        var currentState = initialState;
        for (String c: wordAsList) {
            var found = false;
            for (Transition transition: transitions) {
                if (transition.getFrom().equals(currentState) && transition.getLabel().equals(c)) {
                    currentState = transition.getTo();
                    found = true;
                    break;
                }
            }
            if (!found) {
                return false;
            }
        }
        return finalStates.contains(currentState);
    }

    public String getNextAccepted(String word) {
        var currentState = initialState;
        StringBuilder acceptedWord = new StringBuilder();
        for (String c: word.split("")) {
            String newState = null;
            for (Transition transition: transitions) {
                if (transition.getFrom().equals(currentState) && transition.getLabel().equals(c)) {
                    newState = transition.getTo();
                    acceptedWord.append(c);
                    break;
                }
            }
            if (newState == null) {
                if (!finalStates.contains(currentState)) {
                    return null;
                } else {
                    return acceptedWord.toString();
                }
            }
            currentState = newState;
        }
        return acceptedWord.toString();
    }

}
