import mpi.MPI;

import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

    public static void main(String[] args) throws IOException {
        MPI.Init(args);
        int me = MPI.COMM_WORLD.Rank();
        if (me == 0) {
            // master process
            Matrix matrix = Matrix.fromFile();
            searchMaster(matrix);
        } else {
            // worker process
            searchWorker();
        }
        MPI.Finalize();
    }

    private static void searchMaster(Matrix root) {
        int size = MPI.COMM_WORLD.Size();
        int workers = size - 1;
        int minBound = root.getManhattan();
        boolean found = false;
        long time = System.currentTimeMillis();

        // generate the starting configurations for the workers
        Queue<Matrix> q = new LinkedList<>();
        q.add(root);
        while (q.size() + q.peek().generateMoves().size() - 1 <= workers) {
            Matrix curr = q.poll();
            for (Matrix neighbour : curr.generateMoves()) {
                q.add(neighbour);
            }
        }

        while (!found) {

            // send data to all workers
            Queue<Matrix> temp = new LinkedList<>();
            temp.addAll(q);
            for (int i = 0; i < q.size(); i++) {
                // for each worker, send a "root"
                Matrix curr = temp.poll();
                MPI.COMM_WORLD.Send(new boolean[]{false}, 0, 1, MPI.BOOLEAN, i + 1, 0);
                MPI.COMM_WORLD.Send(new Object[]{curr}, 0, 1, MPI.OBJECT, i + 1, 0);
                MPI.COMM_WORLD.Send(new int[]{minBound}, 0, 1, MPI.INT, i + 1, 0);
            }

            Object[] pairs = new Object[size + 5];
            // receive data
            for (int i = 1; i <= q.size(); i++) {
                MPI.COMM_WORLD.Recv(pairs, i - 1, 1, MPI.OBJECT, i, 0);
            }

            // check if any node found a solution
            int newMinBound = Integer.MAX_VALUE;
            for (int i = 0; i < q.size(); i++) {
                Pair<Integer, Matrix> p = (Pair<Integer, Matrix>) pairs[i];
                //System.out.println(p.toString());
                if (p.getFirst() == -1) {
                    // found solution
                    System.out.println("Solution found in " + p.getSecond().getNumOfSteps() + " steps");
                    System.out.println("Solution is: ");
                    System.out.println(p.getSecond());
                    System.out.println("Execution time: " + (System.currentTimeMillis() - time) + "ms");
                    found = true;
                    break;
                } else if (p.getFirst() < newMinBound) {
                    newMinBound = p.getFirst();
                }
            }
            if(!found){
                System.out.println("Depth " + newMinBound + " reached in " + (System.currentTimeMillis() - time) + "ms");
                minBound = newMinBound;
            }
        }

        for (int i = 1; i < size; i++) {
            // shut down workers when solution was found
            Matrix curr = q.poll();
            MPI.COMM_WORLD.Send(new boolean[]{true}, 0, 1, MPI.BOOLEAN, i, 0);
            MPI.COMM_WORLD.Send(new Object[]{curr}, 0, 1, MPI.OBJECT, i, 0);
            MPI.COMM_WORLD.Send(new int[]{minBound}, 0, 1, MPI.INT, i, 0);
        }
    }

    private static void searchWorker() {
        while (true) {
            Object[] matrix = new Object[1];
            int[] bound = new int[1];
            boolean[] end = new boolean[1];
            MPI.COMM_WORLD.Recv(end, 0, 1, MPI.BOOLEAN, 0, 0);
            MPI.COMM_WORLD.Recv(matrix, 0, 1, MPI.OBJECT, 0, 0);
            MPI.COMM_WORLD.Recv(bound, 0, 1, MPI.INT, 0, 0);
            if (end[0]) { // shut down when solution was found
                //System.out.println("Node " + MPI.COMM_WORLD.Rank() + " is ending its execution");
                return;
            }
            int minBound = bound[0];
            Matrix current = (Matrix) matrix[0];
            Pair<Integer, Matrix> result = search(current, current.getNumOfSteps(), minBound);
            MPI.COMM_WORLD.Send(new Object[]{result}, 0, 1, MPI.OBJECT, 0, 0);
        }
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
        return new Pair<>(min, solution);
    }

}