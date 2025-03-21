use bit_vec::BitVec;
use std::time::Instant;

fn sieve(limit: usize) -> BitVec {
    let mut primes = BitVec::from_elem(limit + 1, true);
    primes.set(0, false);
    primes.set(1, false);

    for p in 2..=((limit as f64).sqrt() as usize) {
        if primes[p] {
            for i in (p * p..=limit).step_by(p) {
                primes.set(i, false);
            }
        }
    }

    primes
}

fn main() {
    let limit = 1_000_000_000;

    let start = Instant::now();

    let primes = sieve(limit);

    let stop = Instant::now();

    let count = primes.iter().filter(|&is_prime| is_prime).count();

    let duration = stop.duration_since(start);
    println!("{}", duration.as_secs_f64());
}
