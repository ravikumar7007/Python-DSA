def last_digit_of_fibonacci(n, m):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n+1):
        prev, curr = curr, prev + curr
    return curr % m


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(last_digit_of_fibonacci(n, m))
