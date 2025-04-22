def pisano_period(m):
    prev, curr = 0, 1
    for i in range(0, m * m):
        prev, curr = curr, (prev + curr) % m
        if prev == 0 and curr == 1:
            return i + 1


def last_digit_of_fibonacci(n, m):
    if n <= 1:
        return n
    pisano_value = pisano_period(m)
    n = n % pisano_value
    prev, curr = 0, 1
    for _ in range(2, n+1):
        prev, curr = curr, prev + curr
    return curr % m


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(last_digit_of_fibonacci(n, m))
