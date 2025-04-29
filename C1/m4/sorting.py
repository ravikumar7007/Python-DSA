from calendar import c
import time
import random

def selection_sort(arr):
    l = len(arr)
    for i in range(l):
        min = i
        for j in range(i + 1, l):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


def merge(A, B):
    C = [0] * (len(A) + len(B))
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C[i + j] = A[i]
            i += 1
        else:
            C[i + j] = B[j]
            j += 1
    while i < len(A):
        C[i + j] = A[i]
        i += 1
    while j < len(B):
        C[i + j] = B[j]
        j += 1
    return C


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)


def partition(arr, low, high):
    pivot = random.randint(low, high)
    arr[high], arr[pivot] = arr[pivot], arr[high]
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr


def count_sort(arr):
    max = -1
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    count = [0] * (max + 1)

    for i in range(len(arr)):
        count[arr[i]] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [0] * len(arr)

    for i in range(len(arr) - 1, -1, -1):  # Iterate in reverse to maintain stability
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return output


# mylist = [2, 19, 3, 17, 5, 13, 7, 11, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
mylist = [random.randint(1, 1000000) for _ in range(1000000)]

# s_start = time.time()
# selsort = selection_sort(mylist)
# s_end = time.time()

mstr = time.time()
mersort = merge_sort(mylist)
m_end = time.time()

q_str = time.time()
quisort = quick_sort(mylist, 0, len(mylist) - 1)
q_end = time.time()

d_str = time.time()
def_sort = mylist.sort()
d_end = time.time()

c_str = time.time()
countsort = count_sort(mylist)
c_end = time.time()

# s_time = (s_end - s_start) * 1000
m_time = (m_end - mstr) * 1000
c_time = (c_end - c_str) * 1000

# print(f"Selection Sort Time: {s_time:.2f} ms")
print(f"Merge Sort Time: {m_time:.2f} ms")
print(f"Count Sort Time: {c_time:.2f} ms")
print("Quick Sort Time: ", (q_end - q_str) * 1000, "ms")
print("Default Sort Time: ", (d_end - d_str) * 1000, "ms")

# # print list
# print("Original list:", mylist)
# print("Sorted list using Selection Sort:", selsort)
# print("Sorted list using Merge Sort:", mersort)
# print("Sorted list using Count Sort:", countsort)
# print("Sorted list using Quick Sort:", quisort)

# check if the sorted lists are equal
if mersort == countsort == quisort == def_sort:
    print("All sorting algorithms produced the same result.")
else:
    print("All sorting algorithms produced different results.")
