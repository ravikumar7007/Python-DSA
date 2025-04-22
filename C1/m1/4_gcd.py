def naive_gcd(a, b):
    result = min(a, b)
    while result > 0:
        if a % result == 0 and b % result == 0:
            return result
        result -= 1
    return 1


def gcd_euclidean(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    if a > b:
        return gcd_euclidean(a % b, b)
    else:
        return gcd_euclidean(a, b % a)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(naive_gcd(a, b))
    print(gcd_euclidean(a, b))
