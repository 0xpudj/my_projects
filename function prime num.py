def is_prime(n):
    if n <= 1:
        return False  
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  
    return True

def first_n_primes(n=10):
    primes = []
    number = 2  
    while len(primes) < n:
        if is_prime(number):
            primes.append(number)
        number += 1
    return primes

n=int(input())
print(first_n_primes(n))
