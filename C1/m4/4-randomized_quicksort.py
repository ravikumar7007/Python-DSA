import random


def partition(arr, low, high):
    rand = random.randint(low, high)
    arr[high], arr[rand] = arr[rand], arr[high]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_quick(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        randomized_quick(arr, low, pi - 1)
        randomized_quick(arr, pi + 1, high)
    return arr


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    arr = randomized_quick(arr, 0, n - 1)
    print(*arr)
