def lastDigitFibonacciSum(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    sum = prev+curr
    for _ in range(2, n+1):
        prev, curr = curr, (prev+curr)
        sum += curr
    return sum % 10


if __name__ == "__main__":
    n = int(input())
    print(lastDigitFibonacciSum(n))
