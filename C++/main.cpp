#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>

std::vector<bool> sieve(int limit) {
    std::vector<bool> primes(limit + 1, true);  // Массив для хранения информации о простоте чисел
    primes[0] = primes[1] = false;  // 0 и 1 не являются простыми

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
    int limit = 1000000000;  // Измените это число для тестов

    // Начало отсчета времени
    auto start = std::chrono::high_resolution_clock::now();

    // Выполнение алгоритма решета Эратосфена
    auto primes = sieve(limit);

    // Окончание отсчета времени
    auto stop = std::chrono::high_resolution_clock::now();

    // Подсчет количества простых чисел
    int count = 0;
    for (bool isPrime : primes) {
        if (isPrime) {
            count++;
        }
    }

    // Вычисление времени в секундах
    std::chrono::duration<double> duration = stop - start;
    std::cout << duration.count() << std::endl;

    return 0;
}
