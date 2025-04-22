def lastDigitFibonacciPartialSum(start, end):
    if start > end:
        return 0
    if end <= 1:
        return end
    prev, curr = 0, 1
    sum = prev+curr
    for _ in range(2, end+1):
        prev, curr = curr, (prev+curr) % 10
        if _ >= start:
            sum += curr
    return sum % 10


if __name__ == "__main__":
    start, end = map(int, input().split())
    print(lastDigitFibonacciPartialSum(start, end))
