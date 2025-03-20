package main

import (
    "fmt"
    "time"
)

func sieve(limit int) []bool {
    primes := make([]bool, limit+1)
    for i := range primes {
        primes[i] = true
    }
    primes[0], primes[1] = false, false

    for p := 2; p*p <= limit; p++ {
        if primes[p] {
            for i := p * p; i <= limit; i += p {
                primes[i] = false
            }
        }
    }
    return primes
}

func main() {
    limit := 1000000000
    start := time.Now()
    primes := sieve(limit)
    duration := time.Since(start)

    count := 0
    for _, isPrime := range primes {
        if isPrime {
            count++
        }
    }
    
    fmt.Printf("%v\n", duration)
}
