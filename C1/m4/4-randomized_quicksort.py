import random


import random


def partition(arr, low, high):
    rand = random.randint(low, high)
    arr[high], arr[rand] = arr[rand], arr[high]  # Randomly select pivot
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:  # Include equality to handle duplicates
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    while low < high:  # Use tail recursion optimization
        pi = partition(arr, low, high)
        if pi - low < high - pi:  # Recur for the smaller partition first
            quick_sort(arr, low, pi - 1)
            low = pi + 1
        else:
            quick_sort(arr, pi + 1, high)
            high = pi - 1
    return arr


def simple_quick_sort(arr, low, high):
    if len(arr) <= 1:
        return arr
    pi = random.randint(low, high)
    less = [el for el in arr if el < arr[pi]]
    equal = [el for el in arr if el == arr[pi]]
    more = [el for el in arr if el > arr[pi]]
    return (
        simple_quick_sort(less, 0, len(less) - 1)
        + equal
        + simple_quick_sort(more, 0, len(more) - 1)
    )


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    arr = simple_quick_sort(arr, 0, n - 1)
    print(*arr)
