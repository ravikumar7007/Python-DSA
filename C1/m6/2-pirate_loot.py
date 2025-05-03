def pirate_loot(n, values):
    total_sum = sum(values)
    if n < 3 or total_sum % 3 != 0:
        return 0

    target = total_sum // 3
    dp = [[[False] * (target + 1) for _ in range(target + 1)] for _ in range(n + 1)]
    dp[0][0][0] = True

    for i in range(1, n + 1):
        for j in range(target + 1):
            for k in range(target + 1):
                dp[i][j][k] = dp[i - 1][j][k]
                if j >= values[i - 1]:
                    dp[i][j][k] = dp[i][j][k] or dp[i - 1][j - values[i - 1]][k]
                if k >= values[i - 1]:
                    dp[i][j][k] = dp[i][j][k] or dp[i - 1][j][k - values[i - 1]]

    return 1 if dp[n][target][target] else 0


if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))
    print(pirate_loot(n, values))
