import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public final class Matrix {

    private static final int[] dx = new int[]{0, -1, 0, 1};
    private static final int[] dy = new int[]{-1, 0, 1, 0};
    private static final String[] movesStrings = new String[]{"left", "up", "right", "down"};

    private final byte[][] tiles;

    private final int numOfSteps;
    private final int freePosI;
    private final int freePosJ;

    private final Matrix previousState;
    private final int minSteps;
    private final int estimation;
    private final int manhattan;
    private final String move;
    private final int hashValue;


    public Matrix(byte[][] tiles, int freePosI, int freePosJ, int numOfSteps, Matrix previousState, String move) {
        this.tiles = tiles;
        this.freePosI = freePosI;
        this.freePosJ = freePosJ;
        this.numOfSteps = numOfSteps;
        this.previousState = previousState;
        this.move = move;
        this.manhattan = manhattanDistance();
        this.minSteps = numOfSteps + manhattan;
        this.estimation = manhattan + numOfSteps;
        this.hashValue = hashCodeFake();
    }

    public static Matrix fromFile() throws IOException {
        byte[][] tiles = new byte[4][4];
        int freeI = -1, freeJ = -1;
        Scanner scanner = new Scanner(new BufferedReader(new FileReader(new File("C:\\Users\\Aurelian\\Documents\\GitHub\\Personal\\UBB-Computer-Science\\Semester5\\Parallel and Distributed Programming\\Project\\Threads\\matrix.in"))));
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                tiles[i][j] = Integer.valueOf(scanner.nextInt()).byteValue();
                if (tiles[i][j] == 0) {
                    freeI = i;
                    freeJ = j;
                }
            }
        }
        return new Matrix(tiles, freeI, freeJ, 0, null, "");
    }


    public int manhattanDistance() {
        int s = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (tiles[i][j] != 0) {
                    int targetI = (tiles[i][j] - 1) / 4;
                    int targetJ = (tiles[i][j] - 1) % 4;
                    s += Math.abs(i - targetI) + Math.abs(j - targetJ);
                }
            }
        }
        return s;
    }

    public List<Matrix> generateMoves() {
        List<Matrix> moves = new ArrayList<>();
        for (int k = 0; k < 4; k++) {
            if (freePosI + dx[k] >= 0 && freePosI + dx[k] < 4 && freePosJ + dy[k] >= 0 && freePosJ + dy[k] < 4) {
                int movedFreePosI = freePosI + dx[k];
                int movedFreePosJ = freePosJ + dy[k];
                if (previousState != null && movedFreePosI == previousState.freePosI && movedFreePosJ == previousState.freePosJ) {
                    continue;
                }
                byte[][] movedTiles = Arrays.stream(tiles)
                        .map(byte[]::clone)
                        .toArray(byte[][]::new);
                movedTiles[freePosI][freePosJ] = movedTiles[movedFreePosI][movedFreePosJ];
                movedTiles[movedFreePosI][movedFreePosJ] = 0;

                moves.add(new Matrix(movedTiles, movedFreePosI, movedFreePosJ, numOfSteps + 1, this, movesStrings[k]));

            }
        }
        return moves;
    }

    @Override
    public String toString() {
        Matrix current = this;
        List<String> strings = new ArrayList<>();
        while (current != null) {
            StringBuilder sb = new StringBuilder();
            sb.append("\n");
            sb.append(current.move);
            sb.append("\n");
            Arrays.stream(current.tiles).forEach(row -> sb.append(Arrays.toString(row)).append("\n"));
            sb.append("\n");
            strings.add(sb.toString());
            current = current.previousState;
        }
        Collections.reverse(strings);
        return "Moves{" +
                String.join("", strings) +
                "numOfSteps=" + numOfSteps +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Matrix matrix = (Matrix) o;
        boolean flag = true;
        for (int i = 0; i < 4; i++)
            flag = flag && Arrays.equals(tiles[i], matrix.tiles[i]);
        return flag;
    }

    @Override
    public int hashCode() {
        return hashValue;
    }


    private int hashCodeFake() {
        int result = 0;
        for (int i = 0; i < 4; i++) {
            result += Arrays.hashCode(tiles[i]);
        }
        return result;
    }

    public int getEstimation() {
        return estimation;
    }

    public int getMinSteps() {
        return minSteps;
    }

    public int getNumOfSteps() {
        return numOfSteps;
    }

    public int getManhattan() {
        return manhattan;
    }

}