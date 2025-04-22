def lcm_gcd(a, b):
    return a*b//gcd_euclid(a, b)


def gcd_euclid(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcd_euclid(a % b, b)
    else:
        return gcd_euclid(a, b % a)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm_gcd(a, b))
