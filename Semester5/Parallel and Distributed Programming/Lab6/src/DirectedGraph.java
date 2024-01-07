import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import static java.util.Collections.shuffle;

public final class DirectedGraph {
    private final List<List<Integer>> container;
    private final List<Integer> nodes;

    DirectedGraph(int nodeCount) {
        this.container = new ArrayList<>(nodeCount);
        this.nodes = new ArrayList<>();

        for (int i = 0; i < nodeCount; i++) {
            this.container.add(new ArrayList<>());
            this.nodes.add(i);
        }
    }

    public void addEdge(int nodeA, int nodeB) {
        this.container.get(nodeA).add(nodeB);
    }

    public List<Integer> neighboursOf(int node) {
        return this.container.get(node);
    }

    public List<Integer> getNodes(){
        return nodes;
    }

    public int size() {
        return this.container.size();
    }

    public static DirectedGraph generateRandomHamiltonian(int size) {
        DirectedGraph graph = new DirectedGraph(size);

        List<Integer> nodes = graph.getNodes();

        shuffle(nodes);

        for (int i = 1; i < nodes.size(); i++){
            graph.addEdge(nodes.get(i - 1),  nodes.get(i));
        }

        graph.addEdge(nodes.get(nodes.size() -1), nodes.get(0));

        Random random = new Random();

        for (int i = 0; i < size / 2; i++){
            int nodeA = random.nextInt(size - 1);
            int nodeB = random.nextInt(size - 1);

            graph.addEdge(nodeA, nodeB);
        }

        return graph;
    }

}