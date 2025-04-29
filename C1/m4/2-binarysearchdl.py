def binary_search_duplicate(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1
    while left <= right:
        m = (left + right) // 2
        if arr[m] == target:
            result = m
            right = m - 1  # Continue searching in the left half for duplicates
        elif arr[m] < target:
            left = m + 1
        else:
            right = m - 1
    return result


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    target_arr = list(map(int, input().split()))
    for i in range(m):
        result = binary_search_duplicate(arr, target_arr[i])
        print(result, end=" ")
