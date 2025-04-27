def max_distinct_summands(n):
    summands = []
    curr = 1
    while n > 0:
        if n - curr > curr:
            summands.append(curr)
            n -= curr
            curr += 1
        else:
            summands.append(n)
            break
    return summands

if __name__ == "__main__":
    n = int(input())
    summands = max_distinct_summands(n)
    print(len(summands))
    print(*summands)
