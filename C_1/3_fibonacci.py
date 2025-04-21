def fibonacci(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_fast(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib: list[int] = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1]+fib[i-2])

    return fib[n]


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"The {n}th Fibonacci number is: {fibonacci_fast(n)}")
