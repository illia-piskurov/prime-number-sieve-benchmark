const { performance } = require('perf_hooks');

function sieve(limit) {
    const primes = new Uint8Array(limit + 1);
    primes.fill(1);
    primes[0] = primes[1] = 0;

    for (let p = 2; p * p <= limit; p++) {
        if (primes[p]) {
            for (let i = p * p; i <= limit; i += p) {
                primes[i] = 0;
            }
        }
    }

    return primes;
}

function main() {
    const limit = 1000000000;
    const start = performance.now();

    const primes = sieve(limit);

    const end = performance.now();
    console.log((end - start) / 1000);
}

main();
