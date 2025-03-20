using System.Diagnostics;
using System.Collections;

class Program
{
    static BitArray Sieve(int limit)
    {
        BitArray primes = new BitArray(limit + 1, true);
        primes[0] = primes[1] = false;

        for (int p = 2; p * p <= limit; p++)
        {
            if (primes[p])
            {
                for (int multiple = p * p; multiple <= limit; multiple += p)
                {
                    primes[multiple] = false;
                }
            }
        }

        return primes;
    }

    static void Main()
    {
        int limit = 1000000000;

        Stopwatch stopwatch = Stopwatch.StartNew();
        BitArray primes = Sieve(limit);
        stopwatch.Stop();

        int count = 0;
        foreach (bool isPrime in primes)
        {
            if (isPrime)
            {
                count++;
            }
        }

        Console.WriteLine($"{stopwatch.ElapsedMilliseconds / 1000.0:F6}");
    }
}
