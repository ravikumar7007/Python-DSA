def majority_element(arr):
    count_map = {}
    n = len(arr)

    for i in range(n):
        count_map[arr[i]] = count_map.get(arr[i], 0) + 1
        if count_map[arr[i]] > n // 2:
            return 1

    return 0


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(majority_element(arr))
