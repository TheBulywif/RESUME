def fibonacci(n):
    # SET FIRST TWO NUMBERS
    fib = [0, 1]

    # GENERATE ADDITION NUMBERS IN THE SEQUENCE
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib


if __name__ == '__main__':
    # GENERATE FIRST 100 NUMBERS WITH OUTPUT
    fib_seq = fibonacci(100)
    for var in fib_seq:
        print(var)
    # ASSERTION TO VALIDATE RESULTS
    assert fib_seq[0] == 0
    assert fib_seq[1] == 1
    assert fib_seq[2] == 1
    assert fib_seq[3] == 2
    assert fib_seq[4] == 3
