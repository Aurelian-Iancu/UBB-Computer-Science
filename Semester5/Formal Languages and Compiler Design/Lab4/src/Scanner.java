import fa.FA;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.regex.Pattern;

public class Scanner {
    private String program;
    private final List<String> tokens;
    private final List<String> reservedWords;
    private SymbolTable symbolTable;
    private List<Pair<String, Pair<Integer, Integer>>> PIF;
    private int index = 0;
    private int currentLine = 1;

    public Scanner() {
        this.symbolTable = new SymbolTable(47);
        this.PIF = new ArrayList<>();
        this.reservedWords = new ArrayList<>();
        this.tokens = new ArrayList<>();
        try {
            readTokens();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void setProgram(String program) {
        this.program = program;
    }

    private void readTokens() throws IOException {
        File file = new File("src/Files/Tokens.in");
        BufferedReader br = Files.newBufferedReader(file.toPath());
        String line;
        while ((line = br.readLine()) != null) {
            String[] parts = line.split(" ");
            switch (parts[0]) {
                case "start", "int", "string", "char", "vector", "bagă", "arată", "oare", "altfel", "atunci", "cattimp", "var", "fă", "oftype", "mod" -> reservedWords.add(parts[0]);
                default -> tokens.add(parts[0]);
            }
        }
    }

    private void skipSpaces() {
        while (index < program.length() && Character.isWhitespace(program.charAt(index))) {
            if (program.charAt(index) == '\n') {
                currentLine++;
            }
            index++;
        }
    }

    private boolean treatIntConstant(){
//        var regexForIntConstant = Pattern.compile("^([+-]?[1-9][0-9]*|0)");
//        var matcher = regexForIntConstant.matcher(program.substring(index));
//        if (!matcher.find()) {
//            return false;
//        }
        if (Pattern.compile("^([+-]?[1-9][0-9]*|0)[a-zA-z_]").matcher(program.substring(index)).find()) {
            return false;
        }

        var fa = new FA("./src/Files/intConstant.in");
        var intConstant = fa.getNextAccepted(program.substring(index));
        if (Objects.equals(intConstant, null)) {
            return false;
        }
        if ((intConstant.charAt(0) == '+' || intConstant.charAt(0) == '-')
                && PIF.size() > 0
                && ( PIF.get(PIF.size() - 1).getFirst().equals("const") || PIF.get(PIF.size() - 1).getFirst().equals("identifier"))) {
            return false;
        }
//        var intConstant = matcher.group(1);
        index += intConstant.length();
        String stringConstant = new String(intConstant);
        Pair<Integer, Integer> position;
        try {
            position = symbolTable.addConstant(stringConstant);
        } catch (Exception e) {
            position = symbolTable.getPositionConstant(stringConstant);
        }
        PIF.add(new Pair<>("const", position));
        return true;
    }

    private boolean treatStringConstant() throws Exception {
        var regexForStringConstant = Pattern.compile("^\"[a-zA-z0-9_ ?:*^+=.!]*\"");
        var matcher = regexForStringConstant.matcher(program.substring(index));
        if (!matcher.find()) {
            if (Pattern.compile("^\"[^\"]\"").matcher(program.substring(index)).find()) {
                throw new Exception("Invalid string constant at line " + currentLine);
            }
            if (Pattern.compile("^\"[^\"]").matcher(program.substring(index)).find()) {
                throw new Exception("Missing \" at line " + currentLine);
            }
            return false;
        }
        var stringConstant = matcher.group(0);
        index += stringConstant.length();
        Pair<Integer, Integer> position;
        try {
            position = symbolTable.addConstant(stringConstant);
        } catch (Exception e) {
            position = symbolTable.getPositionConstant(stringConstant);
        }
        PIF.add(new Pair<>("const", position));
        return true;
    }

    private boolean checkIfValid(String possibleIdentifier, String programSubstring) {
        if (reservedWords.contains(possibleIdentifier)) {
            return false;
        }
        if (Pattern.compile("^[A-Za-z_][A-Za-z0-9_]*\\s+oftype int|char|str").matcher(programSubstring).find()) {
            return true;
        }
        return symbolTable.hasIdentifier(possibleIdentifier);
    }

    private boolean treatIdentifier() {
//        var regexForIdentifier = Pattern.compile("^([a-zA-Z_][a-zA-Z0-9_]*)");
//        var matcher = regexForIdentifier.matcher(program.substring(index));
//        if (!matcher.find()) {
//            return false;
//        }
//        var identifier = matcher.group(1);
        var fa = new FA("./src/Files/identifier.in");
        var identifier = fa.getNextAccepted(program.substring(index));
        if(identifier == null){
            return false;
        }
        if (!checkIfValid(identifier, program.substring(index))) {
            return false;
        }
        index += identifier.length();
        Pair<Integer, Integer> position;
        try {
            position = symbolTable.addIdentifier(identifier);
        } catch (Exception e) {
            position = symbolTable.getPositionIdentifier(identifier);
        }
        PIF.add(new Pair<>("identifier", position));
        return true;
    }

    private boolean treatFromTokenList() {
        String possibleToken = program.substring(index).split(" ")[0];
        for (var reservedToken: reservedWords) {
            if (possibleToken.startsWith(reservedToken)) {
                var regex = "^" + "[a-zA-Z0-9_]*" + reservedToken + "[a-zA-Z0-9_]+";
                if (Pattern.compile(regex).matcher(possibleToken).find()) {
                    return false;
                }
                index += reservedToken.length();
                PIF.add(new Pair<>(reservedToken, new Pair<>(-1, -1)));
                return true;
            }
        }
        for (var token : tokens) {
            if (Objects.equals(token, possibleToken)) {
                index += token.length();
                PIF.add(new Pair<>(token, new Pair<>(-1, -1)));
                return true;
            }
            else if (possibleToken.startsWith(token)) {
                index += token.length();
                PIF.add(new Pair<>(token, new Pair<>(-1, -1)));
                return true;
            }
        }
        return false;
    }

    private void nextToken() throws Exception{
        skipSpaces();
        if (index == program.length()) {
            return;
        }
        if (treatIdentifier()) {
            return;
        }
        if(treatIntConstant()){
            return;
        }
        if (treatStringConstant()) {
            return;
        }
        if (treatFromTokenList()) {
            return;
        }
        throw new Exception("Lexical error: invalid token at line " + currentLine + ", index " + index);
    }

    public void scan(String programFileName){
        try {
            Path file = Path.of("src/Files/" + programFileName);
            setProgram(Files.readString(file));
            index = 0;
            PIF = new ArrayList<>();
            symbolTable = new SymbolTable(47);
            currentLine = 1;
            while (index < program.length()) {
                nextToken();
            }
            FileWriter fileWriter = new FileWriter("PIF" + programFileName.replace(".txt", ".out"));
            for (var pair : PIF) {
                fileWriter.write(pair.getFirst() + " -> (" + pair.getSecond().getFirst() + ", " + pair.getSecond().getSecond() + ")\n");
            }
            fileWriter.close();
            fileWriter = new FileWriter("ST" + programFileName.replace(".txt", ".out"));
            fileWriter.write(symbolTable.toString());
            fileWriter.close();
            System.out.println("Lexically correct");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
