def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        m = (left + right) // 2
        if arr[m] == target:
            return m
        elif arr[m] < target:
            left = m + 1
        else:
            right = m - 1
    return -1


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    target_arr = list(map(int, input().split()))
    for i in range(m):
        result = binary_search(arr, target_arr[i])
        print(result, end=" ")
