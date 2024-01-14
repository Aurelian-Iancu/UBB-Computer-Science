import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;

public class IDAStar {

    private static final int NR_THREADS = 2;
    //private static final int NR_TASKS = 5;

    private static ExecutorService executorService;

    public static void main(String[] args) throws IOException, InterruptedException, ExecutionException {
        Matrix initialState = Matrix.fromFile();

        executorService = Executors.newFixedThreadPool(NR_THREADS);
        //executorService.submit(IDAStar::diagnosticsTread);

        Matrix solution = solve(initialState);
        System.out.println(solution);
        executorService.shutdown();
        executorService.awaitTermination(1000000, TimeUnit.SECONDS);
    }

    public static Matrix solve(Matrix root) throws ExecutionException, InterruptedException {
        long time = System.currentTimeMillis();
        int minBound = root.getManhattan();
        int dist;
        while (true) {
            Pair<Integer, Matrix> solution = searchParallel(root, 0, minBound, NR_THREADS);
            dist = solution.getFirst();
            if (dist == -1) {
                System.out.println("Solution found in " + solution.getSecond().getNumOfSteps() + " steps");
                System.out.println("Execution time: " + (System.currentTimeMillis() - time) + "ms");
                return solution.getSecond();
            } else {
                System.out.println("Depth " + dist + " reached in " + (System.currentTimeMillis() - time) + "ms");
            }
            minBound = dist;
        }
    }

    public static Pair<Integer, Matrix> searchParallel(Matrix current, int numSteps, int bound, int nrThreads) throws ExecutionException, InterruptedException {
        if (nrThreads <= 1) {
            return search(current, numSteps, bound);
        }

        int estimation = numSteps + current.getManhattan();

        if (estimation > bound) {
            return new Pair<>(estimation, current);
        }
        if (estimation > 80) {
            return new Pair<>(estimation, current);
        }
        if (current.getManhattan() == 0) {
            return new Pair<>(-1, current);
        }
        int min = Integer.MAX_VALUE;
        List<Matrix> moves = current.generateMoves();
        List<Future<Pair<Integer, Matrix>>> futures = new ArrayList<>();
        for (Matrix next : moves) {
            Future<Pair<Integer, Matrix>> f = executorService.submit(() -> searchParallel(next, numSteps + 1, bound, nrThreads / moves.size()));
            futures.add(f);
        }
        for (Future<Pair<Integer, Matrix>> f : futures) {
            Pair<Integer, Matrix> result = f.get();
            int t = result.getFirst();
            if (t == -1) {
                return new Pair<>(-1, result.getSecond());
            }
            if (t < min) {
                min = t;
            }

        }
        return new Pair<>(min, current);
    }

    public static Pair<Integer, Matrix> search(Matrix current, int numSteps, int bound) {
        int estimation = numSteps + current.getManhattan();
        if (estimation > bound) {
            return new Pair<>(estimation, current);
        }
        if (estimation > 80) {
            return new Pair<>(estimation, current);
        }
        if (current.getManhattan() == 0) {
            return new Pair<>(-1, current);
        }
        int min = Integer.MAX_VALUE;
        Matrix solution = null;
        for (Matrix next : current.generateMoves()) {
            if (true) {
                Pair<Integer, Matrix> result = search(next, numSteps + 1, bound);
                int t = result.getFirst();
                if (t == -1) {
                    return new Pair<>(-1, result.getSecond());
                }
                if (t < min) {
                    min = t;
                    solution = result.getSecond();
                }
            }
        }
        return new Pair<>(min, solution);

    }

//    public static void diagnosticsTread() {
//        long startTime = System.currentTimeMillis();
//        int k = 0;
//        while (true) {
//            // Add diagnostics here
//            Matrix head = null;
//            if (head == null) {
//                long endTime = System.currentTimeMillis();
//                //System.out.println("Run time: " + (endTime - startTime) + "ms");
//                return;
//            }
//        }
//    }


}