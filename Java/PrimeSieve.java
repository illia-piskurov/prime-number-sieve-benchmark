import java.util.BitSet;

public class PrimeSieve {

    public static BitSet sieve(int limit) {
        BitSet primes = new BitSet(limit + 1);
        primes.set(0, limit + 1);
        primes.clear(0);
        primes.clear(1);

        for (int p = 2; p * p <= limit; p++) {
            if (primes.get(p)) {
                for (int multiple = p * p; multiple <= limit; multiple += p) {
                    primes.clear(multiple);
                }
            }
        }

        return primes;
    }

    public static void main(String[] args) {
        int limit = 1000000000;

        long startTime = System.nanoTime();

        BitSet primes = sieve(limit);

        long endTime = System.nanoTime();
        double duration = (endTime - startTime) / 1e9;

        int count = 0;
        for (int i = 2; i <= limit; i++) {
            if (primes.get(i)) {
                count++;
            }
        }

        System.out.printf("%.6f\n", duration);
    }
}
