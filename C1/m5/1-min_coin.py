def min_coin(money):
    dp = [money] * (money + 1)
    dp[0] = 0

    for i in range(1, money + 1):
        for coin in [1, 3, 4]:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[money]


if __name__ == "__main__":
    money = int(input())
    print(min_coin(money))
