def moneychange(n: int) -> int:
    return n // 10 + (n % 10) // 5 + (n % 5) // 1

if __name__ == "__main__":
    n= int(input())
    print(moneychange(n))