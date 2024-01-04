import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class HamiltonianSearchTask implements Runnable {
    private final List<List<Integer>> graph;
    private final int startingNode;
    private final AtomicBoolean foundHamiltonianCycle;
    private final List<Integer> possiblePath;
    private final List<Integer> output;
    private final Lock lock;
    private final List<Boolean> visited;

    public HamiltonianSearchTask(List<List<Integer>> graph, int startingNode, AtomicBoolean foundHamiltonianCycle, List<Integer> output) {
        this.graph = graph;
        this.startingNode = startingNode;
        this.foundHamiltonianCycle = foundHamiltonianCycle;
        this.possiblePath = new ArrayList<>();
        this.output = output;
        this.lock = new ReentrantLock();
        this.visited = new ArrayList<>();
        for (int i = 0; i < this.graph.size(); i++) {
            this.visited.add(false);
        }
    }

    private void foundCycle() {
        this.possiblePath.add(this.startingNode);
        this.foundHamiltonianCycle.set(true);
        this.lock.lock();
        this.output.clear();
        this.output.addAll(this.possiblePath);
        this.lock.unlock();
    }

    private void goToNode(int nextNode) {
        if (foundHamiltonianCycle.get()) {
            return;
        }

        this.possiblePath.add(nextNode);
        this.visited.set(nextNode, true);
        if (this.possiblePath.size() == this.graph.size()) {
            if (this.graph.get(nextNode).contains(this.startingNode)) {
                this.foundCycle();
            }
        }

        else {
            for (Integer outboundNeighbour : this.graph.get(nextNode)) {
                if (!this.visited.get(outboundNeighbour)) {
                    this.goToNode(outboundNeighbour);
                    return;
                }
            }
        }
    }

    @Override
    public void run() {
        this.goToNode(this.startingNode);
    }
}