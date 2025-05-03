import re


def maximize_expression(expression):
    nums = []
    ops = []

    for i in range(len(expression)):
        if expression[i].isdigit():
            nums.append(int(expression[i]))
        else:
            ops.append(expression[i])

    n = len(nums)
    min_dp = [[0] * n for _ in range(n)]
    max_dp = [[0] * n for _ in range(n)]

    for i in range(n):
        min_dp[i][i] = nums[i]
        max_dp[i][i] = nums[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            min_dp[i][j], max_dp[i][j] = compute_min_max(i, j, min_dp, max_dp, ops)

    return max_dp[0][n - 1]


def compute_min_max(i, j, min_dp, max_dp, ops):
    min_val = float("inf")
    max_val = float("-inf")

    for k in range(i, j):
        op = ops[k]
        if op == "+":
            min_val = min(min_val, min_dp[i][k] + min_dp[k + 1][j])
            max_val = max(max_val, max_dp[i][k] + max_dp[k + 1][j])
        elif op == "-":
            min_val = min(min_val, min_dp[i][k] - max_dp[k + 1][j])
            max_val = max(max_val, max_dp[i][k] - min_dp[k + 1][j])
        elif op == "*":
            min_val = min(min_val, min_dp[i][k] * min_dp[k + 1][j])
            max_val = max(max_val, max_dp[i][k] * max_dp[k + 1][j])

    return min_val, max_val


if __name__ == "__main__":
    expression = input().strip()
    # Remove spaces and parentheses from the expression
    expression = re.sub(r"[()]", "", expression)
    print(maximize_expression(expression))
