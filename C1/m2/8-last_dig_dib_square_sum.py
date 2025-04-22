def lastDigitFibSquareSum(n):
    if n <= 1:
        return n

    prev, curr = 0, 1
    sum = 1
    for _ in range(2, n+1):
        prev, curr = curr, (prev+curr) % 10
        sum += curr*curr

    return sum % 10


if __name__ == '__main__':
    n = int(input())
    print(lastDigitFibSquareSum(n))
