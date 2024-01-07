import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;


public final class CycleFinder implements Runnable{
    private final DirectedGraph graph;
    private final int startingNode;
    private final List<Integer> path;
    private final Lock lock;
    private final List<Integer> result;
    private final AtomicBoolean aBoolean;

    CycleFinder(DirectedGraph graph, int node, List<Integer> result, AtomicBoolean aBoolean) {
        this.graph = graph;
        this.startingNode = node;
        this.path = new ArrayList<>();
        this.lock = new ReentrantLock();
        this.aBoolean = aBoolean;
        this.result = result;
    }

    @Override
    public void run() {
        visit(startingNode);
    }

    private void visit(int node) {
        path.add(node);
        if (!aBoolean.get()){
            if (path.size() == graph.size()) {
                if (graph.neighboursOf(node).contains(startingNode)){
                    //found a cycle
                    aBoolean.set(true);
                    this.lock.lock();
                    result.clear();
                    result.addAll(this.path);
                    //System.out.println(result);
                    this.lock.unlock();
                }
                return;
            }

            graph.neighboursOf(node).forEach(neighbour->{
                if (!this.path.contains(neighbour)){
                    visit(neighbour);
                }
            });
        }
    }


}