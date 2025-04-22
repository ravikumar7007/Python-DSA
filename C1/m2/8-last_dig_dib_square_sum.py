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
    if n <= 1:
        return n
    for _ in range(n - 1):
        prev, curr = curr, (prev + curr) % m
    return curr


def lastDigitFibSquareSum(n):
    if n <= 1:
        return n
    # Using the property: Sum(F(i)^2) = F(n) * F(n+1)
    fn = fibonacci_modulo(n, 10)
    fn_plus_1 = fibonacci_modulo(n + 1, 10)
    return (fn * fn_plus_1) % 10


if __name__ == '__main__':
    n = int(input())
    print(lastDigitFibSquareSum(n))
