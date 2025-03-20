import time
import numpy as np

def sieve(limit):
    primes = np.ones(limit + 1, dtype=bool)
    primes[:2] = False
    
    for p in range(2, int(limit**0.5) + 1):
        if primes[p]:
            primes[p * p::p] = False
    
    return primes

limit = 1000000000
start = time.time()
primes = sieve(limit)
duration = time.time() - start

count = np.sum(primes)
print(f"{duration:.6f}")
