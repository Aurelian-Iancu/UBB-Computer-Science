import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;

public class Scanner {

    private String program;
    private int index = 0;
    private int currentLine = 1;
    private final ArrayList<String> operators = new ArrayList<>(
            List.of("+", "-", "*", "/", "mod", "<=", ">=", "==", "<", ">", "=")
    );

    private final ArrayList<String> separators = new ArrayList<>(
            List.of("[", "]", "{", "}", "(", ")", ";", ":", ",", " ", "\n")
    );
    private final ArrayList<String> reservedWords = new ArrayList<>(
            List.of("start", "int", "string", "char", "vector", "bagă", "arată", "oare", "altfel", "atunci" +
                    "cattimp", "var", "fă", "oftype")
    );

    private final ArrayList<String> tokens;
    private SymbolTable symbolTable;
    private List<Pair<String, Pair<Integer, Integer>>> PIF;

    public Scanner() {
        this.symbolTable = new SymbolTable(47);
        this.PIF = new ArrayList<>();
        this.tokens = new ArrayList<>();
    }




}
