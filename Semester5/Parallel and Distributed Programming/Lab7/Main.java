import mpi.MPI;

import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;
import java.util.concurrent.ExecutionException;

public class Main {
    static final int POLYNOMIAL_SIZE = 40000;
    static final String IMPLEMENTATION = "regular";

    public static void master(int processes) {
        Polynomial p1 = new Polynomial(POLYNOMIAL_SIZE);
        p1.generateCoefficients();
        Polynomial p2 = new Polynomial(POLYNOMIAL_SIZE);
        p2.generateCoefficients();

        Instant startTime = Instant.now();

        if (IMPLEMENTATION == "karatsuba") {
            if (p1.getDegree() < 2 || p2.getDegree() < 2) {
                Polynomial result = Common.regularSequential(p1, p2);
                return;
            }

            int m = Math.min(p1.getDegree(), p2.getDegree()) / 2;
            Polynomial low1 = new Polynomial(new ArrayList<>(p1.getCoefficients().subList(0, m)));
            Polynomial high1 = new Polynomial(new ArrayList<>(p1.getCoefficients().subList(m, p1.getSize())));
            Polynomial low2 = new Polynomial(new ArrayList<>(p2.getCoefficients().subList(0, m)));
            Polynomial high2 = new Polynomial(new ArrayList<>(p2.getCoefficients().subList(m, p2.getSize())));

            MPI.COMM_WORLD.Send(new Object[]{low1}, 0, 1, MPI.OBJECT, 1, 0);
            MPI.COMM_WORLD.Send(new Object[]{low2}, 0, 1, MPI.OBJECT, 1, 0);

            MPI.COMM_WORLD.Send(new Object[]{Polynomial.add(low1, high1)}, 0, 1, MPI.OBJECT, 2, 0);
            MPI.COMM_WORLD.Send(new Object[]{Polynomial.add(low2, high2)}, 0, 1, MPI.OBJECT, 2, 0);

            MPI.COMM_WORLD.Send(new Object[]{high1}, 0, 1, MPI.OBJECT, 3, 0);
            MPI.COMM_WORLD.Send(new Object[]{high2}, 0, 1, MPI.OBJECT, 3, 0);

            Object[] result1 = new Object[1];
            MPI.COMM_WORLD.Recv(result1, 0, 1, MPI.OBJECT, 1, 0);
            Polynomial z0 = (Polynomial) result1[0];

            Object[] result2 = new Object[1];
            MPI.COMM_WORLD.Recv(result2, 0, 1, MPI.OBJECT, 2, 0);
            Polynomial z1 = (Polynomial) result2[0];

            Object[] result3 = new Object[1];
            MPI.COMM_WORLD.Recv(result3, 0, 1, MPI.OBJECT, 3, 0);
            Polynomial z2 = (Polynomial) result3[0];

            Polynomial resultPol1 = Polynomial.addZeros(z2, 2 * m);
            Polynomial resultPol2 = Polynomial.addZeros(Polynomial.subtract(Polynomial.subtract(z1, z2), z0), m);
            Polynomial result = Polynomial.add(Polynomial.add(resultPol1, resultPol2), z0);

            Instant endTime = Instant.now();
            long duration = Duration.between(startTime, endTime).toMillis();
            System.out.println("Master's execution time: " + duration);
//            System.out.println(result);
        } else {
            int length = p1.getSize() / (processes - 1);
            int start;
            int end = 0;
            for (int i = 1; i < processes; i++) {
                start = end;
                end = start + length;
                if (i == processes - 1) {
                    end = p1.getSize();
                }
                MPI.COMM_WORLD.Send(new Object[]{p1}, 0, 1, MPI.OBJECT, i, 0);
                MPI.COMM_WORLD.Send(new Object[]{p2}, 0, 1, MPI.OBJECT, i, 0);
                MPI.COMM_WORLD.Send(new int[]{start}, 0, 1, MPI.INT, i, 0);
                MPI.COMM_WORLD.Send(new int[]{end}, 0, 1, MPI.INT, i, 0);
            }
            Object[] results = new Object[processes - 1];
            for (int i = 1; i < processes; i++) {
                MPI.COMM_WORLD.Recv(results, i - 1, 1, MPI.OBJECT, i, 0);
            }
            Polynomial result = Common.getResult(results);

            Instant endTime = Instant.now();
            long duration = Duration.between(startTime, endTime).toMillis();
            System.out.println("Master's execution time: " + duration);
//            System.out.println(result);
        }
    }

    public static void regularWorker(int me) {
        Instant startTime = Instant.now();
        Object[] p1 = new Object[2];
        Object[] p2 = new Object[2];
        int[] start = new int[1];
        int[] end = new int[1];

        MPI.COMM_WORLD.Recv(p1, 0, 1, MPI.OBJECT, 0, 0);
        MPI.COMM_WORLD.Recv(p2, 0, 1, MPI.OBJECT, 0, 0);
        MPI.COMM_WORLD.Recv(start, 0, 1, MPI.INT, 0, 0);
        MPI.COMM_WORLD.Recv(end, 0, 1, MPI.INT, 0, 0);

        Polynomial pol1 = (Polynomial) p1[0];
        Polynomial pol2 = (Polynomial) p2[0];

        Polynomial result = Common.multiplySequence(pol1, pol2, start[0], end[0]);
        MPI.COMM_WORLD.Send(new Object[]{result}, 0, 1, MPI.OBJECT, 0, 0);
        Instant endTime = Instant.now();
        long duration = Duration.between(startTime, endTime).toMillis();
        System.out.println("Worker " + me + " (" + start[0] + ", " + end[0] + ") execution time: " + duration);
    }

    public static void karatsubaWorker(int me) throws ExecutionException, InterruptedException {
        Instant startTime = Instant.now();
        Object[] p1 = new Object[2];
        Object[] p2 = new Object[2];
        int[] start = new int[1];
        int[] end = new int[1];

        MPI.COMM_WORLD.Recv(p1, 0, 1, MPI.OBJECT, 0, 0);
        MPI.COMM_WORLD.Recv(p2, 0, 1, MPI.OBJECT, 0, 0);

        Polynomial pol1 = (Polynomial) p1[0];
        Polynomial pol2 = (Polynomial) p2[0];

        Polynomial result = Common.KaratsubaParallel(pol1, pol2, 1);
        MPI.COMM_WORLD.Send(new Object[]{result}, 0, 1, MPI.OBJECT, 0, 0);
        Instant endTime = Instant.now();
        long duration = Duration.between(startTime, endTime).toMillis();
        System.out.println("Worker " + me + " (" + start[0] + ", " + end[0] + ") execution time: " + duration);
    }

    public static void main(String[] args) throws ExecutionException, InterruptedException {
        MPI.Init(args);
        int me = MPI.COMM_WORLD.Rank();
        int size = MPI.COMM_WORLD.Size();

        if (me == 0) {
            System.out.println("Master process: rank -> " + me + "\n");

            master(size);
        } else {
            System.out.println("Worker process: rank -> " + me + "\n");
            if (IMPLEMENTATION.equalsIgnoreCase("regular")) {
                regularWorker(me);
            }
            else if (IMPLEMENTATION.equalsIgnoreCase("karatsuba")) {
                karatsubaWorker(me);
            }
        }
        MPI.Finalize();
    }
}