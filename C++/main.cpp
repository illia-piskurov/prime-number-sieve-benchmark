#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>

std::vector<bool> sieve(int limit) {
    std::vector<bool> primes(limit + 1, true);
    primes[0] = primes[1] = false;

    for (int p = 2; p * p <= limit; ++p) {
        if (primes[p]) {
            for (int i = p * p; i <= limit; i += p) {
                primes[i] = false;
            }
        }
    }

    return primes;
}

int main() {
    int limit = 1000000000;

    auto start = std::chrono::high_resolution_clock::now();

    auto primes = sieve(limit);

    auto stop = std::chrono::high_resolution_clock::now();

    int count = 0;
    for (bool isPrime : primes) {
        if (isPrime) {
            count++;
        }
    }

    std::chrono::duration<double> duration = stop - start;
    std::cout << duration.count() << std::endl;

    return 0;
}
