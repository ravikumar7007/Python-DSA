def knapsack(weights, values, W, n):
    value = 0
    while n > 0 and W > 0:
        best_price = 0
        best_index = -1
        for i in range(n):
            if values[i] / weights[i] > best_price:
                best_price = values[i] / weights[i]
                best_index = i

        a = min(W, weights[best_index])
        value += a * best_price
        W = W - a
        values[best_index] = 0
    return value


if __name__ == "__main__":
    n, W = map(int, input().split())
    weights = [0] * n
    values = [0] * n
    for i in range(n):
        values[i], weights[i] = map(int, input().split())

    result = knapsack(weights, values, W, n)
    print(f"{result:.4f}")  # upto 4 decimal places
