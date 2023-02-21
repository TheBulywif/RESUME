def fibonacci(n):
    fib = [0, 1]

    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib


if __name__ == '__main__':
    fib_seq = fibonacci(100)
    for var in fib_seq:
        print(var)
    assert fib_seq[0] == 0
    assert fib_seq[1] == 1
    assert fib_seq[2] == 1
    assert fib_seq[3] == 2
    assert fib_seq[4] == 3
