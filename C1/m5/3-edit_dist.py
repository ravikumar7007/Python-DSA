def edit_dist(s1, s2):
    m = len(s1)
    n = len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j]
            else:
                dp[i + 1][j + 1] = 1 + min(dp[i + 1][j], dp[i][j], dp[i][j + 1])

    return dp[m][n]


if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(edit_dist(s1, s2))
