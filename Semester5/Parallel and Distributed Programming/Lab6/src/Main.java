import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicBoolean;

public class Main {

    private static final int NR_GRAPHS = 2000;
    private static final int NR_THREADS = 5;

    public static void main(String[] args) throws InterruptedException {
        for (int i = 1; i <= NR_GRAPHS; i++) {
            DirectedGraph graph = DirectedGraph.generateRandomHamiltonian(i*10); // nr of vertices
            test(i, graph, NR_THREADS);
        }
    }

    public static void test(int vertices, DirectedGraph graph, int nrThreads) throws InterruptedException {
        long startTime = System.nanoTime();
        find(graph, nrThreads);
        long endTime = System.nanoTime();
        long duration = (endTime - startTime) / 1000000;
        System.out.println(vertices*10 + " vertices: " + duration + " ms");
    }

    public static void find(DirectedGraph graph, int nrThreads) throws InterruptedException {
        ExecutorService pool = Executors.newFixedThreadPool(nrThreads);

        List<Integer> result = new ArrayList<>(graph.size());

        AtomicBoolean atomicBoolean = new AtomicBoolean(false);

        for (int i = 0; i < graph.size(); i++){ //check from each node
            pool.submit(new CycleFinder(graph, i, result, atomicBoolean));
        }

        pool.shutdown();

        pool.awaitTermination(10, TimeUnit.SECONDS);
    }

}