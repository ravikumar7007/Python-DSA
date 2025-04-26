def max_array(arr):
    max_val = arr[0]
    max_index = 0
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_index = i
    return max_val, max_index


def max_ads(n, prices, clicks):
    result = 0
    for i in range(n):
        max_price, max_price_index = max_array(prices)
        max_clicks, max_clicks_index = max_array(clicks)
        result += max_price * max_clicks
        prices[max_price_index] = -1
        clicks[max_clicks_index] = -1
    return result


if __name__ == "__main__":
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    print(max_ads(n, prices, clicks))
