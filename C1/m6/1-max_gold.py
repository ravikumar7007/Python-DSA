def max_gold(W, n, weights):
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                value = dp[i - 1][w - weights[i - 1]] + weights[i - 1]
                dp[i][w] = max(dp[i - 1][w], value)
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]


if __name__ == "__main__":
    W, n = map(int, input().split())
    weights = list(map(int, input().split()))
    print(max_gold(W, n, weights))
