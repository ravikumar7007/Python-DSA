def pisano_period(m):
    prev, curr = 0, 1
    for i in range(0, m * m):
        prev, curr = curr, (prev + curr) % m
        if prev == 0 and curr == 1:
            return i + 1


def fibonacci_modulo(n, m):
    if n <= 1:
        return n
    pisano_value = pisano_period(m)
    n = n % pisano_value
    prev, curr = 0, 1
    for _ in range(n - 1):
        prev, curr = curr, (prev + curr) % m
    return curr


def lastDigitFibonacciSum(n):
    lastDigitFibonacciSumPlus2 = fibonacci_modulo(n + 2, 10)
    return (lastDigitFibonacciSumPlus2 - 1) % 10


if __name__ == "__main__":
    n = int(input())
    print(lastDigitFibonacciSum(n))
