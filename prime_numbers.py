def generate_primes(n):
    primes = [2]
    num = 3
    while len(primes) < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 2
    return primes


if __name__ == '__main__':
    primes = generate_primes(100)
    for prime in primes:
        print(prime)

    assert primes[0] == 2
    assert primes[1] == 3
    assert primes[2] == 5
    assert primes[3] == 7
    assert primes[4] == 11
