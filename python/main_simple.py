import time

def sieve(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    
    for p in range(2, int(limit**0.5) + 1):
        if primes[p]:
            for multiple in range(p * p, limit + 1, p):
                primes[multiple] = False
    
    return primes

limit = 1000000000
start = time.time()
primes = sieve(limit)
duration = time.time() - start

count = sum(primes)
print(f"{duration:.6f}")
