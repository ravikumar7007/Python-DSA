def primitive_calculator(n):
    dp = [n] * (n + 1)
    dp[1] = 0
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    sequence = []
    curr = n
    while curr > 0:
        sequence.append(curr)
        if curr == 1:
            break
        if dp[curr] == dp[curr - 1] + 1:
            curr -= 1
        elif curr % 2 == 0 and dp[curr] == dp[curr // 2] + 1:
            curr = curr // 2
        elif curr % 3 == 0 and dp[curr] == dp[curr // 3] + 1:
            curr = curr // 3

    sequence.reverse()
    return dp[n], sequence


if __name__ == "__main__":
    n = int(input())
    min_operations, sequence = primitive_calculator(n)
    print(min_operations)
    print(*sequence)
