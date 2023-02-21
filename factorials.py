import math
import random


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    # CALCULATE FACTORIALS AND ASSERT RESULTS
    for i in range(5):
        n = random.randint(1, 10)
        result = factorial(n)
        print(f"{n}! = {result}")
        assert result == math.factorial(n)
