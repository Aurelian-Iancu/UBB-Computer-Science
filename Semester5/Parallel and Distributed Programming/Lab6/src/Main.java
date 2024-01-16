import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // random graph
        Graph graph = new Graph(13);
        System.out.println(graph);

        // custom graphs
        // graph 1 - Hamiltonian cycle: 0 -> 1 -> 2 -> 3 -> 4 -> 0
        Graph graphWithHamiltonianCycle = new Graph(
                new ArrayList<>(List.of(0, 1, 2, 3, 4)),
                new ArrayList<>(
                        List.of(
                                new ArrayList<>(List.of(1, 4)),
                                new ArrayList<>(List.of(2, 4)),
                                new ArrayList<>(List.of(1, 3)),
                                new ArrayList<>(List.of(0, 2, 4)),
                                new ArrayList<>(List.of(0, 2))
                        )
                )
        );

        // graph 2 - no Hamiltonian cycle, edge 4 -> 0 is removed from the previous one
        Graph graphWithoutHamiltonianCycle = new Graph(
                new ArrayList<>(List.of(0, 1, 2, 3, 4)),
                new ArrayList<>(
                        List.of(
                                new ArrayList<>(List.of(1, 4)),
                                new ArrayList<>(List.of(2, 4)),
                                new ArrayList<>(List.of(1, 3)),
                                new ArrayList<>(List.of(0, 2, 4)),
                                new ArrayList<>(List.of(2))
                        )
                )
        );

        var startTime = System.nanoTime();
        HamiltonianCycleFinder findHamiltonianCycle = new HamiltonianCycleFinder(graph);
        findHamiltonianCycle.beginSearch();
        var endTime = System.nanoTime();
        System.out.println("Graph size: " + graph.size());
        System.out.println("Time: " + ((double) endTime - (double) startTime) / 1_000_000_000.0 + "s");

        startTime = System.nanoTime();
        findHamiltonianCycle = new HamiltonianCycleFinder(graphWithHamiltonianCycle);
        findHamiltonianCycle.beginSearch();
        endTime = System.nanoTime();
        System.out.println("Graph with Hamiltonian cycle size: " + graphWithHamiltonianCycle.size());
        System.out.println("Time: " + ((double) endTime - (double) startTime) / 1_000_000_000.0 + "s");

        startTime = System.nanoTime();
        findHamiltonianCycle = new HamiltonianCycleFinder(graphWithoutHamiltonianCycle);
        findHamiltonianCycle.beginSearch();
        endTime = System.nanoTime();
        System.out.println("Graph without Hamiltonian cycle size: " + graphWithoutHamiltonianCycle.size());
        System.out.println("Time: " + ((double) endTime - (double) startTime) / 1_000_000_000.0 + "s");
    }
}